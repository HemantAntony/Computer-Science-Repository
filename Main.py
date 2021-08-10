import Admin
import Client
import mysql.connector as connector

mydb = connector.connect(host = "localhost", username = "root", password = "root")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS AirportManagement")
mycursor.execute("USE AirportManagement")


print("Hello there! Which mode do you want?")
print("1. Client Mode (c)")
print("2. Admin Mode (a)")
answer = input()
if answer == 'c':
  Client.displayFunctions()
elif answer == 'a':
  Admin.displayFunctions()
else:
  print("Invalid Input")