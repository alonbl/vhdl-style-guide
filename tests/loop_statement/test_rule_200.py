# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import loop_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_200_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_200_test_input.fixed.vhd"), lExpected)


class test_loop_statement_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_200(self):
        oRule = loop_statement.rule_200()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "loop_statement")
        self.assertEqual(oRule.identifier, "200")

        lExpected = [32, 35, 38, 41]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_200(self):
        oRule = loop_statement.rule_200()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
