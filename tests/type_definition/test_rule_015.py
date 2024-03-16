import os
import unittest

from vsg.rules import type_definition
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_015_test_input.vhd"))


class test_type_definition_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_015(self):
        oRule = type_definition.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type")
        self.assertEqual(oRule.identifier, "015")

        lExpected = [8]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
