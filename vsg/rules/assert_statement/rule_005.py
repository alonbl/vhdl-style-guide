# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token_when_between_tokens_unless_token_is_found

lTokens = []
lTokens.append(token.assertion.severity_keyword)

oStart = token.assertion.keyword
oEnd = token.assertion_statement.semicolon
oStop = token.concurrent_assertion_statement.semicolon


class rule_005(split_line_at_token_when_between_tokens_unless_token_is_found):
    """
    This rule checks the **severity** keyword is on its own line for sequential assertion statements.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

         process begin

           assert WIDTH > 16 report "FIFO width is limited to 16 bits." severity FAILURE;

         end process;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

         process begin

           assert WIDTH > 16 report "FIFO width is limited to 16 bits."
             severity FAILURE;

         end process;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, oStop)
        self.solution = "Place **severity** keyword on its own line."
