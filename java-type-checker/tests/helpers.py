import unittest
import re


class TypeTest(unittest.TestCase):
    def assertCompileError(self, error, error_message, expr):
        with self.assertRaisesRegex(error, re.escape(error_message)):
            expr.check_types()

    def assertNoCompileErrors(self, expr):
        expr.check_types()
