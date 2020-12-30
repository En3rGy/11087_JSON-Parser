@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib
@echo on

xcopy .\src\*.* .\release 

cd ..\..
C:\Python27\python generator.pyc "11087_JSON-Parser" UTF-8
@REM C:\Python27\python generator.pyc "EasterDate" UTF-8

@echo Fertig.

@pause