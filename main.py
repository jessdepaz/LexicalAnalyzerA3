import re

# Define token types
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(int|bool|float|char|if|else|while|return|true|false)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('INTEGER', r'\b\d+\b'),
    ('FLOAT', r'\b\d+\.\d+\b'),
    ('CHAR', r"'[^']'"),
    ('BOOLEAN', r'\b(true|false)\b'),
    ('OPERATOR', r'==|!=|<=|>=|[+\-*/%<>&|!=]'),
    ('DELIMITER', r'[;(),{}\[\]]'),
    ('STRING', r'".*?"'),
    ('WHITESPACE', r'\s+'),
    ('COMMENT', r'//.*'),
    ('UNKNOWN', r'.')
]

token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)

def lexer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'WHITESPACE' or kind == 'COMMENT':
            continue  # Ignore whitespace and comments
        tokens.append((kind, value))
    return tokens

# Sample Clite input
sample_code = """
int main() {
    int x = 10;
    float y = 5.5;
    char c = 'A';
    bool flag = true;
    if (x > y && flag) {
        return x;
    } else {
        return y;
    }
    while (x >= 0) {
        x = x - 1;
    }
}
"""

# Run lexer
tokens = lexer(sample_code)

# Print tokens
for token in tokens:
    print(token)
