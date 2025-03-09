from models.Scraper import scraper

url = scraper.query_url + str(1)
tree = scraper.get_html_tree(url)
if tree is not None:
  links = tree.xpath('//h1/a[starts-with(@href, "/project/")]/@href')
  print(f'Quantidade de links: {len(links)}\n')

  for link in links[:5]:
    project_url = scraper.url_main + link
    tree = scraper.get_html_tree(project_url)

    if tree is not None:
      title = tree.xpath('//div[ contains(@class, "box-project-view-principal") ]/h1[1]/span/text()')
      description = tree.xpath('//div[ @class="container" ]/div/text()')
      howmatch_of_proposal = tree.xpath('//tr[th[ text()="Propostas:" ]]/td/text()')
      status = tree.xpath('//tr[th[ text()="Orçamento:" ]]/td/text()')
      status = True if status[0] == 'Aberto' else False
      client = tree.xpath('//div[ @class="info-usuario-nome" ]/a[@href]/span/text()')
      skills = tree.xpath('//div[ @class="container container-habilidades" ]/p/a/text()') or tree.xpath('//div[ @class="container container-habilidades" ]/p/text()')

      print({
        'project': {
          'url': project_url,
          'status': status,
          'title': title,
          'description': description[:8],
          'proposals': howmatch_of_proposal,
          'client': client,
          'skills': skills
        }
      })
      print('\n')

