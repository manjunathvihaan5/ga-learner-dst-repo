# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
p_a= df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

p_b=df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

df1=df[df['purpose']=='debt_consolidation']


p_a_b=df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0]
print(p_a_b)

result=(p_a==p_a_b)
print(result)



#task2

prob_lp= df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
print(prob_lp)

prob_cs= df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
print(prob_cs)


new_df= df[df['paid.back.loan'] == 'Yes']

prob_pd_cs=new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)


bayes= (prob_pd_cs * prob_lp)/prob_cs
print(bayes)


#task 3


df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title('Probability distribution of purpose')
plt.xlabel('No. of purpose')
plt.ylabel('Probability')
plt.show()


df1=df[df['paid.back.loan']=='No']

df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title('Probability distribution of purpose')
plt.xlabel('No. of purpose')
plt.ylabel('Probability')
plt.show()

#task 4

inst_median=df.installment.median()
print(inst_median)

inst_mean= df.installment.mean()
print(inst_mean)

df.installment.plot(kind='hist')
plt.show()



df['log.annual.inc'].plot(kind='hist')
plt.show()





