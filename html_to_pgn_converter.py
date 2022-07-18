import re
import requests
from bs4 import BeautifulSoup as bs

NUMBER_OF_FILES = 12
OPENING_NAME = 'dutch_defence'

puncts = {'+/=': ' $14',
          '=/+': ' $15',
          '+-+': '+ $19',
          '+-': ' $18',
          '-+': ' $19',
          '∓': ' {-/+}',
          '±': ' {+/-}',
          '=': ' $10',
          '⇆': ' {counterplay}',
          '↑': ' {initiative}',
          '∞': ' $13',
          ' N ': r' {N} ',
          ' N)': r' {N})'
          }

def add_parentheses(content):
    content = str(content)
    content = re.sub('(<blockquote><span.*?><span.*?>)', r'\1(', content)
    content = re.sub('(<\/span><\/blockquote><\/blockquote>)', r'))\1', content)
    content = re.sub('([^\)])(<\/span><\/blockquote>)', r'\1)\2', content)
    return content

def convert_to_pgn(soup):
    soup_text = soup.get_text(separator=' ')
    soup_text = re.sub('(\d+\.+)\s', r'\1', soup_text)

    for punct in puncts:
        if punct in soup_text:
            soup_text = soup_text.replace(punct, puncts[punct])

    soup_text = re.sub('(\w)N', r'\1 {N}', soup_text)
    soup_text = soup_text + ' *'

    content_pgn = '''[Event "Study"]
[Site "Chess Opening Analysis"]
[Result "*"]
[UTCDate "2022.07.18"]
[UTCTime "18:16:00"]
[Variant "Standard"]
[ECO "A00"]
[Opening "Chess Opening"]
[Annotator "Author"]

''' + soup_text

    return content_pgn

if __name__ == '__main__':
    for i in range(1, NUMBER_OF_FILES+1):
        with open(f'pgnnewhtml{i}.html', encoding='utf-8') as f:
            # opening = OPENING_NAME.replace('_', '-')
            # r = requests.get(f'https://openings101.org/{opening}/{i}')
            # soup = bs(r.content)
            # content = soup.find('div', class_='MuiBox-root css-10z733a')
            content = f.read()
            content = add_parentheses(content)

            soup = bs(content, 'html.parser')
            content_pgn = convert_to_pgn(soup)

            countopened = content_pgn.count('(')
            countclosed = content_pgn.count(')')
            assert countopened == countclosed, f'Assertion error in file number {i}'

        with open(f'{OPENING_NAME}_{i}.pgn', 'w') as f:
            f.write(content_pgn)