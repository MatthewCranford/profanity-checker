
from urllib.request import urlopen
from urllib.request import FancyURLopener

class myOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myopener = myOpener()

# Takes in a specified file and calls check_profanity on it.
def read_text():
    quotes = open("file")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    with myopener.open("http://www.wdylike.appspot.com/?q=" + text_to_check,data=None) as connection:
        output = connection.read().decode('utf-8')
        print(output)

        if "true" in output:
            print("Profanity Alert!!")
        elif "false" in output:
            print("This document has no curse words!")
        else:
            print("Could not scan the document properly.")

read_text()
