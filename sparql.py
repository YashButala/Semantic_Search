from SPARQLWrapper import SPARQLWrapper, JSON


def whoIs(person):
  ret = ""
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sql = """ 
      PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>
      PREFIX dbpedia: <http://dbpedia.org/resource>
      PREFIX dbpprop: <http://dbpedia.org/property>

     SELECT DISTINCT ?person ?comment ?label
      WHERE {
        ?person rdf:type dbpedia-owl:Person.
        ?person rdfs:comment ?comment.  
        ?person rdfs:label ?label
        FILTER regex(?label, "^%s", "i")
        FILTER (LANG(?comment) = 'pt') 
      }
      LIMIT 1
      """ % ''.join((person))
  
  sparql.setQuery(sql)
  

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results["results"]["bindings"]:
      ret+=(result["comment"]["value"])
  return ret
     


def whereIs(location):
  ret = ""
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sql = """ 
      PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX dbp: <http://dbpedia.org/property/>

      SELECT *
      WHERE  { 
        ?location rdf:type dbo:Location.
        ?location dbo:location ?country.
        ?location rdfs:label ?label.
        OPTIONAL {
          ?country dbp:coordinatesType ?city.
        }
        ?country rdfs:label ?countryLabel.

        FILTER regex(?label, "^%s", "i").
       
        

      }
      LIMIT 1
      """ % ''.join((location))

  sparql.setQuery(sql)
  

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results["results"]["bindings"]:
      ret+=(result["countryLabel"]["value"])
  return ret    

def whatIs(term):
  ret=""
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sql = """ 
  PREFIX w3-owl: <http://www.w3.org/2002/07/owl#>
  SELECT ?thing, ?comment, ?label
    WHERE {
      ?thing rdf:type w3-owl:Thing.
      ?thing rdfs:comment ?comment.
      ?thing rdfs:label ?label.
      FILTER regex(?label, "^%s", "i").
      FILTER (lang(?comment) = 'pt')
    }
  LIMIT 1
  """ % ''.join((term))

  sparql.setQuery(sql)

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results["results"]["bindings"]:
      ret+= (result["comment"]["value"])
  return ret    
def howToCook(term):
  ret=""
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sql = """ 
  PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>
  PREFIX dbpedia: <http://dbpedia.org/resource>
  PREFIX dbpprop: <http://dbpedia.org/property>
     SELECT *
      WHERE {
        ?dessert rdf:type dbpedia-owl:Food.
        ?dessert dbpedia-owl:ingredientName ?ing.
        ?dessert dbpedia-owl:servingTemperature ?servingTemp.
        ?dessert rdfs:comment ?comment.
        ?dessert rdfs:label ?label.
        FILTER regex(?label, "^%s", "i")
        
        FILTER (LANG(?comment) = 'pt') 

      }
      LIMIT 1
  """ % ''.join((term))

  sparql.setQuery(sql)

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results["results"]["bindings"]:
      ret+= (result["comment"]["value"] + "\n")
      ret+= ('Ingredientes: ' + result["ing"]["value"] + "\n")
      ret+= ('Servir: ' + result["servingTemp"]["value"] + "\n")

  return ret
      
def whereWasBorn(person):
  ret=""
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sql = """ 
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

      SELECT *
      WHERE  { 
        ?person rdf:type dbo:Person.
        ?person rdfs:label ?label.
        ?person dbo:birthPlace ?country.
        ?country rdfs:label ?birthPlace.
        FILTER regex(?label, "^%s", "i")

      }

      LIMIT 1
      """ % ''.join((person))
  
  sparql.setQuery(sql)
  

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results["results"]["bindings"]:
      ret+=(result["birthPlace"]["value"])
  return ret