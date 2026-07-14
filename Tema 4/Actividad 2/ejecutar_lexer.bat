@echo off
title Ejecucion Actividad 2 - Lexer Docker (Grupo Nabla)
color 0B

echo ================================================================
echo    ANALIZADOR LEXICO PARA DOCKERFILE - ACTIVIDAD 2 - GRUPO NABLA
echo ================================================================
echo.

echo [ PRUEBA 1: Sintaxis Basica Correcta ]
echo.
echo Ejecutando: python lexer_dockerfiles.py dockerfile_1.txt
echo -------------------------------------------------------
python lexer_dockerfiles.py dockerfile_1.txt
echo.
pause

cls
echo ================================================================
echo    ANALIZADOR LEXICO PARA DOCKERFILE - ACTIVIDAD 2 - GRUPO NABLA
echo ================================================================
echo.

echo [ PRUEBA 2: Filtrado de Comentarios ]
echo.
echo Ejecutando: python lexer_dockerfiles.py dockerfile_2.txt
echo -------------------------------------------------------
python lexer_dockerfiles.py dockerfile_2.txt
echo.
pause

cls
echo ================================================================
echo    ANALIZADOR LEXICO PARA DOCKERFILE - ACTIVIDAD 2 - GRUPO NABLA
echo ================================================================
echo.

echo [ PRUEBA 3: Inyeccion de Error Lexico '?' ]
echo.
echo Ejecutando: python lexer_dockerfiles.py dockerfile_3.txt
echo -------------------------------------------------------
python lexer_dockerfiles.py dockerfile_3.txt
echo.
echo =======================================================
echo               EJECUCION FINALIZADA
echo =======================================================
pause