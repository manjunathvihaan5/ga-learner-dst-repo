# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

categorical_var=bank_data.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank_data.select_dtypes(include='number')
print(numerical_var)

categorical_var.shape
numerical_var.shape

banks= bank_data.drop(columns='Loan_ID')

banks.isnull().sum()

bank_mode=banks.mode().iloc[0]

banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())

avg_loan_amount=banks.pivot_table(values=['LoanAmount'],index=['Gender','Married','Self_Employed'],aggfunc=np.mean)
print(avg_loan_amount)

loan_approved_se=banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
print(loan_approved_se)
loan_approved_nse=banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
print(loan_approved_nse)


percentage_se=(loan_approved_se*100/614)
percentage_se=percentage_se[0]
print(percentage_se)

percentage_nse=(loan_approved_nse*100/614)
print(loan_approved_nse)


loan_term=banks['Loan_Amount_Term'].apply( lambda x : int(x)/12)

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

columns_to_show=['ApplicantIncome','Credit_History']




loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[columns_to_show]

mean_values=loan_groupby.agg([np.mean])
print(mean_values)




