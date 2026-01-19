# Basic Test Script for Mining Bot

import unittest
from mining_bot import MiningBot

class TestMiningBot(unittest.TestCase):
    def setUp(self):
        self.bot = MiningBot()

    def test_start_mining(self):
        self.bot.start_mining()
        self.assertTrue(self.bot.is_mining_active())

    def test_stop_mining(self):
        self.bot.stop_mining()
        self.assertFalse(self.bot.is_mining_active())

if __name__ == '__main__':
    unittest.main()