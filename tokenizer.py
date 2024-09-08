class TokenType:
    Alphanumeric = "Alpha Numeric"
    Word = "Word"
    Number = "Number"
    Delimiter = "Delimiter"
    LineBreak = "Line Break"
    Punctuation = "Punctuation"
    SpecialChar = "Special Character"
    Whitespace = "Whitespace"
    Mixed = "Mixed"  

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token: '{self.value}' \t\t Type: '{self.type}'"

def categorize(token):
    has_alpha = any(char.isalpha() for char in token)
    has_digit = any(char.isdigit() for char in token)
    has_symbol = any(char in '!@#%^&$*()-_=+[{]}\\|;:\'",<.>/? ' for char in token)

    if has_alpha and has_digit and not has_symbol:
        return TokenType.Alphanumeric
    elif has_symbol:
        if has_alpha or has_digit:
            return TokenType.Mixed
        elif all(char in ' ' for char in token):
            return TokenType.Whitespace
        elif all(char in '.,!?()"\';—-' for char in token):
            return TokenType.Punctuation
        else:
            return TokenType.SpecialChar
    elif has_alpha:
        return TokenType.Word
    elif has_digit:
        return TokenType.Number
    else:
        return TokenType.Alphanumeric  



def tokenize(inputString):
    tokens = []
    newArr = []

    i = 0
    while i < len(inputString):
        ch = inputString[i]

        if ch == ':':
            if newArr:
                tokenVal = ''.join(newArr)
                token_type = categorize(tokenVal)
                tokens.append(Token(token_type, tokenVal))
                newArr.clear()
            i += 1

        elif ch == '\n':
            if newArr:
                tokenVal = ''.join(newArr)
                token_type = categorize(tokenVal)
                tokens.append(Token(token_type, tokenVal))
                newArr.clear()

            tokens.append(Token(TokenType.LineBreak, "\\n"))
            i += 1

        else:
            newArr.append(ch)
            i += 1

    if newArr:
        tokenVal = ''.join(newArr)
        token_type = categorize(tokenVal)
        tokens.append(Token(token_type, tokenVal))

    return tokens

def granularBreakdown(tokens):
    print("\n===============================================")
    print("\nGranular Breakdown:")
    if tokens:

        for token in tokens:
            chars = ', '.join([f"'{char}'" for char in token.value])
            print(f'Token: "{token.value}" --> {chars}')
    else:
        
        print("No tokens generated.")

def main():
    sampleText1 = "123angela:bernales789"
    sampleText2 = "Hello, world! Version 2.0 is here on 2024-08-27."
    sampleText3 = "-2:"
    sampleText4 = ""
    sampleText5 = "Hello world!: blah:2:15@:\n:\nhello:\n:"

    sampleTexts = [sampleText1, sampleText2, sampleText3, sampleText4, sampleText5]

    for idx, sampleInput in enumerate(sampleTexts, start=1):
        print(f"\nSample Text {idx}:\n")
        print(sampleInput)
        print("\nTokens:")

        tokens = tokenize(sampleInput)

        if tokens:
            for token in tokens:
                print(token)
        else:
            print("No tokens generated.")

        granularBreakdown(tokens)

        print("\n")


if __name__ == "__main__":
    main()