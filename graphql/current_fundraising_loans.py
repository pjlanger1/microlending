import requests
import json

url = "https://gateway.production.kiva.org/graphql"
headers = {"Content-Type": "application/json"}

query = """
query GetFundraisingLoans($limit: Int, $pageNumber: Int) {
  fundraisingLoans(limit: $limit, pageNumber: $pageNumber) {
    totalCount
    values {
      id
      name
      loanAmount
    }
  }
}
"""

#pagination variables
limit = 100
page_number = 1
all_loans = []

while True:
    variables = {"limit": limit, "pageNumber": page_number}
    response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
    data = response.json()
    
    loans = data["data"]["fundraisingLoans"]["values"]
    total_count = data["data"]["fundraisingLoans"]["totalCount"]
    
    if not loans:
        break  

    all_loans.extend(loans)
    page_number += 1  #next
    
   
    if page_number * limit >= total_count:
        break

print(f"Retrieved {len(all_loans)} fundraising loans.")
