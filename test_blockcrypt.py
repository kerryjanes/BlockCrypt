# test_blockcrypt.py
"""
Tests for BlockCrypt module.
"""

import unittest
from blockcrypt import BlockCrypt

class TestBlockCrypt(unittest.TestCase):
    """Test cases for BlockCrypt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockCrypt()
        self.assertIsInstance(instance, BlockCrypt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockCrypt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
