import unittest
import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

from tests.test_note import NoteTest

def suite():
    """
    Return a composite test suite.
    """
    notetest_suite = unittest.makeSuite(NoteTest)
    
    suites = (notetest_suite,)
    return unittest.TestSuite(suites)
    
if __name__ == '__main__':
    unittest.main(defaultTest="suite")