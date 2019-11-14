from SPARQLWrapper import SPARQLWrapper, JSON

import json


def whatIs(term,attribute):
  sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
  sql = """ 
SELECT DISTINCT  ?res
WHERE
{
  ?property wdt:P31/wdt:P279* wd:Q18616576;
           rdfs:label "%s"@en;
            wikibase:directClaim  ?wdt.
  ?country wdt:P31 wd:Q3624078.
   ?country  ?wdt ?res;
           rdfs:label "%s"@en;
           rdfs:label ?countryLabel.
  FILTER (lang(?countryLabel) = "en")
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}

ORDER BY DESC(?res)
LIMIT 10
  """%(attribute,term)
  print(term,attribute)
  sparql.setQuery(sql)

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  for result in results["results"]["bindings"]:
      print(result["res"]["value"],end="\t")

def listEach(attribute,comp,limit):
  sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
  if(comp==0):
      sql = """ 
      SELECT DISTINCT ?countryLabel ?res
      WHERE
      {
        ?property wdt:P31/wdt:P279* wd:Q18616576;
                 rdfs:label "%s"@en;
                  wikibase:directClaim  ?wdt.
        ?country wdt:P31 wd:Q3624078.
         ?country  ?wdt ?res;
                 rdfs:label ?countryLabel.
        FILTER (lang(?countryLabel) = "en")
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
      }

      ORDER BY ASC(?countryLabel)
      LIMIT 1000

      """%(attribute)
      print(attribute)
      sparql.setQuery(sql)

      sparql.setReturnFormat(JSON)
      results = sparql.query().convert()
      for result in results["results"]["bindings"]:
          print(result["countryLabel"]["value"],end="\t")
          print(result["res"]["value"],end="\n")
