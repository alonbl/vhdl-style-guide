
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_026(self):
        oRule = context.rule_026()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [7]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026(self):
        oRule = context.rule_026()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

