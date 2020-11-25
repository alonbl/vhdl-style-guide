

from vsg import parser
from vsg import rule
from vsg import token
from vsg.vhdlFile import utils
from vsg import violation


class remove_carriage_returns_between_token_pairs(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, lTokens, bInsertSpace=False):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.bInsertSpace = bInsertSpace

    def analyze(self, oFile):

        lToi = []
        for oToken in self.lTokens:
            lToi_a = oFile.get_tokens_bounded_by(oToken[0], oToken[1])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:
                if isinstance(oToken, parser.carriage_return):
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    self.add_violation(oViolation)
                    break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()

        lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        if self.bInsertSpace:
            if not isinstance(lTokens[1], parser.whitespace):
                lTokens.insert(1, parser.whitespace(' '))

        oViolation.set_tokens(lTokens)

