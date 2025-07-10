# yiddish_writers_graph


### SPARQL ENDPOINT
The KG is available at the url: https://kgccc.di.unito.it/sparql/yiddish-writers-kg

### SPARQL QUEQRY EXAMPLE


find all the triples of all the authors

```
PREFIX pim: <https://purl.archive.org/people-in-the-media#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>

SELECT DISTINCT *
FROM NAMED <https://kgccc.di.unito.it/sparql/yiddish-writers-kg>
WHERE { 
  GRAPH <https://kgccc.di.unito.it/sparql/yiddish-writers-kg> {
    ?sit a pim:BiographicalSituation ;
         dul:isSettingFor ?a, ?b, ?c .

    ?a rdfs:label ?author_label .
    ?c rdfs:label ?event .
    ?b rdfs:label ?entity .
    
    ?a ?c ?b .
  } 
}

```
