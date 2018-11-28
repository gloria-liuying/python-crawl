# -*- coding:utf-8 -*-

import os
import time
from fang import make_request1
from elasticsearch import Elasticsearch
from datetime import datetime
from elasticsearch.helpers import bulk
from os import walk

es = Elasticsearch([{'host':'127.0.0.1','port':9200}])

json = make_request1(4)

for i in json['projectComment']:
    print(type(i['createTime']))
print(json['projectComment'])
print(json)

es.create(index="test-index4",doc_type="fangtianxia111",id=2,body={"any":json,"timesamp":datetime.now()})






