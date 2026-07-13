%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <string>

enum TokenTypes {
    TK_EOF = 0,
    TK_FN, TK_LET, TK_MUT, TK_IF, TK_ELSE, TK_RETURN, TK_TRUE, TK_FALSE,
    TK_I32, TK_F32, TK_BOOL,
    TK_ASSIGN, TK_PLUS, TK_MINUS, TK_MUL, TK_DIV,
    TK_EQ, TK_NE, TK_LT, TK_GT,
    TK_LBRACE, TK_RBRACE, TK_LPAREN, TK_RPAREN, TK_COLON, TK_ARROW, TK_SEMI, TK_COMMA,
    TK_IDENT, TK_LIT_INT, TK_LIT_FLOAT,
    TK_ERROR
};

int line_num = 1;
int col_num = 1;
int token_line = 1;
int token_col = 1;

void update_location(const char* text) {
    for (int i = 0; text[i] != '\0'; ++i) {
        if (text[i] == '\n') {
            line_num++;
            col_num = 1;
        } else if (text[i] != '\r') {
            col_num++;
        }
    }
}
%}

%option noyywrap

%%

"//".*              { token_line = line_num; token_col = col_num; update_location(yytext); }
[ \t\r]+            { token_line = line_num; token_col = col_num; update_location(yytext); }
\n                  { line_num++; col_num = 1; }

"fn"                { token_line = line_num; token_col = col_num; update_location(yytext); return TK_FN; }
"let"               { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LET; }
"mut"               { token_line = line_num; token_col = col_num; update_location(yytext); return TK_MUT; }
"if"                { token_line = line_num; token_col = col_num; update_location(yytext); return TK_IF; }
"else"              { token_line = line_num; token_col = col_num; update_location(yytext); return TK_ELSE; }
"return"            { token_line = line_num; token_col = col_num; update_location(yytext); return TK_RETURN; }
"true"              { token_line = line_num; token_col = col_num; update_location(yytext); return TK_TRUE; }
"false"             { token_line = line_num; token_col = col_num; update_location(yytext); return TK_FALSE; }

"i32"               { token_line = line_num; token_col = col_num; update_location(yytext); return TK_I32; }
"f32"               { token_line = line_num; token_col = col_num; update_location(yytext); return TK_F32; }
"bool"              { token_line = line_num; token_col = col_num; update_location(yytext); return TK_BOOL; }

"->"                { token_line = line_num; token_col = col_num; update_location(yytext); return TK_ARROW; }
"=="                { token_line = line_num; token_col = col_num; update_location(yytext); return TK_EQ; }
"!="                { token_line = line_num; token_col = col_num; update_location(yytext); return TK_NE; }
"<"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LT; }
">"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_GT; }
"="                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_ASSIGN; }
"+"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_PLUS; }
"-"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_MINUS; }
"*"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_MUL; }
"/"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_DIV; }

"{"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LBRACE; }
"}"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_RBRACE; }
"("                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LPAREN; }
")"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_RPAREN; }
":"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_COLON; }
";"                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_SEMI; }
","                 { token_line = line_num; token_col = col_num; update_location(yytext); return TK_COMMA; }

[a-zA-Z_][a-zA-Z0-9_]*  { token_line = line_num; token_col = col_num; update_location(yytext); return TK_IDENT; }
[0-9]+\.[0-9]+          { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LIT_FLOAT; }
[0-9]+                  { token_line = line_num; token_col = col_num; update_location(yytext); return TK_LIT_INT; }

. {
    token_line = line_num;
    token_col = col_num;
    update_location(yytext);
    std::cerr << "ERROR LEXICO: caracter invalido '" << yytext
              << "' en la linea " << token_line << ", columna " << token_col << std::endl;
    return TK_ERROR;
}

%%

std::string token_to_string(int token) {
    switch (token) {
        case TK_FN: return "TK_FN";
        case TK_LET: return "TK_LET";
        case TK_MUT: return "TK_MUT";
        case TK_IF: return "TK_IF";
        case TK_ELSE: return "TK_ELSE";
        case TK_RETURN: return "TK_RETURN";
        case TK_TRUE: return "TK_TRUE";
        case TK_FALSE: return "TK_FALSE";
        case TK_I32: return "TK_I32";
        case TK_F32: return "TK_F32";
        case TK_BOOL: return "TK_BOOL";
        case TK_ASSIGN: return "TK_ASSIGN";
        case TK_PLUS: return "TK_PLUS";
        case TK_MINUS: return "TK_MINUS";
        case TK_MUL: return "TK_MUL";
        case TK_DIV: return "TK_DIV";
        case TK_EQ: return "TK_EQ";
        case TK_NE: return "TK_NE";
        case TK_LT: return "TK_LT";
        case TK_GT: return "TK_GT";
        case TK_LBRACE: return "TK_LBRACE";
        case TK_RBRACE: return "TK_RBRACE";
        case TK_LPAREN: return "TK_LPAREN";
        case TK_RPAREN: return "TK_RPAREN";
        case TK_COLON: return "TK_COLON";
        case TK_ARROW: return "TK_ARROW";
        case TK_SEMI: return "TK_SEMI";
        case TK_COMMA: return "TK_COMMA";
        case TK_IDENT: return "TK_IDENT";
        case TK_LIT_INT: return "TK_LIT_INT";
        case TK_LIT_FLOAT: return "TK_LIT_FLOAT";
        default: return "TK_ERROR";
    }
}

int main(int argc, char** argv) {
    if (argc > 1) {
        FILE* file = fopen(argv[1], "r");
        if (!file) {
            std::cerr << "Error al abrir el archivo fuente de Rust." << std::endl;
            return 1;
        }
        yyin = file;
    } else {
        yyin = stdin;
    }

    std::cout << std::left << std::setw(20) << "TOKEN"
              << std::setw(25) << "LEXEMA"
              << std::setw(10) << "LINEA"
              << "COLUMNA" << std::endl;
    std::cout << std::string(65, '-') << std::endl;

    int token;
    while ((token = yylex()) != TK_EOF) {
        if (token == TK_ERROR) {
            continue;
        }

        std::cout << std::left << std::setw(20) << token_to_string(token)
                  << std::setw(25) << yytext
                  << std::setw(10) << token_line
                  << token_col << std::endl;
    }

    return 0;
}