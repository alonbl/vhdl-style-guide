# -*- coding: utf-8 -*-

from vsg import parser


class port_keyword(parser.keyword):
    '''
    unique_id = port_map_aspect : port_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class map_keyword(parser.keyword):
    '''
    unique_id = port_map_aspect : map_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = port_map_aspect : open_parenthesis
    '''

    def __init__(self, sString=None):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = port_map_aspect : close_parenthesis
    '''

    def __init__(self, sString=None):
        super().__init__()
