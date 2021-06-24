from chain_of_resp_solution import *
import unittest

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"

chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

class TestChain(unittest.TestCase):
    def test_chain_get(self):
        cases = [42, 3.14, "some text"]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(chain.handle(obj, EventGet(type(case))), case)

    def test_chain_set(self):
        cases = [100, 0.5, "newest text"]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(chain.handle(obj, EventSet(case)), case)


unittest.main()
