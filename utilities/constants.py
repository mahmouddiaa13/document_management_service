index_mappings = {
  "settings": {
    "analysis": {
      "analyzer": {
        "partial_match_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "edge_ngram_filter"]
        }
      },
      "filter": {
        "edge_ngram_filter": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 10
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "partial_match_analyzer",
        "fields": {
          "exact": {
            "type": "keyword"
          }
        }
      },
      "content": {
        "type": "text",
        "analyzer": "partial_match_analyzer"
      }
    }
  }
}

