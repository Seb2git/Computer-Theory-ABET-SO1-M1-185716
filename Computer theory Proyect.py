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
                if token_type == "NUM":
                    token_type = keywords.get(value, "NUM")
                
                if token_type == "ASSIGN":
                    token_type = keywords.get(value, "ASSIGN")
                
                if token_type == "EQUAL":
                    token_type = keywords.get(value, "COMPARISON")
                if token_type == "LESS_TH":
                    token_type = keywords.get(value, "COMPARISON")
                if token_type == "MORE_TH":
                    token_type = keywords.get(value, "COMPARISON")
                if token_type == "LESS_EQ":
                    token_type = keywords.get(value, "COMPARISON")
                if token_type == "MORE_EQ":
                    token_type = keywords.get(value, "COMPARISON")
                if token_type == "UNEQUAL":
                    token_type = keywords.get(value, "COMPARISON")
                    
                if token_type == "PLUS":
                    token_type = keywords.get(value, "EQUATION")
                if token_type == "MINUS":
                    token_type = keywords.get(value, "EQUATION")
                if token_type == "MULTI":
                    token_type = keywords.get(value, "EQUATION")
                if token_type == "DIV":
                    token_type = keywords.get(value, "EQUATION")
                    
                if token_type == "AND":
                    token_type = keywords.get(value, "LOGICAL")
                if token_type == "OR":
                    token_type = keywords.get(value, "LOGICAL")
                if token_type == "NOT":
                    token_type = keywords.get(value, "LOGICAL")
                    
                if token_type == "OP_PAR":
                    token_type = keywords.get(value, "OP_PAR")
                if token_type == "CL_PAR":
                    token_type = keywords.get(value, "CL_PAR")
                if token_type == "OP_BRAC":
                    token_type = keywords.get(value, "OP_BRAC")
                if token_type == "CL_BRAC":
                    token_type = keywords.get(value, "CL_BRAC")
                    
                    
                if token_type == "COMMA":
                    token_type = keywords.get(value, "COMMA")
                if token_type == "DOT":
                    token_type = keywords.get(value, "DOT")
                if token_type == "SEMICOL":
                    token_type = keywords.get(value, "SEMICOL")
                    
                if token_type != "SPACE":
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
    "false":"FALSE",
    
    "while":"WHILE",
    
    "if"   :"IF",
    "else" :"ELSE",
    
    "print":"PRINT",
    }

def parse_assignment(tokens):
    expected = ["ID","ASSIGN","NUM","SEMICOL"]

