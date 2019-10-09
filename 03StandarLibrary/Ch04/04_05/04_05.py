# HTML Parser Module
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("Attr:", attr)

    def handle_endtag(self, tag):
        print("End tag:", tag)

    def handle_comment(self, data):
        print("Comment:", data)

    def handle_data(self, data):
        print("Data:", data)


parser = MyHTMLParser()
parser.feed(
    "<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>"
)

input = input("Put in HTML Code")
parser.feed(input)
print()

htmlFile = open("sampleHTML.html", "r")
s = ""
for line in htmlFile:
    s += line
parser.feed(s)
