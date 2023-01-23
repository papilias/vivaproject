import unittest
from serviceA import ServiceA

class TestServiceA(unittest.TestCase):
    def setUp(self):
        self.serviceA = ServiceA()

    def test_start(self):
        # test the start method of ServiceA
        pass

    def test_call_b_and_c(self):
        # test the call_b_and_c