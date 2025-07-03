import pysparql_anything as sa

engine = sa.SparqlAnything()

engine.run(query='queries/biographical_situations.sparql', output='kg/biographical_situations.nt', format='nt')
