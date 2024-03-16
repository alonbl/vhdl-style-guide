import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import type_definition

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_009_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_009_test_input.fixed.vhd"), lExpected)


class test_type_definition_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_009(self):
        oRule = type_definition.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type")
        self.assertEqual(oRule.identifier, "009")
        self.assertEqual(oRule.groups, ["structure"])

        lExpected = [8, 12, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_009(self):
        oRule = type_definition.rule_009()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
