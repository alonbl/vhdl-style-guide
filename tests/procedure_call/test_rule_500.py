import os
import unittest

from vsg.rules import procedure_call
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_500_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_500_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_500_test_input.fixed_upper.vhd"), lExpected_upper)


class test_procedure_call_statement_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_500_lower(self):
        oRule = procedure_call.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "500")

        lExpected = [8, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_500_upper(self):
        oRule = procedure_call.rule_500()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "500")

        lExpected = [6, 14]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_500_lower(self):
        oRule = procedure_call.rule_500()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_500_upper(self):
        oRule = procedure_call.rule_500()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
