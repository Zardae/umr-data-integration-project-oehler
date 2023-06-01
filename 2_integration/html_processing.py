from bs4 import BeautifulSoup



if __name__ == "__main__":
    file = open("../0_datasets/bw2_route_20.html", "r")
    soup = BeautifulSoup(file, 'html.parser', from_encoding="windows-1252")
    main_tag = soup.main
    for string in main_tag.stripped_strings:
        print(repr(string))
