
# coding: utf-8

# In[68]:

import pandas as pd
import numpy as np
import xml.etree.cElementTree as ET

data = pd.read_csv(open('profile.csv'))
print(data)
print(data.columns)

#converting to numpy array
numbofpts=data.as_matrix([data.columns])
numbofpts[:,2]

#finding avg age
numbofpts[:,2].mean()

avg_open=numbofpts[:,4].mean()
avg_con=numbofpts[:,5].mean()
avg_ext=numbofpts[:,6].mean()
avg_agr=numbofpts[:,7].mean()
avg_neu=numbofpts[:,8].mean()
gender_ratio=numbofpts[:,3].mean()
print("ratio")
print(gender_ratio)
if gender_ratio>0.5:
    gender=1
else:
    gender=0

print(gender)

output_data=data
del output_data['age']
output_data.insert(2, 'age','25-34')
output_data['gender']=gender
output_data['ope']=avg_open
output_data['con']=avg_con
output_data['ext']=avg_ext
output_data['agr']=avg_agr
output_data['neu']=avg_neu
del output_data['Unnamed: 0']

output_arr=output_data.as_matrix([output_data.columns])
a=0   
for row in output_arr:
    if row[2]==1:
        gend="female"
    else:
        gend="male"
    xmlel = ET.Element("user-id="+str(row[0])+"\n"+"age_group="+str(row[1])+"\n"+"gender="+gend+"\n"+"extrovert="+str(row[5])+"\n"+"neurotic="+str(row[7])+"\n"+"agreeable="+str(row[6])+"\n"+"conscientious="+str(row[4])+"\n"+"open="+str(row[3])+"\n")
    tree = ET.ElementTree(xmlel)
    tree.write(str(row[0])+".xml")
    if a>3:
        break
    a=a+1
        



