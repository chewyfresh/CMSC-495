import cgi

print("Content-type:text/html")

classes = database.get_classes()
print("<html><head>")
print("<title>Removing a class</title>"
print("<body>")
for cls in classes:
    print("<li><a href=", "delete_class.py?class_id=", cls.number, ">", cls.name, "</a><li>", sep='')
    print("<h3></h3>")
print("</body></html>")