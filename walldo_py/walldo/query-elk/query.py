from elasticsearch import Elasticsearch
 
es = Elasticsearch()
res = es.search(index="filebeat-6.4.2-2018.11.24", body={"query": {"match_all": {}}})
#print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['system']))
    del doc
