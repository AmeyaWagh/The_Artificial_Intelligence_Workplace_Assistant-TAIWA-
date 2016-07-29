import webbrowser
import sys
searchurl = "http://www.google.com/?#q="
new=2
searchterm = sys.argv[1]
webbrowser.open(searchurl+searchterm,new = new)