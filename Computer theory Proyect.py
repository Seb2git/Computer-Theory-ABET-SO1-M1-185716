import regex

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

rules = [
    ("ID"     , r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUM"    , r"[0-9]+"),
    
    ("ASSIGN" , r"="),
    
    ("COMPAR" , r"=="),
    ("COMPAR" , r"<"),
    ("COMPAR" , r">"),
    ("COMPAR" , r"<="),
    ("COMPAR" , r">="),
    ("COMPAR" , r"!="),
    
    ("EQUAT"  , r"\+"),
    ("EQUAT"  , r"\-"),
    ("EQUAT"  , r"\*"),
    ("EQUAT"  , r"/"),
    
    ("LOGIC"  , r"\&\&"),
    ("LOGIC"  , r"\|\|"),
    ("LOGIC"  , r"!"),
    
    ("OP_PAR" , r"\("),
    ("CL_PAR" , r"\)"),
    ("OP_BRAC", r"{"),
    ("CL_BRAC", r"}"),
    
    ("COMMA"  , r"\,"),
    ("DOT"    , r"\."),
    ("SEMICOL", r"\;"),
    ("SPACE"  , r"\s")]

def tokenize(text):
    tokens   = []
    position = 0
    
    while position < len(text):
        for token_type, pattern in rules:
            match = regex.match(pattern, text[position:])
            
            if match:
                value = match.group()
                
                if token_type == "SPACE":
                    position = position + 1
                else:
                    if token_type == "ID":
                        token_type = keywords.get(value, "ID")
                    elif token_type == "NUM":
                        token_type = keywords.get(value, "NUM")
                
                    elif token_type == "ASSIGN":
                        token_type = keywords.get(value, "ASSIGN")
                
                    elif token_type == "COMPAR":
                        token_type = keywords.get(value, "COMPAR")
                    
                    elif token_type == "EQUAT":
                        token_type = keywords.get(value, "EQUAT")
                    
                    elif token_type == "LOGIC":
                        token_type = keywords.get(value, "LOGIC")
                    
                    elif token_type == "OP_PAR":
                        token_type = keywords.get(value, "OP_PAR")
                    elif token_type == "CL_PAR":
                        token_type = keywords.get(value, "CL_PAR")
                    elif token_type == "OP_BRAC":
                        token_type = keywords.get(value, "OP_BRAC")
                    elif token_type == "CL_BRAC":
                        token_type = keywords.get(value, "CL_BRAC")
                    
                    elif token_type == "COMMA":
                        token_type = keywords.get(value, "COMMA")
                    elif token_type == "DOT":
                        token_type = keywords.get(value, "DOT")
                    elif token_type == "SEMICOL":
                        token_type = keywords.get(value, "SEMICOL")
                    else:
                        print("error en "+str(position))
                        position = position + 1
                        break
                    tokens.append((token_type, value))
                    position = position + len(value)
                    break
                    
    return(tokens)

def parse_assignment(tokens):
    expected = [
        ["ID","ASSIGN","NUM","SEMICOL"],
        []
        
        ]

    actual = [token[0] for token in tokens]
    for expect in expected:
        if actual != expect:
            raise SyntaxError("Invalid assignment")
        return {"node":"Assignment",
                "target":tokens[0][1],
                "value":{
                    "node":"IntegerLiteral",
                    "value":int(tokens[2][1])}}


testtext = "x =13;" #borrar cuando se prepare el parse_assignment para el segundo test
"""
int x,y;
x = 13;
a = 12;
if (true && x > a || !false){
    print(a)
    }}
"""
testToknz = (tokenize(testtext))
print(testToknz)
print(parse_assignment(testToknz))

