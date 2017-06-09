f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<h1>Hello World</h1> 
<h2>Hello</h2>
</body>
</html>"""

f.write(message)
f.close()