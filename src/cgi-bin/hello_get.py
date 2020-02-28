import cgi, cgitb

form = cgi.FieldStorage()
print("Content-type:text/html")
print()
cgitb.enable()
print("HELLO WORLD")