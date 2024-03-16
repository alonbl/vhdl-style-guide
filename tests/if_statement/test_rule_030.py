import os
import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_030_test_input.vhd"))

lExpected_require_blank = []
lExpected_require_blank.append("")
utils.read_file(os.path.join(sTestDir, "rule_030_test_input.fixed_require_blank.vhd"), lExpected_require_blank)

lExpected_no_blank = []
lExpected_no_blank.append("")
utils.read_file(os.path.join(sTestDir, "rule_030_test_input.fixed_no_blank.vhd"), lExpected_no_blank)


class test_if_statement_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_030_w_require_blank(self):
        oRule = if_statement.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "if")
        self.assertEqual(oRule.identifier, "030")

        lExpected = [32]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank(self):
        oRule = if_statement.rule_030()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = "no_blank_line"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "if")
        self.assertEqual(oRule.identifier, "030")

        lExpected = [19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = "no_blank_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
