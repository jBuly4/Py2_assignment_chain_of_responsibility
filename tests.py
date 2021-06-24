from chain_of_resp_solution import *
import unittest

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"

chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

class TestChain(unittest.TestCase):
    def test_chain_get_int(self):
        case = 42
        with self.subTest(x=case):
            print(chain.handle(obj, EventGet(type(case))))
            self.assertEqual(chain.handle(obj, EventGet(type(case))), case)

    def test_chain_get_float(self):
        case = 3.14
        with self.subTest(x=case):
            # print(type(case) == float)
            # print(chain.handle(obj, EventGet(type(case))))
            self.assertEqual(chain.handle(obj, EventGet(type(case))), case)

    def test_chain_get_str(self):
        case = "some text"
        with self.subTest(x=case):
            self.assertEqual(chain.handle(obj, EventGet(type(case))), case)


unittest.main()
