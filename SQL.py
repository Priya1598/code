import pandas as pd
import numpy as np
##xls = pd.ExcelFile(r'C:\Users\180100\OneDrive - NTT DATA North America\Automations_\SQL upload\DEI Training Data.xlsx')
import pyodbc
def sql_cnt():
    SERVER='165.136.18.251'
    DATABASE='COMMERCIAL'
    USERNAME='com_admin'
    PASSWORD='star#com121'
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    cnxn = pyodbc.connect(connectionString)
    print("Driver connected")
    cursor = cnxn.cursor()
    return cursor,cnxn
cursor,cnxn=sql_cnt()
# query = f"""truncate table TBL_Bronze"""
# cursor.execute(query)
# cnxn.commit()

xls = pd.ExcelFile(r'C:\Users\180100\OneDrive - NTT DATA North America\Automations_\SQL upload\DEI Training Data.xlsx')
# df1 = pd.read_excel (xls,'TBL_Bronze')
# qury = f"""truncate table TBL_Bronze"""
# cursor.execute(query)
# cnxn.commit()
# for sheet_name in xls.sheet_names:
df=pd.read_excel(xls,sheet_name='TBL_Bronze')
table_name = 'TBL_Bronze'
print(table_name)
for index,row in df.iterrows():
    columns=','.join(row.index)
    # print(columns)
    values=','.join(['?']*len(row))
    query=f'insert into {table_name}({columns})values({values})'

cursor.execute(query,tuple(row))
cnxn.commit()
# df1 = pd.read_excel (xls,'TBL_Bronze')
# table_name = 'TBL_Bronze'


# for index, row in df1.iterrows():
#     # cursor = cnxn.cursor()
#     cursor.execute(f"insert into {table_name} (Portal Id,Employee Name,Is Hlm,Employee Type,Grade,Work Country,Company Code,Enrolled Date,Elapsed Days,Completed Status,Completed Date,Aging (in Weeks),HLM,HLM NAME,L1 Mgr ID,L1 Mgr Name,L2 Mgr ID,L2 Mgr Name,L3 Mgr ID,L3 Mgr Name,L4 Mgr ID,L4 Mgr Name,L5 Mgr ID,L5 Mgr Name,L6 Mgr ID,L6 Mgr Name,Report Date) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
#                    row['Portal Id'],row['Employee Name'],row['Is Hlm'],row['Employee Type'],row['Grade'],row['Work Country'],row['Company Code'],row['Enrolled Date'],row['Elapsed Days'],row['Completed Status'],row['Completed Date'],row['Aging (in Weeks)'],row['HLM'],row['HLM NAME'],row['L1 Mgr ID'],row['L1 Mgr Name'],row['L2 Mgr ID'],row['L2 Mgr Name'],row['L3 Mgr ID'],row['L3 Mgr Name'],row['L4 Mgr ID'],row['L4 Mgr Name'],row['L5 Mgr ID'],row['L5 Mgr Name'],row['L6 Mgr ID'],row['L6 Mgr Name'],row['Report Date'])
#     cnxn.commit()




