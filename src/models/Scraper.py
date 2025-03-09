from lxml import html
import requests

class Scraper:

  url_main = 'https://www.99freelas.com.br/'
  query_url = 'https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&page='
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'
  }

  def get_html_tree(self, url):

    try:
      response = requests.get(url, headers=self.headers, timeout=5, allow_redirects=False)
      if response.ok:
        return html.fromstring(response.text)
      else:
        print(f'response not ok: {url}')

    except Exception as e:
      print(f'excessão ao tentar obter a tree da url: {url}, excessão: {e}')
      return []
    


scraper = Scraper()


