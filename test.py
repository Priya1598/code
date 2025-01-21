import pandas as pd
import pyodbc
import urllib
import pandas as pd
import csv
import os
import re
import pyodbc
from datetime import datetime, timedelta
import numpy as np
from sqlalchemy import create_engine
import urllib
import warnings
warnings.filterwarnings('ignore')
xls = pd.ExcelFile(r'C:\Users\180100\OneDrive - NTT DATA North America\Automations_\SQL upload\DEI Training Data.xlsx')
df1 = pd.read_excel (xls,'TBL_Bronze')
df2 = pd.read_excel (xls,'TBL_Silver')
df3 = pd.read_excel (xls,'TBL_Gold')
df4 = pd.read_excel (xls,'TBL_Safe_Zone')
df5 = pd.read_excel (xls,'TBL_Safe_Zone_Certification')
df6 = pd.read_excel (xls,'TBL_Unconscious')
df7 = pd.read_excel (xls,'TBL_Microaggression')


pwd =  urllib.parse.quote('star#com121')
params = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};'
                                 'Server=165.136.18.251;'
                                 'Database=Commercial;'
                                 'UID=Com_admin;'
                                 f'PWD={pwd};')
 
DB_engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), fast_executemany=True)

# connection = engine.connect()
# truncate_query = sqlalchemy.text("TRUNCATE TABLE TBL_Safe_Zone_Certification")
# connection.execution_options(autocommit=True).execute(truncate_query)


df1.to_sql('TBL_Bronze',DB_engine,if_exists='append',index=False)
df2.to_sql('TBL_Silver',DB_engine,if_exists='append',index=False)
df3.to_sql('TBL_Gold',DB_engine,if_exists='append',index=False)
df4.to_sql('TBL_Safe_Zone',DB_engine,if_exists='append',index=False)
df5.to_sql('TBL_Safe_Zone_Certification',DB_engine,if_exists='append',index=False)
df6.to_sql('TBL_Unconscious',DB_engine,if_exists='append',index=False)
df7.to_sql('TBL_Microaggression',DB_engine,if_exists='append',index=False)
# # xls = pd.ExcelFile(r'C:\Users\180100\OneDrive - NTT DATA North America\Automations_\SQL upload\DEI Training Data.xlsx')