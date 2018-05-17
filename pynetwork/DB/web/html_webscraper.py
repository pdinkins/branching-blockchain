
def webscraper():
    from bs4 import BeautifulSoup
    import requests


    '''
    input file name
    input target website url
    scrapes html content from the target 
    
    '''

    print("================")
    print("Website Scrapper")
    print("====================")
    print("file will be saved as an .html\nin the folder the script is run from")
    print("====================")

    filename = input(str("file save name: "))
    print("========================")
    url = input(str(" target url: "))
    print("========================")

    r = requests.get(url)

    soup = BeautifulSoup(r.text)

    print(soup.prettify())
    print(soup.find_all('a'))
    f = open(filename + ".html", "w+")
    f.write(soup.prettify())
    s = soup.prettify()
    f.write(s)
    f.close()


webscraper()
