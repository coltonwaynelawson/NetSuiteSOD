# NetSuite Segregation of Duties (SOD) Audit
**Project goal**: The primary goal of the analysis is to determine which users have roles, or combinations of roles, that cause a segregation of duties issue in NetSuite.

**Tech used**: Python

**Datasets**: The data structure is extracted from NetSuite using the native Saved Search Functionality

## Step #1: Pull the employee file from NetSuite using Saved Search
Create a new saved search on the **Employee** search type.
![image](https://user-images.githubusercontent.com/46463801/207162904-e8d3826c-c656-45c3-8c73-137eeb7069f9.png)

Do not include any Criteria.
![image](https://user-images.githubusercontent.com/46463801/207162937-a3b517da-0d65-4173-a820-4cf3ac40c761.png)

Include **Name** and **Role** in the Results.
![image](https://user-images.githubusercontent.com/46463801/207163040-62a26dbe-617c-4fa4-b504-4323e442a517.png)

Click **Save & Run** and export the resulting report to Excel.

## Step #2: Pull the permissions file from NetSuite using Saved Search
Create a new saved search on the **Role** search type.
![image](https://user-images.githubusercontent.com/46463801/207163531-1fdb905e-cb21-4c62-ae71-29dc6e2978a3.png)

Do not include any Criteria.
![image](https://user-images.githubusercontent.com/46463801/207163551-c978e81c-a3fa-4587-851e-6539fe5d771a.png)

Include **Name**, **Permission**, and **Level** in the Results.
![image](https://user-images.githubusercontent.com/46463801/207163558-0677b8ab-4dc6-4806-82e0-cf154080f374.png)

Click **Save & Run** and export the resulting report to Excel.

## Step 3: Run the analysis in Python
Use the Employee File and the Permissions File from steps #1 and #2 above as the inputs to the analysis and run the code in the [SOD Analysis](https://github.com/coltonwaynelawson/NetSuiteSOD/blob/main/sod.ipynb) to find the users that have a segregation of duties issue. This analysis focuses on standard NetSuite permissions that could cause segregation of duties issues (e.g. what could go wrong) if not addressed.

 -	Users that can create journal entries (Make Journal Entry) and approve journal entries (Journal Approval)
 -	Users that can create customer invoices (Invoice) and can either receive customer payments (Customer Deposit) or record customer payments (Customer Payment)
 -	Users that can create vendors (Vendors) and pay vendors (Pay Bills)
 -	Users that can create credit memos (Credit Memo) and can either receive customer payments (Customer Deposit) or record customer payments (Customer Payment)
 -	Users that can create customers (Customers) and issue customer refunds (Customer Refund)
 -	Users that can create customers (Customers) and credit memos (Credit Memo)
 
Please note that each NetSuite instance can be configured either via Suite Script or Workflows to have different transaction routing for different transaction types, so a segregation of duties issue in one environment may not be a segregation of duties issue in a different environment. The data you see in the [SOD Analysis](https://github.com/coltonwaynelawson/NetSuiteSOD/blob/main/sod.ipynb) was obfuscated using Faker so as not to give away any PII.
