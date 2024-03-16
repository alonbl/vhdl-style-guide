from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_004(token_case):
    """
    This rule checks the **begin** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    """

    def __init__(self):
        token_case.__init__(self, lTokens)
        self.groups.append("case::keyword")
