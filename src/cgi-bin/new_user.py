import cgi
form = cgi.FieldStorage()

print("Content-type:text/html")
print("\n<html><head>")
print("<title>Creating a new user</title></head>")
print("""
<div>
    <text> Note: Password requires at least One capital letter, One digit, One special character, and eight characters minimum</text>
    <label for="username">Enter your username:</label>
    <label for="password">Enter your password:</label>
    <form action="/cgi-bin/handle_new.py" method="post">
        <input type="text" name="username"></input>
        <input type="password" name="password"></input>
        <input type="submit" value="Submit"></input>
</form>
</div>
""")
print("</html>")