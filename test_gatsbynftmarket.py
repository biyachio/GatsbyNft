# test_gatsbynftmarket.py
"""
Tests for GatsbyNftMarket module.
"""

import unittest
from gatsbynftmarket import GatsbyNftMarket

class TestGatsbyNftMarket(unittest.TestCase):
    """Test cases for GatsbyNftMarket class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GatsbyNftMarket()
        self.assertIsInstance(instance, GatsbyNftMarket)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GatsbyNftMarket()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
