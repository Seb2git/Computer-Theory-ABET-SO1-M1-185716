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
                    token_type = keywords.get(value, "IDENTIFIER")
                if token_type == "SPACE":
                    token_type = tokens.append((token_type, value))

rules = [
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUM", r"[0-9]+"),
    ("LESS_EQ", r"<="),
    ("ASSIGN", r"="),
    ("PLUS", r"\+"),
    ("SEMICOL", r""),
    ("SPACE", r"\s+"),
    ()
    ]

keywords = {
    "int"  :"INT",
    "bool" :"BOOL",
    "while":"WHILE",
    "if"   :"IF",
    "else" :"ELSE",
    "print":"PRINT",
    "true" :"TRUE",
    "false":"FALSE"
    }

