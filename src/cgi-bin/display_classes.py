# Display all classes user is in
import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")

from back_end.database import database
sys.path = normal_sys
db = database("CYBERFITNESS", "1")

username = None
password = None
with open('current_user.txt', 'r') as fd:
    username, password = fd.read().split('\n')
    
user_data = db.db_query(username, password)

classes = []

for x in user_data.keys():
    if x not in ('name', 'password'):
        classes.append(x)

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <input type="submit" value="Continue"></input>
</form>
</div>
"""
print("Content-type:text/html\n")
print("<html><body>")
if len(classes) == 0:
    print("<text>NO CLASSES TO DISPLAY</text>")
else:
    for cls in classes:
        print("<li>{}</li>\n".format(cls))

print(continue_string.format("gym_welcome.py"))
    
print("</body></html>")