# microlending repository  

### collaboration & sharing of microlending ideas and exploratory analysis  

---

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
    
