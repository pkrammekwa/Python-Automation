# Python-Automation
The project aims to automate SQL table creation using Python by extracting data from an json file.

## Tools:
1. SQL Server Management Studio 19
2. VSCode
3. Microsoft ODBC Driver 17/18 for SQL Server
4. Microsoft SQL Server 2019 LocalDB
5. Python 3.12
6. Python packages: pyodbc

## Steps:
1. Assuming all the necessary tools and packages are installed.
2. Create a folder in documents named “Python” or whichever you prefer.
3. Place the “data.json” and “Main.py” in the Python folder.
4. Open the Main.py file using VSCode
5. Change location of the data.json
(C:\Users\pkrammekwa\Documents\Python\data.json) to where you stored the json file.
6. Install “Python v2023.20.0” extension
7. Run SQL Server Management Studio 19
8. Enter the following:
- Server name: (LocalDb)\MSSQLLocalDB
- Server Type: Database Engine
- Authentication: Windows Authention
10. Click connect
11. Right Click Databases and click New Database > Enter DB name (usersDB) >
Add
12. In VSCode, run the python script.
13. Go back to SSMS > expand usersDB > expand Tables, users table should be
visible.
14. Right click users table > Select top 1000 rows. New data should be now be present.
15. Done.