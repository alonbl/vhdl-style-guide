import os
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

lBresenhamer = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'Bresenhamer.vhd'))
oBresenhamer = vhdlFile.vhdlFile(lBresenhamer)
lDebouncer = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'Debouncer.vhd'))
oDebouncer = vhdlFile.vhdlFile(lDebouncer)
lVgatop = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'VGA_Top.vhd'))
oVgatop = vhdlFile.vhdlFile(lVgatop)
lPointer = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'Pointer.vhd'))
oPointer = vhdlFile.vhdlFile(lPointer)
lFreqDiv = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'FreqDiv.vhd'))
oFreqDiv = vhdlFile.vhdlFile(lFreqDiv)
lSynchronizer = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'Synchronizer.vhd'))
oSynchronizer = vhdlFile.vhdlFile(lSynchronizer)
lFrameBuffer =  utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'FrameBuffer2.vhd'))
oFrameBuffer =  vhdlFile.vhdlFile(lFrameBuffer)

dLegacyConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','styles', 'legacy.yaml'))

class testCodeExample(unittest.TestCase):

    def test_bresenhamer(self):
        oRuleList = rule_list.rule_list(oBresenhamer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Bresenhamer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBresenhamer.lines[iLineNumber].line, sLine)

    def test_debouncer(self):
        oRuleList = rule_list.rule_list(oDebouncer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Debouncer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oDebouncer.lines[iLineNumber].line, sLine)

    def test_vga_top(self):
        oRuleList = rule_list.rule_list(oVgatop)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'VGA_Top.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oVgatop.lines[iLineNumber].line, sLine)

    def test_pointer(self):
        oRuleList = rule_list.rule_list(oPointer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Pointer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oPointer.lines[iLineNumber].line, sLine)

    def test_freqdiv(self):
        oRuleList = rule_list.rule_list(oFreqDiv)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'FreqDiv.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oFreqDiv.lines[iLineNumber].line, sLine)

    def test_synchronizer(self):
        oRuleList = rule_list.rule_list(oSynchronizer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Synchronizer.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oSynchronizer.lines[iLineNumber].line, sLine)

    def test_framebuffer(self):
        oRuleList = rule_list.rule_list(oFrameBuffer)
        oRuleList.configure(dLegacyConfig)
        oRuleList.fix(7)
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'FrameBuffer2.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oFrameBuffer.lines[iLineNumber].line, sLine)
