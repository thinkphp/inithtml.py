import sys

script_tag = ""

filename = ""

name = len(sys.argv) > 1 and sys.argv[1] or None

x = len(sys.argv) > 2

if x:
 filename = sys.argv[2]
else:
 filename = 'noname.html'

if name:
   script_tag = '<script type="text/javascript" src="%s"></script><script type="text/javascript">(function(){ alert("Ready to Go") })();</script>' % name

template = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>Title</title>
<style type="text/css">
</style>
%s
</head>
<body>
</body>
</html>
""" % script_tag

#open the handler file
f = open(filename,'w')

#write to file
f.write(template)

#clone handle file
f.close()

#print screen
print template
