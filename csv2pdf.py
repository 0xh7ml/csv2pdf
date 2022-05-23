import pandas as pd
import re
import numpy as np

req_cols = ["Item Name" ,"Seller SKU","Unit Price","Variation"]

# Reading the csv file
df_new = pd.read_csv('~/test.csv' , sep=';' , encoding='utf-8' ,usecols=req_cols)


# Color Columm
color = df_new['Variation'].str.split(',' ,expand=True)[0]
df_new['Color'] = color.str.split(':' , expand=True)[1]

# Size Column
size = df_new['Variation'].str.split(',' ,expand=True)[1]
df_new['Size'] = size.str.split(':' ,expand=True)[2]

if df_new = df_new[df_new['Size'].str.contains()]
del df_new['Variation']

# Get Ready stock product
df_new = df_new[df_new["Seller SKU"].str.contains("MTHPOS|mthpos|MJGMP|mjgmp|pl00|PL00|mjtj|MJTJ|CL00|cl00") == False]



# Insert data
df_new.insert(1, "PTY" , "Daraz")

# Changing headers name
df_after_rename = df_new.rename(columns={
"Item Name": "Design Name",
"Seller SKU" : "Code"
})

# Saving xlsx file
write_excel_file = pd.ExcelWriter('/storage/emulated/0/rsp.xlsx')
df_after_rename.to_excel(write_excel_file,index=False,sheet_name="RS product Sheet")
write_excel_file.save()
