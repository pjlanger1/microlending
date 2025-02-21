import requests
import json
from concurrent.futures import ThreadPoolExecutor

url = "https://gateway.production.kiva.org/graphql"


query = """
query LoanDetails($loanId: Int!) {
  lend {
    loan(id: $loanId) {
      id
      name
      status
      loanAmount
      paidAmount
      sector {
        name
      }
      activity {
        name
      }
      description
      fundraisingDate
      plannedExpirationDate
      tags
      use
      gender
      borrowerCount
      lenders {
        totalCount
      }
      terms {
        lenderRepaymentTerm
      }
      
      # Fields specific to LoanDirect
      ... on LoanDirect {
        businessName
        businessDescription
        trusteeId  # Instead of querying trustee { name id }, use trusteeId directly
        yearsInBusiness
      }

      # Fields specific to LoanPartner
      ... on LoanPartner {
        partner {
          name
          id
        }
        partnerName
        partnerId
        journalCount
        themes
      }
    }
  }
}

"""

#loan IDs to fetch
loan_ids = [2894531, 653051]

#fetch a single loan
def fetch_loan(loan_id):
    variables = {"loanId": loan_id}
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps({"query": query, "variables": variables})
    )
    return response.json()

#fetch loans concurrently
with ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch_loan, loan_ids))

#print results
for result in results:
    print(json.dumps(result, indent=2))
