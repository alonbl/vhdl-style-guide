import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import file_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_100_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_100_test_input.fixed.vhd"), lExpected)


class test_file_declaration_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_100(self):
        oRule = file_statement.rule_100()
        self.assertTrue(oRule)
        self.assertTrue(oRule.disable)
        self.assertEqual(oRule.name, "file")
        self.assertEqual(oRule.identifier, "100")

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_100(self):
        oRule = file_statement.rule_100()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
