import webbrowser

def dictionary():
    ask = str(input("Enter the Word: "))
    baseLink =  "https://en.wiktionary.org/wiki/" + ask.lower()
    print(baseLink)
    webbrowser.open(baseLink, new=1)
