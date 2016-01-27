echo off

call env\Scripts\python.exe manage.py makemigrations
call env\Scripts\python.exe manage.py migrate

pause