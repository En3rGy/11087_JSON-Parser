[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
# 11087 JSON-Parser

## Beschreibung

Der Baustein liefert den Wert eines JSON Objekts oder die hinter dem Objekt liegende Json-Struktur. Außerdem bietet der Baustein folgende Funktionen:
- Baustein-Kaskaden über Text-Ausgang zu Json-Eingang, um verschachtelte Strukturen zu erreichen
- Umlaute / Sonderzeichen werden [XML-Encodiert](https://wiki.selfhtml.org/wiki/XML/Regeln/Zeichen) ausgegeben
- Bei einem Wert Array Index > -1: Ausgabe von Listeneinträgen

Beispiel für eine Bausteinkaskade, mit JSON-String = `{"1": "a", "2":[{"2.1": "b.1", "2.2": "b.2"}, {"2.3": "b.3"}]}`
1. Baustein mit Key = "2" liefert `[{"2.1": "b.1", "2.2": "b.2"}, {"2.3": "b.3"}]`
2. Baustein mit Idx = 0 liefert `{"2.1": "b.1", "2.2": "b.2"}`
3. Baustein mit Key = "2.2" liefert `"b.2"` 

## Eingänge

| Nr. | Name        | Initialisierung | Beschreibung                                                                                                                                   |
|-----|-------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | JSON-String |                 | Gültiger (!) JSON-String                                                                                                                       |
| 2   | Key         |                 | JSON Key, für den der Wert ausgegeben werden soll.<br>*Wird nur verwendet, wenn Array Index < 0!*                                              |
| 3   | Array Index | -1              | Index des Array Elements, welches ausgegeben werden soll. Das erste Element hat den Index 0<br>*Wenn >= 0 wird immer der Index verwendet und nie der Key!* |

## Ausgänge

| Nr. | Name           | Initialisierung | Beschreibung                                                                           |
|-----|----------------|-----------------|----------------------------------------------------------------------------------------|
| 1   | Value (str)    |                 | Angefragter Wert oder JSON-Struktur; XML enkodiert, falls UTF-8 Zeichen enthalten sind |
| 2   | Value (number) | 0               | Angefragter Wert als Zahl (float, int oder bool)                                       | 

## Sonstiges 

- Neuberechnung beim Start: Nein
- Baustein ist remanent: Nein

### Change Log

- v1.4
  - XML encoded output if UTF-8 characters would be part of the output
- v1.3
  - added unit tests
  - improved reliability / stability
  - improved documentation
- v1.2
  - Refactoring der unit tests
  - Verbesserung der unit tests
  - Wechsel der Doku zu markdown
  - fix https://github.com/En3rGy/11087_JSON-Parser/issues/1
- v1.1
  - Reduktion Log-Ausgaben
- v1.0
  - Release
- v0.14
  - Ausgaben / Informationen für Debug-Seite ergänzt.
- v0.13
  - Fehlerhaften Modul-Import korrigiert.
  -	Error-Meldungen auf Debug-Seite hinzugefügt.

### Open Issues / Known Bugs
- keine

### Support

Please use [GitHub issue feature](https://github.com/En3rGy/11087_JSON-Parser/issues) to report bugs or rise feature requests.
Questions can be addressed as new threads at the [knx-user-forum.de](https://knx-user-forum.de) also. There might be discussions and solutions already.


### Code

Der Python-Code des Bausteins befindet sich auf [github](https://github.com/En3rGy/11087_JSON-Parser).

### Lizenz

Copyright 2021 T. Paul

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
