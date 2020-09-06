
from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import mode
from vsg.vhdlFile.classify_new import subtype_indication


from vsg.token import interface_unknown_declaration as token

from vsg.vhdlFile import utils

'''
    This is a classification if the signal, constant, or variable keywords can not be found.
    This is not in the VHDL LRM.
    It is based off the interface_signal_declaration as it has the most keywords.

    interface_unknown_declaration ::=
        identifier_list : [ mode ] subtype_indication [ bus ] [ := *static*_expression ]
'''

def detect(iToken, lObjects):
    if utils.is_next_token('type', iToken, lObjects):
        return iToken
    elif utils.is_next_token('file', iToken, lObjects):
        return iToken
    elif utils.is_next_token('function', iToken, lObjects):
        return iToken
    elif utils.is_next_token('procedure', iToken, lObjects):
        return iToken
    elif utils.is_next_token('impure', iToken, lObjects):
        return iToken
    elif utils.is_next_token('pure', iToken, lObjects):
        return iToken
    elif utils.is_next_token('package', iToken, lObjects):
        return iToken
    else:
        return classify(iToken, lObjects)

def classify(iToken, lObjects):
    iCurrent = identifier_list.classify(iToken, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    iCurrent = mode.classify(iCurrent, lObjects)
    sEnd = utils.find_earliest_occurance([')', ';', 'bus'], iCurrent, lObjects)
    if sEnd == 'bus':
        iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('bus', token.bus_keyword, iCurrent, lObjects)
        if utils.is_next_token(':=', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)
            sEnd = utils.find_earliest_occurance([')', ';'], iCurrent, lObjects)
            iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects)
    elif utils.find_in_range(':=', iCurrent, sEnd, lObjects):
        iCurrent = utils.classify_subelement_until(':=', subtype_indication, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)
        iCurrent = utils.classify_subelement_until(sEnd, expression, iCurrent, lObjects)
    else:
        iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects)

    return iCurrent