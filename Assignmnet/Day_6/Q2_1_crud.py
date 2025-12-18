import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri",
    use_pure = True
)

# form a query to be executed
sensor_id = int(input("Enter sensor id : "))
moisture_level = int(input("Enter moisture level : "))
datetime = input("Enter data and time : ")

query = f"insert into feild_information values({sensor_id}, {moisture_level}, '{datetime}')"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()