Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> response = requests.get(r'https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html')
>>> text=response.content
>>> for i in text:
	if ord('a') < i < ord ('z'):
		print(i, end=" ")

		
104 116 109 108 104 101 100 116 105 116 108 101 118 101 114 121 115 105 109 112 108 101 119 101 98 112 103 101 116 105 116 108 101 98 115 101 102 111 110 116 115 105 101 104 101 100 98 111 100 121 98 103 99 111 108 111 114 104 118 101 114 121 115 105 109 112 108 101 119 101 98 112 103 101 104 105 115 105 115 110 104 108 101 118 101 108 104 101 100 101 114 104 104 104 105 115 105 115 108 101 118 101 108 104 104 101 100 101 114 104 104 104 105 115 105 115 108 101 118 101 108 104 104 101 100 101 114 114 101 116 116 121 115 109 108 108 104 112 104 105 115 105 115 115 116 110 100 114 100 112 114 103 114 112 104 112 112 108 105 103 110 99 101 110 116 101 114 111 119 118 101 108 105 103 110 101 100 105 116 105 110 116 104 101 99 101 110 116 101 114 111 102 116 104 101 115 99 114 101 101 110 112 112 108 105 103 110 114 105 103 104 116 111 119 108 105 103 110 101 100 116 111 116 104 101 114 105 103 104 116 112 112 98 111 108 100 116 101 120 116 98 112 112 115 116 114 111 110 103 116 114 111 110 103 108 121 101 109 112 104 115 105 101 100 116 101 120 116 115 116 114 111 110 103 110 121 111 117 116 101 108 108 116 104 101 100 105 102 102 101 114 101 110 99 101 118 115 98 111 108 100 112 112 105 116 108 105 99 115 105 112 112 101 109 109 112 104 115 105 101 100 116 101 120 116 101 109 117 115 116 108 105 107 101 116 108 105 99 115 112 112 101 114 101 105 115 112 114 101 116 116 121 112 105 99 116 117 114 101 105 109 103 115 114 99 101 120 109 112 108 101 112 114 101 116 116 121 112 105 99 116 117 114 101 106 112 103 108 116 114 101 116 116 121 105 99 116 117 114 101 112 112 109 101 116 104 105 110 103 108 105 103 110 101 100 100 105 102 102 101 114 101 110 116 108 121 116 111 116 104 101 112 114 103 114 112 104 105 109 103 108 105 103 110 116 111 112 115 114 99 101 120 109 112 108 101 112 114 101 116 116 121 112 105 99 116 117 114 101 106 112 103 108 116 114 101 116 116 121 105 99 116 117 114 101 112 104 114 104 111 119 98 111 117 116 110 105 99 101 111 114 100 101 114 101 100 108 105 115 116 104 111 108 108 105 104 105 115 108 105 116 116 108 101 112 105 103 103 121 119 101 110 116 116 111 109 114 107 101 116 108 105 104 105 115 108 105 116 116 108 101 112 105 103 103 121 119 101 110 116 116 111 99 108 115 115 108 105 104 105 115 108 105 116 116 108 101 112 105 103 103 121 119 101 110 116 116 111 110 101 120 112 101 110 115 105 118 101 114 101 115 116 117 114 110 116 105 110 111 119 110 116 111 119 110 108 111 108 116 111 108 105 104 105 115 108 105 116 116 108 101 112 105 103 103 121 116 101 116 111 111 109 117 99 104 116 110 100 105 110 117 102 102 101 116 108 105 104 105 115 108 105 116 116 108 101 112 105 103 103 121 103 111 116 108 111 115 116 111 108 104 110 111 114 100 101 114 101 100 108 105 115 116 104 117 108 108 105 105 114 115 116 101 108 101 109 101 110 116 108 105 101 99 111 110 100 101 108 101 109 101 110 116 108 105 104 105 114 100 101 108 101 109 101 110 116 117 108 104 114 104 101 115 116 101 100 105 115 116 115 104 117 108 108 105 104 105 110 103 115 116 111 116 111 116 111 100 121 111 108 108 105 108 107 116 104 101 100 111 103 108 105 101 101 100 116 104 101 99 116 108 105 111 119 116 104 101 108 119 110 111 108 108 105 104 105 110 103 115 116 111 100 111 116 111 109 111 114 114 111 119 111 108 108 105 117 110 99 104 119 105 116 104 109 111 109 108 105 101 101 100 116 104 101 104 109 115 116 101 114 108 105 108 101 110 107 105 116 99 104 101 110 111 108 117 108 112 110 100 102 105 110 108 108 121 104 111 119 98 111 117 116 115 111 109 101 104 114 101 102 104 116 116 112 119 119 119 121 104 111 111 99 111 109 105 110 107 115 112 112 114 108 101 116 115 106 117 115 116 108 105 110 107 116 111 104 114 101 102 105 110 100 101 120 104 116 109 108 110 111 116 104 101 114 112 103 101 111 110 116 104 105 115 115 101 114 118 101 114 112 112 101 109 101 109 98 101 114 121 111 117 99 110 118 105 101 119 116 104 101 108 99 111 100 101 102 114 111 109 116 104 105 115 111 114 110 121 111 116 104 101 114 112 103 101 98 121 117 115 105 110 103 116 104 101 105 101 119 103 101 111 117 114 99 101 99 111 109 109 110 100 111 102 121 111 117 114 98 114 111 119 115 101 114 112 98 111 100 121 104 116 109 108 
>>> re.findall('<.*?>', txt)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    re.findall('<.*?>', txt)
NameError: name 're' is not defined
>>> txt=requests.text
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    txt=requests.text
AttributeError: module 'requests' has no attribute 'text'
>>> txt=response.text
>>> import re
>>> re.findall('<.*?>', txt)
['<html>', '<head>', '<title>', '</title>', '<basefont size=4>', '</head>', '<body bgcolor=FFFFFF>', '<h1>', '</h1>', '<h2>', '</h2>', '<h6>', '</h6>', '<p>', '</p>', '<p align=center>', '</p>', '<p align=right>', '</p>', '<p>', '<b>', '</b>', '</p>', '<p>', '<strong>', '</strong>', '</p>', '<p>', '<i>', '</i>', '</p>', '<p>', '<em>', '</em>', '</p>', '<p>', '<img src=example/prettypicture.jpg alt="Pretty Picture">', '</p>', '<p>', '<img align=top src=example/prettypicture.jpg alt="Pretty Picture">', '</p>', '<hr>', '<h2>', '</h2>', '<ol>', '<li>', '<li>', '<li>', '<li>', '<li>', '</ol>', '<h2>', '</h2>', '<ul>', '<li>', '<li>', '<li>', '</ul>', '<hr>', '<h2>', '</h2>', '<ul>', '<li>', '<ol>', '<li>', '<li>', '<li>', '</ol>', '<li>', '<ol>', '<li>', '<li>', '<li>', '</ol>', '</ul>', '<p>', '<a href=http://www.yahoo.com/>', '</a>', '</p>', '<p>', '<a href=../../index.html>', '</a>', '</p>', '<p>', '</p>', '</body>', '</html>']
>>> html_set = set(re.findall('<.*?>', txt))
>>> html_set
{'<title>', '<h6>', '</strong>', '</em>', '<p>', '</p>', '<strong>', '<li>', '<p align=right>', '</i>', '<hr>', '</html>', '<basefont size=4>', '<a href=../../index.html>', '</title>', '<html>', '<a href=http://www.yahoo.com/>', '<body bgcolor=FFFFFF>', '<h2>', '<em>', '</body>', '<img align=top src=example/prettypicture.jpg alt="Pretty Picture">', '<h1>', '<ol>', '<img src=example/prettypicture.jpg alt="Pretty Picture">', '</head>', '<b>', '<i>', '</ul>', '</a>', '</h2>', '</ol>', '<head>', '<ul>', '</h1>', '</h6>', '<p align=center>', '</b>'}
>>> 