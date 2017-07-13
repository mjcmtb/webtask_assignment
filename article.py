########################
# The purpose of this is to invoke newsapi.org to
# pull a list of articles containing a key word
# in the title or description
#
##########################
import urllib2, json, sys

reload(sys)
sys.setdefaultencoding('utf-8')

#### Configuration #####
my_api_key = u'f24e2295d8a440fba028511e6e722d91'
key_word = u' Apple'
country = u'us'
language = u'en'
##########################

def main():

  print(u'Fetching articles based on keyword: {}, please wait...\n\n'.format(key_word))

  list_articles=get_filtered_article(get_source_ids())

  for filtered_article in list_articles:
    print u'Title: ' + filtered_article['title']
    print u'Description: ' + filtered_article['description']
    print u'URL: ' + filtered_article['url'] + '\n\n'


def get_filtered_article(art_source_list):

  list_articles=[]

  for art_source in art_source_list:

    url = u'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(art_source, my_api_key)
    article_resp = urllib2.urlopen(url)
    json_articles = json.loads(article_resp.read())

    for article in json_articles['articles']:

      try:
        title_lower = article['title'].lower()
        desc_lower = article['description'].lower()
      except:
        continue

      if key_word.lower() in title_lower or key_word.lower() in desc_lower:
        list_articles.append(article)

  return list_articles

def get_source_ids():

  url = u'https://newsapi.org/v1/sources?language={}&country={}'.format(language,country)

  response = urllib2.urlopen(url)

  json_cont = json.loads(response.read())

  list_sources = []

  for source in json_cont['sources']:
    list_sources.append(source['id'])

  return list_sources

if __name__=='__main__':
  main()
