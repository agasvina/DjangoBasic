# SOME USEFUL COMMAND

python manage.py inspectdb --database=kaggle

curl -X POST -d "username=luca&password=agas1234" http://localhost:8000/api-token-auth/

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IiIsInVzZXJfaWQiOjEsImV4cCI6MTQ4Mjc5NDMzOCwidXNlcm5hbWUiOiJsdWNhIn0.qRX1WROM2G4w3gp7r4c-qoZqIZ90ws68R1pZbHBUXoY" http://localhost:8000/api/todo/


docker stop $(docker ps -a -q);docker rm $(docker ps -a -q)

docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Super@secret1234' -p 8888:1433  -d microsoft/mssql-server-linux
-v /Users/luca/djangoEngd/var/opt/mssql:/var/opt/mssql

tsql -S TS  -U sa -P Super@secret1234
[TS] 
    host = localhost
    port = 8888
    tds version = 8.0



https://github.com/lionheart/django-pyodbc/wiki/Mac-setup-to-connect-to-a-MS-SQL-Server


Some Useful query:
	http://localhost:8000/api/kaggle/summary/?form=d3&platform=PC&platform=PS3&platform=XOne&format=json
	http://localhost:8000/api/kaggle/total/?format=json