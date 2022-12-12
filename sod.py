import numpy as np
import pandas as pd

# read files
employees = pd.read_excel('EmployeeRoles.xlsx')
permissions = pd.read_excel('RolePermissions.xlsx')

# combine the employee file and the permissions file
all_permissions = employees.merge(permissions, how='outer', on='Role')

# some users have multiple roles, each with a differnt permissions level. we need to replace the pmermission levels with a binary (1=edit access or 0=no edit access); those values will be summed when we pivot the data; a user that has a permission that sums > 0 has access to that permission across any of their roles
df = all_permissions.replace({'Level': {'Full': 1, 'Edit': 1, 'Create': 1, 'View': 0, 'None': 0}})

# pivot the all_permissions df to get the permissions in the column headers; the index variable is all of the columns that we need to keep from the raw data
df = df.pivot_table(index='Name', values='Level', columns='Permission', aggfunc='sum').reset_index().rename_axis(None, axis=1).fillna(0)
for col in df.columns:
  if col not in index:
    df[col] = np.where(df[col] > 0, 'Yes', 'No')

# pivot the all_permissions df with the role included for presentation purposes; end user will want to see which roles each user has and the level of their permissions
df2 = all_permissions.pivot_table(index=['Name','Role'], values='Level', columns='Permission', aggfunc=','.join).reset_index().rename_axis(None, axis=1).fillna(0).replace({0 : 'None'})

# filter the df to those users with the offending permissions
tbld = 'Users that can create journal entries (Make Journal Entry) and approve journal entries (Journal Approval).'
vf = pd.unique(df[(df['Make Journal Entry'] == "Yes") & (df['Journal Approval'] == "Yes")]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Make Journal Entry', 'Journal Approval']]

# filter the df to those users with the offending permissions
tbld = 'Users that can create customer invoices (Invoice) and can either receive customer payments (Customer Deposit) or record customer payments (Customer Payment).'
vf = pd.unique(df[(df['Invoice'] == "Yes") & ((df['Customer Deposit'] == "Yes") | (df['Customer Payment'] == "Yes"))]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Invoice', 'Customer Deposit', 'Customer Payment']]

# filter the df to those users with the offending permissions
tbld = 'Users that can create vendors (Vendors) and pay vendors (Pay Bills).'
vf = pd.unique(df[(df['Vendors'] == "Yes") & (df['Pay Bills'] == "Yes")]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Customers', 'Customer Refund']]

# filter the df to those users with the offending permissions
tbld = 'Users that can create credit memos (Credit Memo) and can either receive customer payments (Customer Deposit) or record customer payments (Customer Payment).'
vf = pd.unique(df[(df['Credit Memo'] == "Yes") & ((df['Customer Deposit'] == "Yes") | (df['Customer Payment'] == "Yes"))]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Credit Memo', 'Customer Deposit', 'Customer Payment']]

# filter the df to those users with the offending permissions
tbld = 'Users that can create customers (Customers) and issue customer refunds (Customer Refund).'
vf = pd.unique(df[(df['Customers'] == "Yes") & (df['Customer Refund'] == "Yes")]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Customers', 'Customer Refund']]

# filter the df to those users with the offending permissions
tbld = 'Users that can create customers (Customers) and credit memos (Credit Memo).'
vf = pd.unique(df[(df['Customers'] == "Yes") & (df['Credit Memo'] == "Yes")]['Name']).tolist()
lf = df2[df2['Name'].isin(vf)][['Name', 'Role', 'Customers', 'Credit Memo']]
