from SPARQLWrapper import SPARQLWrapper, JSON

import json
# def whoIs(person):
#   sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
#   sql = """ 
 
#       """# % ''.join((person))
  
#   sparql.setQuery(sql)
  

#   sparql.setReturnFormat(JSON)
#   results = sparql.query().convert()

#   for result in results["results"]["bindings"]:
#       print(result["comment"]["value"])


# def whereIs(location):
#   sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#   sql = """ 
#       PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
#       PREFIX dbo: <http://dbpedia.org/ontology/>
#       PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#       PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#       PREFIX dbp: <http://dbpedia.org/property/>

#       SELECT *
#       WHERE  { 
#         ?location rdf:type dbo:Location.
#         ?location dbo:location ?country.
#         ?location rdfs:label ?label.
#         OPTIONAL {
#           ?country dbp:coordinatesType ?city.
#         }
#         ?country rdfs:label ?countryLabel.

#         FILTER regex(?label, "^%s", "i").
       
        

#       }
#       LIMIT 1
#       """ #% ''#.join((location))

#   sparql.setQuery(sql)
  

#   sparql.setReturnFormat(JSON)
#   results = sparql.query().convert()

#   for result in results["results"]["bindings"]:
#       print(result["countryLabel"]["value"])


def whatIs(term,attribute):
  sparql = SPARQLWrapper("http://query.wikidata.org/sparql")
  mydict={attribute,term}
 # mydict.append(attribute)
 # mydict.append(term)
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
 #     print(result["population"]["value"],end="\n")
  #for result in results["results"]["population"]:
 #y=json.loads(results)
  #print(results)
  #jstring = json.dumps(results)
  #print(jstring)

# def howToCook(term):
#   sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#   sql = """ 
#   PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>
#   PREFIX dbpedia: <http://dbpedia.org/resource>
#   PREFIX dbpprop: <http://dbpedia.org/property>
#      SELECT *
#       WHERE {
#         ?dessert rdf:type dbpedia-owl:Food.
#         ?dessert dbpedia-owl:ingredientName ?ing.
#         ?dessert dbpedia-owl:servingTemperature ?servingTemp.
#         ?dessert rdfs:comment ?comment.
#         ?dessert rdfs:label ?label.
#         FILTER regex(?label, "^%s", "i")
        
#         FILTER (LANG(?comment) = 'pt') 

#       }
#       LIMIT 1
#   """ #% ''.join((term))

#   sparql.setQuery(sql)

#   sparql.setReturnFormat(JSON)
#   results = sparql.query().convert()

#   for result in results["results"]["bindings"]:
#       print(result["comment"]["value"] + "\n")
#       print('Ingredientes: ' + result["ing"]["value"] + "\n")
#       print('Servir: ' + result["servingTemp"]["value"] + "\n")


# def whereWasBorn(person):
#   sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#   sql = """ 
#       PREFIX dbo: <http://dbpedia.org/ontology/>
#       PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#       PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

#       SELECT *
#       WHERE  { 
#         ?person rdf:type dbo:Person.
#         ?person rdfs:label ?label.
#         ?person dbo:birthPlace ?country.
#         ?country rdfs:label ?birthPlace.
#         FILTER regex(?label, "^%s", "i")

#       }

#       LIMIT 1
#       """ #% ''.join((person))
  
#   sparql.setQuery(sql)
  

#   sparql.setReturnFormat(JSON)
#   results = sparql.query().convert()

#   for result in results["results"]["bindings"]:
#       print(result["birthPlace"]["value"])