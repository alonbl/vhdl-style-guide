import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import assert_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_003_test_input.vhd"))

dIndentMap = utils.read_indent_file()

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed.vhd"), lExpected)


class test_assert_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_003(self):
        oRule = assert_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "assert")
        self.assertEqual(oRule.identifier, "003")
        self.assertEqual(oRule.groups, ["structure"])

        lExpected = [10, 15, 22, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003(self):
        oRule = assert_statement.rule_003()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
