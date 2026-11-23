import regex

def tokenize(text):
    tokens   = []
    position = 0
    
    while position < len(text):
        for token_type, pattern in rules:
            match = regex.match(pattern, text[position:])
            
            if match:
                value = match.group()
                
                if token_type == "ID":
                    token_type = keywords.get(value, "ID")
                if token_type == "SPACE":
                    token_type = tokens.append((token_type, value))

rules = [
    ("ID"     , r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUM"    , r"[0-9]+"),
    
    ("ASSIGN" , r"="),
    
    ("EQUAL"  , r"=="),
    ("LESS_TH", r"<"),
    ("MORE_TH", r">"),
    ("LESS_EQ", r"<="),
    ("MORE_EQ", r">="),
    ("UNEQUAL", r"!="),
    
    ("PLUS"   , r"\+"),
    ("MINUS"  , r"\-"),
    ("MULTI"  , r"\*"),
    ("DIV"    , r"/"),
    
    ("AND"    , r"\&\z&"),
    ("OR"     , r"\|\|"),
    ("NOT"    , r"!"),
    
    ("OP_PAR" , r"\("),
    ("CL_PAR" , r"\)"),
    ("OP_BRAC", r"{"),
    ("CL_BRAC", r"}"),
    
    ("COMMA"  , r"\,"),
    ("DOT"    , r"\."),
    ("SEMICOL", r"\;"),
    ("SPACE"  , r"\s")
    ]

keywords = {
    "int"  :"INT",
    "bool" :"BOOL",
    
    "true" :"TRUE",
    "false":"FALSE"
    
    "while":"WHILE",
    
    "if"   :"IF",
    "else" :"ELSE",
    
    "print":"PRINT",
    }

