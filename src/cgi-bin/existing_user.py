import cgi
form = cgi.FieldStorage()

print("Content-type:text/html")
print()
print("""
</html><body>
<div>
    <label for="username">Enter your username:</label>
    <label for="password">Enter your password:</label>
    <form action="/cgi-bin/handle_existing.py" method="post">
        <input type="text" name="username"></input>
        <input type="password" name="password"></input>
        <input type="submit" value="Submit"></input>
</form>
</div>
</body></html>
""")