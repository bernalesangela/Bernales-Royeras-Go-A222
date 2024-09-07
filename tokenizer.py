class TokenType:
    Delimiter = "Delimiter"
    LineBreak = "Line Break"  
    Identifier = "Identifier"  
    Punctuator = "Punctuation" 
    Numeric = "Numeric"  
    Whitespace = "Whitespace" 


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token: '{self.value}' \t\t Type: '{self.type}'"



def tokenize(input_string):
    tokens = []
    i = 0

    while i < len(input_string):
        ch = input_string[i]

        if ch == ':':  
            delimiter = ch
            i += 1
            tokens.append(Token(TokenType.Delimiter, delimiter))

        elif ch == '\n': 
            lineBreak = "\\n"
            tokens.append(Token(TokenType.LineBreak, lineBreak))
            i += 1

        elif ch.isalpha(): 
            identifier = ""
            while i < len(input_string) and (input_string[i].isalpha() or input_string[i] == '_'):
                identifier += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Identifier, identifier))

        elif ch.isdigit():  
            numeric = ""
            while i < len(input_string) and (input_string[i].isdigit() or input_string[i] == '.'):
                numeric += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Numeric, numeric))

        elif ch in '!@#%^&*()-_=+[{]}\\|;:\'",<.>/?':  
            punctuator = ""
            while i < len(input_string) and input_string[i] in '!@#%^&*()-_=+[{]}\\|;:\'",<.>/?':
                punctuator += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Punctuator, punctuator))

        elif ch == ' ':  
            whitespace = ""
            while i < len(input_string) and input_string[i] == ' ':
                whitespace += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Whitespace, whitespace))

        else:
            i += 1

    return tokens

def granular_breakdown(tokens):
    print("\n===============================================")
    print("\nPhase 2 Output (Granular Breakdown):")
    for token in tokens:
        chars = ', '.join([f"'{char}'" for char in token.value])
        print(f'Token: "{token.value}" --> {chars}')


def main():
    sampletext1 = "this:is a:sample text:"
    sampletext2 = "Hello, world! Version 2.0 is here on 2024-08-27."
    sampletext3 = "delimiter:_:test\n:New line here;"
    sampletext4 = "123456:numbers:and:some:words:"
    sampletext5 = "Punctuations:!@#$:^&*():"

    sample_texts = [sampletext1, sampletext2, sampletext3, sampletext4, sampletext5]

    for idx, input_data in enumerate(sample_texts, start=1):
        print(f"\nSample Text {idx}:\n")
        print(input_data)
        print("\nTokens:")

        tokens = tokenize(input_data)

        for token in tokens:
            print(token)

        granular_breakdown(tokens)

        print("\n")


if __name__ == "__main__":
    main()
