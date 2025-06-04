#!/bin/bash

curl -X POST http://localhost:8083/connectors \
  -H "Content-Type: application/json" \
  -d '{
    "name": "es-connector",
    "config": {
      "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
      "tasks.max": "1",
      "topics": "ufc-events",
      "connection.url": "http://elasticsearch:9200",
      "key.ignore": "true",
      "type.name": "_doc",
      "name": "es-connector"
    }
  }'
