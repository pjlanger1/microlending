import requests
import json

"""
This code runs an introspection query on KIVA's production databases via API POST requests to their graphQL.
It should return an exhaustive schema of available fields within the system.
"""

url = "https://gateway.production.kiva.org/graphql"

introspection_query = """
{
  __schema {
    types {
      name
      kind
      possibleTypes {
        name
      }
      fields {
        name
        args {
          name
          type {
            name
          }
        }
        type {
          name
        }
      }
      inputFields {
        name
        type {
          name
        }
      }
      interfaces {
        name
      }
      enumValues {
        name
      }
      ofType {
        name
      }
    }
  }
}
"""

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps({"query": introspection_query})
)


data = response.json()

#print out the human-readable schema 
[t for t in data.get('data').get('__schema').get('types') if t.get('name')]
