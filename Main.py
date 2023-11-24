import os, json, pyodbc


try:
    print("[READING] Accessing file...")
    # Read dile
    JsonData = open(r"C:\Users\pkrammekwa\Documents\Python\data.json",'r', encoding='utf-8').read()
    JsonObj = json.loads(JsonData)
    # validate before insertion
    def validateString(val):
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val
            
    print("[CONNECTING] Establishing connection to DB...")
    # connect to the DB
    connectionString = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(LocalDB)\\MSSQLLocalDB;DATABASE=usersDB;Trusted_Connection=yes;')

    # Declare and Instantiate cursor to manage context of fetch operation
    cursor = connectionString.cursor()

    print("[TABLE] Creating table...")
    # Create table
    cursor.execute("CREATE TABLE users (name varchar(100),surname varchar(100),email varchar(50))")


    print("[PROCESSING] Inserting data...")
    # Loop through the entire file,validate and then insert into the db
    for i, item in enumerate(JsonObj):
        name = validateString(item.get("name",None))
        surname = validateString(item.get("surname",None))
        email = validateString(item.get("email",None))
        cursor.execute("INSERT INTO dbo.users([name],[surname],[email]) VALUES (?,?,?)", (name,surname,email))

    # Commit the changes to finish transaction
    connectionString.commit()

    # Close connection
    connectionString.close()

    print("[COMPLETED] Success!")

    # Delete file
    os.remove(r"C:\Users\pkrammekwa\Documents\Python\data.json")
  
except Exception as e:
  print("An exception occurred: ",e) 

