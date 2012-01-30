'''
Created on Jan 29, 2012

@author: Josiah
'''
import unittest
from brainfuck.brainfuck import Brainfuck
import sys
from StringIO import StringIO



class Test(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def testWorld(self):
        
        br = Brainfuck("++++++++++[>+++++++>+++a+++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
        br.parse()
        self.assertEqual(sys.stdout.getvalue(), "Hello World!\n")
        
        
    """
    def testFib(self):
        with open("fib") as filer:
            file_source = filer.read()
        bran = Brainfuck(file_source)
        bran.parse()
        self.assertEqual(sys.stdout.getvalue(), "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")"""
        
    
    def tearDown(self):
        sys.stdout = self.held


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    