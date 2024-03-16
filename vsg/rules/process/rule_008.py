# -*- coding: utf-8 -*-

from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_keyword)


class rule_008(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END process proc_a;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    '''

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append('case::keyword')
