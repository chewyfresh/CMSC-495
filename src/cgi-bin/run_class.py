import cgi, os, string, sys

normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")
import FitnessClasses as fc
from back_end.database import database

sys.path = normal_sys
db = database("CYBERFITNESS", "1")

form = cgi.FieldStorage()

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
if len(classes) > 0:
    print("""
     <form action="/cgi-bin/handle_run.py" method="post">
     <select name="choice">""")
    for cls in classes:
        print("<OPTION Value={}>{}</OPTION>".format(cls, cls))
    print("""
        </select><input type="submit" value="Submit"></input></form>""")
else:
    print("<text>NO CLASSES TO RUN</text>")
    print(continue_string.format('gym_welcome.py'))
print("</body></html>")