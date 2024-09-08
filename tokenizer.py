import customtkinter as ctk
from PIL import Image
import emoji

# CONSTANTS
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

# Define a token class
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token: '{self.value}' \t\t Type: '{self.type}'"

# Categorize tokens
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

# Tokenize the input string
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

            tokens.append(Token(TokenType.Delimiter, ch))
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

# Granular breakdown function
def granular_breakdown(tokens):
    breakdown = []
    for token in tokens:
        chars = ', '.join([f"'{char}'" for char in token.value])
        breakdown.append(f'Token: "{token.value}" --> {chars}')
    return breakdown


class TokenizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Tokenizer")
        self.root.geometry("600x600")

        # Themes
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(root, corner_radius=0)
        self.scrollable_frame.pack(expand=True, fill="both")

        # Frame for Scrollable frame
        self.content_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=0)
        self.content_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Title of the Program
        self.string_tokenizer_label = ctk.CTkLabel(self.content_frame, text=emoji.emojize("String Tokenizer"), font=("Helvetica", 18), fg_color=None)
        self.string_tokenizer_label.pack(pady=15, anchor="center", expand=True)

        # Input
        self.input_label = ctk.CTkLabel(self.content_frame, text="Input Text:", font=("Helvetica", 12))
        self.input_label.pack(pady=10)

        self.input_text = ctk.CTkTextbox(self.content_frame, wrap="word", width=400, height=100)
        self.input_text.pack(pady=10)

        # Button & Image
        self.image = ctk.CTkImage(light_image=Image.open("token.png"), dark_image=Image.open("white_token.png"), size=(25, 25))
        self.tokenize_button = ctk.CTkButton(self.content_frame, text="Tokenize", image=self.image, compound="left", command=self.tokenize_text)
        self.tokenize_button.pack(pady=10)

        # Output
        self.tokens_label = ctk.CTkLabel(self.content_frame, text="Tokens:", font=("Helvetica", 12))
        self.tokens_label.pack(pady=10)

        self.tokens_output = ctk.CTkTextbox(self.content_frame, wrap="word", width=400, height=200)
        self.tokens_output.pack(pady=10)
        self.tokens_output.configure(state="disabled")

        # Granular Breakdown
        self.breakdown_label = ctk.CTkLabel(self.content_frame, text="Granular Breakdown:", font=("Helvetica", 12))
        self.breakdown_label.pack(pady=10)

        self.breakdown_output = ctk.CTkTextbox(self.content_frame, wrap="word", width=400, height=200)
        self.breakdown_output.pack(pady=10)
        self.breakdown_output.configure(state="disabled")

        # Made With Love
        self.made_with_love = ctk.CTkLabel(self.content_frame, text=emoji.emojize("Made by: Bernales | Royeras | Go :red_heart:"), font=("Helvetica", 8), fg_color=None)
        self.made_with_love.pack(pady=7, anchor="center", expand=True)


    def tokenize_text(self):
        # Clear previous results
        self.tokens_output.configure(state="normal")
        self.breakdown_output.configure(state="normal")
        self.tokens_output.delete('1.0', 'end')
        self.breakdown_output.delete('1.0', 'end')

        # Get input from text box
        input_string = self.input_text.get("1.0", 'end').strip()

        # Tokenize the input
        tokens = tokenize(input_string)

        # Display tokens
        for token in tokens:
            self.tokens_output.insert('end', f"{token}\n")

        # Display granular breakdown
        breakdown = granular_breakdown(tokens)
        for line in breakdown:
            self.breakdown_output.insert('end', f"{line}\n")

        # Disable text boxes to prevent editing
        self.tokens_output.configure(state="disabled")
        self.breakdown_output.configure(state="disabled")


root = ctk.CTk()
app = TokenizerApp(root)


root.mainloop()
