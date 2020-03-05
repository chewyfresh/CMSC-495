# Set goals for user
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
    <div>
        <label for="weight">Enter your desired weight:</label>
        <label for="cals">Enter your desired total calorie loss:</label>
        <label for="classes_taken">Enter total classes desired:</label>
        <form action="/cgi-bin/handle_goals.py" method="post">
            <input type="text" name="weight"></input>
            <input type="text" name="cals"></input>
            <input type="text" name="classes_taken"></input>
            <input type="submit" value="Submit"></input>
    </form>
    </div>
    """)
print("</body></html>")