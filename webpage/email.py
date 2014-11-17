#!/usr/bin/python
import MySQLdb
import cgi, cgitb

form = cgi.FieldStorage()

email = form.getvalue('email')

# Avoid script injection escaping the user input
email = cgi.escape(email)

print email


db = MySQLdb.connect(host="mysql.example.com", port=3306, user="l", passwd="l", db="l")
cursor = db.cursor()

add_driver = ("INSERT INTO Users "
           "(UsersName, UsersEmail, UsersPlate) "
           "VALUES (%s, %s, %s)")

cursor.execute(add_driver, (name, email, plate))
db.commit()
cursor.close()
db.close()

print "Content-type: text/html\n\n"
print 
print """\
<html>
<body>
    <h2>Hello!</h2>
    <ul>
</body>
</html>
"""