ECHO OFF
python js2json.py
SET dt=%DATE:~10,4%_%DATE:~4,2%
DEL data/%dt%.json
python delete.py
PAUSE
