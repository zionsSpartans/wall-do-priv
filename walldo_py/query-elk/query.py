from elasticsearch import Elasticsearch
 
es = Elasticsearch()
#res = es.search(index="filebeat-6.4.2-2018.11.20", body={"query": {"match": {'hostname': 'localhost.localdomain'}}})
es.get(index='filebeat-6.4.2-2018.11.20')

