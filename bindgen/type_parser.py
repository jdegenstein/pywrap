from pyparsing import Word, Literal, alphas, alphanums, Optional, MatchFirst

CONST = Literal("const")

# Expand to handle modern C++ smart pointers seamlessly
SMART_PTR_WRAPPER = MatchFirst([
    Literal("opencascade::handle<"),
    Literal("std::shared_ptr<"),
    Literal("std::unique_ptr<")
])

TYPE = Word(alphas + "_", alphanums + "_")
CLOSING = Literal(">")
PTR_REF = MatchFirst([Literal("&"), Literal("*")])

parser = (
    Optional(CONST)
    + Optional(SMART_PTR_WRAPPER)
    + TYPE.setResultsName("type")
    + Optional(CLOSING)
    + Optional(PTR_REF)
)

def parse_type(t):
    return parser.parseString(t).type
