# Join a class
import cgi, os, string, sys
normal_sys = sys.path
sys.path.append(os.path.abspath(os.pardir) + "\\src\\")

from back_end.database import database
sys.path = normal_sys
db = database("CYBERFITNESS", "1")
form = cgi.FieldStorage()

username = None
password = None
with open('current_user.txt', 'r') as fd:
    username, password = fd.read().split('\n')

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <input type="submit" value="Continue"></input>
</form>
</div>
"""

print("Content-type:text/html")
print("<html><body>")
user_data = db.db_query(username, password)
if user_data == -1:
    print("<text>Invalid credentials</text>")
    print(continue_string.format("gym_welcome.py"))
else:
    print("""
        <form action="/cgi-bin/handle_class.py" method="post">
            <select name="class_name">
                <OPTION Value="kickboxing" selected>Kickboxing</OPTION>
                <OPTION Value="zumba">Zumba</OPTION>
                <OPTION Value="hit">H.I.T</OPTION>
                <OPTION Value="judo">Judo</OPTION>
                <OPTION Value="dancing">Dancing</OPTION>
                <OPTION Value="yoga">Yoga</OPTION>
            </select>
        <input type="submit" value="Submit"></input>
        </form>
        """)

print("</body></html>")