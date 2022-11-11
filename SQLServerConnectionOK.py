# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:09:46 2022

@author: Gul Rez Khan
"""
import pandas as pd
import pyodbc
#cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=172.20.124.120;DATABASE=QC_Analysis;UID=sa;PWD=Ccclsite123")
#cnxn= ("Driver={SQL Server Native Client 11.0};" "Server=172.20.24.120,1433;" "Database=QC_Analysis;" "UID=sa;" "PWD=Ccclsite123;") 
#plant = input('Enter in number format')

#plant=1300
cnxn= ("Driver={SQL Server Native Client 11.0};" "Server=172.20.24.120,1433;" "Database=QC;" "UID=sa;" "PWD=Ccclsite123;") 

cnxn = pyodbc.connect(cnxn)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Cement")
#cursor.execute("SELECT * FROM Kilnfeed1")
tables = cursor.fetchall()
#data = pd.read_sql("SELECT * FROM Cement", cnxn)
query = ("SELECT * FROM Cement "
         f"WHERE Plant = '{1200}'")

data = pd.read_sql(query, cnxn)

print(data)
