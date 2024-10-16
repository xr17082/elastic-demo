from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import json

def main():
    global elastic_client
    try:
        load_dotenv()
        
        elastic_endpoint = os.getenv("ENDPOINT")
        api_key = os.getenv("API_KEY")
        
        elastic_client = Elasticsearch(elastic_endpoint, api_key=api_key)
        
        while True:
            user_input = input("Enter a keyword to search for (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                print("Exiting the search.")
                break
            
            query = {
                "query": {
                    "multi_match": {
                        "query": user_input,
                        "fields": ["title", "author", "description"]
                    }
                }
            }

            result = elastic_client.search(index="books", body=query)

            print(json.dumps(result.body, indent=2))
        
    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
