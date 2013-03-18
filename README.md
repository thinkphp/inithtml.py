# inithtml.py

A simple python that creates a HTML template on the fly from your src name js (Inspired from https://github.com/jb55)

# Usage

```
$ git clone git://github.com/thinkphp/inithtml.py.git
$ cd inithtml.py
$ python inithtml jquery.js filename.html
```


##Output:

filename.html

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>Title</title>
<style type="text/css">
</style>
<script type="text/javascript" src="jquery.js"></script><script type="text/javascript">(function(){ alert("Ready to Go") })();</script>
</head>
<body>
</body>
</html>
```