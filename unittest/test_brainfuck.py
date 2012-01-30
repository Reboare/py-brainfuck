'''
Created on Jan 29, 2012

@author: Josiah
'''
import unittest
from brainfuck.brainfuck import Brainfuck
import sys, multiprocessing, cStringIO
import doctest


class Test(unittest.TestCase):


    def testWorld(self):
        br = Brainfuck("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
        bar = cStringIO.StringIO()
        sys.stdout = bar
        br.parse()
        self.assertEqual(bar.getvalue(), "Hello World!\n")
    
    
 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    