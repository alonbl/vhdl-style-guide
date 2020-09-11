
from vsg.token import variable_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import signal_kind
from vsg.vhdlFile.classify_new import subtype_indication


'''
    variable_declaration ::=
        [ shared ] variable identifier_list : subtype_indication [ := expression ] ;
'''


def detect(iToken, lObjects):

    if utils.is_next_token('shared', iToken, lObjects):
        return classify(iToken, lObjects)    
    elif utils.is_next_token('variable', iToken, lObjects):
        return classify(iToken, lObjects)    

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('shared', token.shared_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('variable', token.variable_keyword, iCurrent, lObjects)
    iCurrent = identifier_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    sEnd = utils.find_earliest_occurance([';', ':='], iCurrent, lObjects)
    iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects) 
    iCurrent = signal_kind.detect(iToken, lObjects)
    sEnd = utils.find_earliest_occurance([';', ':='], iCurrent, lObjects)
    if utils.is_next_token(':=', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(':=', token.assignment_operator, iCurrent, lObjects)
        iCurrent = utils.classify_subelement_until(';', expression, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent 