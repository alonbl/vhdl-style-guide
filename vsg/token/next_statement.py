# -*- coding: utf-8 -*-

from vsg import parser


class label(parser.label):
    '''
    unique_id = next_statement : label
    '''

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    '''
    unique_id = next_statement : label_colon
    '''

    def __init__(self):
        super().__init__()


class next_keyword(parser.keyword):
    '''
    unique_id = next_statement : next_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class loop_label(parser.label):
    '''
    unique_id = next_statement : loop_label
    '''

    def __init__(self, sString):
        super().__init__(sString)


class when_keyword(parser.keyword):
    '''
    unique_id = next_statement : when_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    '''
    unique_id = next_statement : semicolon
    '''

    def __init__(self, sString=';'):
        super().__init__()
