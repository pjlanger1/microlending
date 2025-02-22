# microlending repository  

### collaboration & sharing of microlending ideas and exploratory analysis  

---
## Project Plan
## stage 1:  

- **initial idea:**  
  *explore [Kiva](https://www.kiva.org)* in order to better understand:
  - credit costs to borrowers (what are they actually paying in interest)
  - who Kiva's lending partners are and how they service the debt
  - some econometrics on the loan origination countries or regions

- **have:**  
  - *a complete extract of all loans written by Kiva correspondent lenders (2013-2017) (see folder /data/extract)*  
  - *a few GraphQL methods to read their internal data to get 2018-present activity (see folder /graphql/)*  

- *need to do:*
  - hydrate the database of 2018 to Present Activity
  - begin streaming daily updates of loans-in-funding to better track the underwriting/funding/disbursement process.
      - want to capture repayment schedule
      - cadence to funding by loan theme
      - unsuccessful loan applications (loans that were not crowdfunded to completion)


___
## About GraphQL & Kiva's Implementation:

 What is GraphQL?
 It is both a query language and a resolver for said queries. It serves structured data from a variety of internal sources like REST APIs, database calls in a flexible, declarative manner.  

 Kiva's Implementation: Kiva has a robust system for developer data access. 
 
 Read their [documentation, schema and play in their sandbox with custom queries if you'd like.](https://gateway.production.kiva.org/graphql).

 **A Quick Note: ALWAYS read and abide by Terms of Service when programatically accessing such data.**

 Here's some of what I've learned about two of the query formats available to us:

**Loan ID-Queryable**

Queryable via Pagination: 
