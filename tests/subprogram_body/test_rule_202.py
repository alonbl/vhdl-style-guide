import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import subprogram_body

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_202_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_202_test_input.fixed.vhd"), lExpected, False)


class test_subprogram_body_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_202(self):
        oRule = subprogram_body.rule_202()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "subprogram_body")
        self.assertEqual(oRule.identifier, "202")

        lExpected = [47, 55]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_202(self):
        oRule = subprogram_body.rule_202()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
