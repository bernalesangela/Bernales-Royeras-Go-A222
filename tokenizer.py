
class TokenType:
    Delimiter = "Delimiter"  
    LineBreak = "Line Break" 
    Identifier = "Identifier"  
    Punctuator = "Punctuator" 
    Numeric = "Numeric"  
    Whitespace = "Whitespace"  



class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{{ type: '{self.type}'\t, value: '{self.value}' }}"


def tokenize(input_string):
    tokens = []
    i = 0

    while i < len(input_string):
        ch = input_string[i]

        if ch == ':': 
            print(ch, end='') 
            delimiter = ch
            i += 1
            tokens.append(Token(TokenType.Delimiter, delimiter))

        elif ch == '\n': 
            print(ch, end='') 
            lineBreak = "\\n"
            tokens.append(Token(TokenType.LineBreak, lineBreak))
            i += 1

        elif ch.isalpha():  
            identifier = ""
            while i < len(input_string) and (input_string[i].isalpha() or input_string[i] == '_'):
                print(input_string[i], end='')
                identifier += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Identifier, identifier))

        elif ch.isdigit():
            numeric = ""
            while i < len(input_string) and (input_string[i].isdigit() or input_string[i] == '.'):
                print(input_string[i], end='')
                numeric += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Numeric, numeric))

        elif ch in '!@#%^&*()-_=+[{]}\\|;:\'",<.>/?':  
            print(ch, end='')
            punctuator = ch
            tokens.append(Token(TokenType.Punctuator, punctuator))
            i += 1

        elif ch == ' ': 
            whitespace = ""
            while i < len(input_string) and input_string[i] == ' ':
                print(input_string[i], end='')
                whitespace += input_string[i]
                i += 1
            tokens.append(Token(TokenType.Whitespace, whitespace))

        else:
            i += 1

    return tokens


def main():
    # Predefined sample text options
    sampletext1 = "this:is a:sample text:"
    sampletext2 = "another:sample;text,;with punctuation:"
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

        print("\n")


if __name__ == "__main__":
    main()
