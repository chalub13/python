# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json
import textwrap

with urllib.request.urlopen(
    "https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224"
) as f:
    text = f.read()
    decodedText = text.decode("utf-8")
    print(textwrap.fill(decodedText, width=50))

print()

obj = json.loads(decodedText)
print(obj["kind"])

print()
print(obj["items"][0]["searchInfo"]["textSnippet"])

print()
for item in obj["items"]:
    print(item["searchInfo"]["textSnippet"])
