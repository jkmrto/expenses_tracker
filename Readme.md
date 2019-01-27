# Expenses tracker

## Run clean docker mysql database
```
docker run --name mysql-gastos -e MYSQL_ROOT_PASSWORD=pwd -e MYSQL_DATABASE='expenses' -p 3306:3306 -d mysql:5.7.23
```

## Run clean docker metabase
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

## To generate virtual environment
```
bash venv_creation.sh
```
This will create a folder named "venv" where a python binary can be found with all the dependencies to run the project 

## Setting up google sheet acces:

Follow his full instructions on the Google Developers Console web site to create a service account Client ID JSON file. I will call the file gspread-test.json from now on.

After saving gspread-test.json you need to share your document with the given email in the client_email field of the file. Otherwise you’ll get a SpreadsheetNotFound exception when trying to open it.

http://alexsavio.github.io/gspread_oauth2client_intro.html


## COnnect to mysql ddbb in terminal
mysql -u user -D expenses -h 127.0.0.1 -p

## Roadmap

1. To generate topics script
```
venv/bin/python3 generate_topics.py
```

