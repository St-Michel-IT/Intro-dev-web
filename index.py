#!/usr/bin/env python3
# coding: utf-8
# import the required libraries
import os
import urllib.parse
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
name: str = form.getvalue("name")

# Request from envrionment variables
query_string = os.environ['QUERY_STRING']
# convert the query string to a dictionary
arguments = urllib.parse.parse_qs(query_string)

method = os.environ['REQUEST_METHOD']

content_type = os.environ['CONTENT_TYPE']

html = f"""<!DOCTYPE html>
<head>
    <title>KISS</title>
</head>
<body>
    <h1>{name if name else "Inconnu"}</h1>
    <p>Vous avez envoyé la requête suivantes: {arguments}</p>
    <p>Avec la méthode: {method}</p>
    <p>Avec la Content Type: {content_type}</p>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="" placeholder="Votre nom"/>
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""
print(html)
# TODO: https://docs.python.org/3/library/http.server.html#http.server.CGIHTTPRequestHandler, Code 200 (script output follows) is sent prior to execution of the CGI script. This pre-empts the status code.
