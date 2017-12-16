
from vsg import rule
from vsg import check
from vsg import fix


class indent_rule(rule.rule):
    '''
    Checks for and fixes indent problems.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None):
        rule.rule.__init__(self, name, identifier)
        # These are filled out when creating a new rule
        self.sTrigger = sTrigger
        # Leave everything below this alone
        self.solution = 'Invalid indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
