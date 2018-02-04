# -*- coding: utf-8 -*-

from java_type_checker import *
from tests.fixtures import Graphics
import unittest


class TestTypeRelationships(unittest.TestCase):

    def test_type_is_its_own_subtype(self):
        self.assert_subtype(Graphics.rectangle, Graphics.rectangle)

    def test_subtype_includes_direct_supertypes(self):
        self.assert_subtype(Graphics.graphics_group, Graphics.graphics_object)
        self.assert_not_subtype(Graphics.graphics_object, Graphics.graphics_group)

    def test_subtype_includes_indirect_supertypes(self):
        self.assert_subtype(Graphics.color, Type.object)
        self.assert_not_subtype(Type.object, Graphics.color)

    def test_subtype_does_not_include_unrelated_types(self):
        self.assert_not_subtype(Graphics.color, Graphics.point)
        self.assert_not_subtype(Graphics.point, Graphics.color)

    # ––– Helpers –––

    def assert_subtype(self, type0, type1):
        self.assertTrue(type0.is_subtype_of(type1))
        self.assertTrue(type1.is_supertype_of(type0))

    def assert_not_subtype(self, type0, type1):
        self.assertFalse(type0.is_subtype_of(type1))
        self.assertFalse(type1.is_supertype_of(type0))


if __name__ == '__main__':
    unittest.main()
