import pandas as pd

from bs4 import BeautifulSoup

def get_code_snippets(body):

    soup = BeautifulSoup(body, 'html.parser')
    snippets = []
    for snippet in soup.find_all('code'):
        snippets.append(snippet.get_text())
    return snippets


if __name__ == "__main__":

    dl = pd.read_csv('./table_table1.csv')

    for i in range(5):
        print("Line number =", i)
        print(get_code_snippets(dl['Body'][i]))

        

