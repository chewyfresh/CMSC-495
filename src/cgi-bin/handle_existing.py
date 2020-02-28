import cgi

form = cgi.FieldStorage()

print("Content-type:text/html")

username = form.getvalue("username")
password = form.getvalue("password")

continue_string = """
<div>
<form action="/cgi-bin/{}" method="post">
    <input type="submit" value="Continue"></input>
</form>
</div>
"""
print("<html><body>")
# Need to instantiate database first before this can run
if DATABASE.db_query(username, password) == -1:
    print("<text>No user by those credentials</text>")
    print(continue_string.format("existing_user.py"))
    # Continue button sends user to "index.html"
else:
    print(f"<text>Welcome back {username}</text>!")
    print(continue_string.format("gym_welcome.py"))
    # Continue button sends user to "Gym interface"

print("</body></html>")