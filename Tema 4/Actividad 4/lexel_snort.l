%{
#include <stdio.h>
#define TK_ACTION 1
#define TK_PROTOCOL 2
#define TK_VAR 3
#define TK_PORT 4
#define TK_DIRECTION 5
#define TK_OPTION_KEY 6
#define TK_OPTION_VALUE 7
%}

%option noyywrap

%%

"alert"|"log"|"drop"         { printf("TOKEN: TK_ACTION, Lexema: %s\n", yytext); return TK_ACTION; }
"tcp"|"udp"|"icmp"|"any"     { printf("TOKEN: TK_PROTOCOL, Lexema: %s\n", yytext); return TK_PROTOCOL; }
"->"                         { printf("TOKEN: TK_DIRECTION, Lexema: %s\n", yytext); return TK_DIRECTION; }
\$[a-zA-Z_][a-zA-Z0-9_]*     { printf("TOKEN: TK_VAR, Lexema: %s\n", yytext); return TK_VAR; }
"any"|[0-9]+                 { printf("TOKEN: TK_PORT, Lexema: %s\n", yytext); return TK_PORT; }
"msg"|"sid"|"content"        { printf("TOKEN: TK_OPTION_KEY, Lexema: %s\n", yytext); return TK_OPTION_KEY; }
\"[^\"]*\"                   { printf("TOKEN: TK_OPTION_VALUE, Lexema: %s\n", yytext); return TK_OPTION_VALUE; }

[ \t\n\r]+                   { /* Ignorar espacios en blanco, tabulaciones y nuevas líneas */ }
#.*                          { /* Ignorar comentarios de una sola línea */ }
.                            { printf("ERROR LÉXICO: Carácter no reconocido '%s'\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error al abrir el archivo de firmas");
            return 1;
        }
        yyin = file;
    }
    while(yylex());
    return 0;
}
