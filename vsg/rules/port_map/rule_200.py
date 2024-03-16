# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token as Rule

lTokens = []
lTokens.append(token.port_map_aspect.open_parenthesis)


class rule_200(Rule):
    '''
    This rule checks for a blank line below the open parenthesis in a port map.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

      port map (

        WR_EN => w_wr_en,
        RD_EN => w_rd_en,
        OVERFLOW => w_overflow
      );

    **Fix**

    .. code-block:: vhdl

      port map (
        WR_EN => w_wr_en,
        RD_EN => w_rd_en,
        OVERFLOW => w_overflow
      );
    '''

    def __init__(self):
        super().__init__(lTokens)
        self.style = 'no_blank_line'
