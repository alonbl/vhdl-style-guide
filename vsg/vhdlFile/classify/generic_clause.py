
from vsg.token import generic_clause as token


def generic_clause(dVars, lTokens, lObjects, oLine):
    '''
    Classifies generic clauses:

        generic ( generic_list ) ;
    '''
    for iToken, sToken in enumerate(lTokens):
        if not dVars['bGenericClauseKeywordFound']:
            classify_keyword(sToken, iToken, lObjects, dVars)
        else:
            if not dVars['bGenericClauseOpenParenthesisFound']:
                classify_open_parenthesis(sToken, iToken, lObjects, dVars)
            else:
                classify_semicolon(sToken, iToken, lObjects, dVars)
                classify_close_parenthesis(sToken, iToken, lObjects, dVars)


def classify_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'generic':
        lObjects[iToken] = token.keyword(sToken)
        dVars['bGenericClauseKeywordFound'] = True


def classify_open_parenthesis(sToken, iToken, lObjects, dVars):
    if sToken == '(':
        lObjects[iToken] = token.open_parenthesis()
        dVars['bGenericClauseOpenParenthesisFound'] = True


def classify_close_parenthesis(sToken, iToken, lObjects, dVars):
    if sToken == ')':
        lObjects[iToken] = token.close_parenthesis()


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = token.semicolon()
        dVars['bGenericClauseKeywordFound'] = False
        dVars['bGenericClauseOpenParenthesisFound'] = False