@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib

echo Creating help file header...

echo ^<head^> > .\release\log11087.html
echo ^<link rel="stylesheet" href="style.css"^> >> .\release\log11087.html
echo ^<title^>Logik - JSON-Parser (11087)^</title^> >> .\release\log11087.html
echo ^<style^> >> .\release\log11087.html
echo body { background: none; } >> .\release\log11087.html
echo ^</style^> >> .\release\log11087.html
echo ^<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"^> >> .\release\log11087.html
echo ^</head^> >> .\release\log11087.html


echo Generating html...
type .\README.md | C:\Python27\python -m markdown -x tables >> .\release\log11087.html

echo Generating py file...
cd ..\..
C:\Python27\python generator.pyc "11087_JSON-Parser" UTF-8

echo Copying...
xcopy .\projects\11087_JSON-Parser\src .\projects\11087_JSON-Parser\release /exclude:.\projects\11087_JSON-Parser\src\exclude.txt

@echo Fertig.

@pause
