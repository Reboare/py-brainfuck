"""
brainfuck.py
An attempt at writing a brainfuck interpreter in python
"""
import sys

class Brainfuck(object):
    """Simple Interpreter of Brainfuck Programs"""
    __tree = {}
    __pointer = 0
    __current_val = 0 
    __output = ""
    
    
    def __init__(self, text):
        """Text must be the unicode data to be passed to the class 
        which is then parsed
        """
        commands = ["+", "-", ".", ",", "[", "]", ">", "<"]
        self.code = [x for x in text if x in commands ]   
        
    def __instruction(self, node):
        """Maps every instruction but the loop to 
        a python instruction.  Soon to be merged
        with parse"""      
        if node == "+":
            self.__current_val += 1
            self.__tree[self.__pointer] = self.__current_val
        elif node == "-":
            self.__current_val -= 1
            self.__tree[self.__pointer] = self.__current_val
        elif node == ">":
            self.__pointer += 1
            self.__current_val = self.__tree.get(self.__pointer, 0)
            
        elif node == "<":
            self.__pointer -= 1
            self.__current_val = self.__tree.get(self.__pointer, 0) 
        elif node == ",":
            self.__tree[self.__pointer] = ord(sys.stdin.read(1))  
        elif node == ".":
            arg = chr(self.__tree[self.__pointer])
            sys.stdout.write(arg)
            sys.stdout.flush()
            
    def __generate_brace_map(self):
        """Parses over the instruction set and returns a list containing 
        coordinates of any matching brace sets, allowing easier loop 
        traversal
        """
        instructions = self.code
        left_braces = []
        brace_map = []
        for pos, each in enumerate(instructions):
            if each == "[": 
                left_braces.append(pos)
            if each == "]": 
                brace_map.append([left_braces[-1], pos])   
        return brace_map
    
    def parse(self):
        """Takes a __clean set of instructions and operates on the __tree"""
        point = 0
        instructions = self.code
        brace_map = self.__generate_brace_map()
        while point < len(instructions):
            if instructions[point] != "]" and instructions[point] != "[":
                self.__instruction(instructions[point])
            elif instructions[point] == "[" and self.__current_val == 0:
                for left, right in brace_map:
                    if left == point: 
                        point = right
            elif instructions[point] == "]" and self.__current_val != 0:
                for left, right in brace_map:
                    if right == point: 
                        point = left
            point += 1