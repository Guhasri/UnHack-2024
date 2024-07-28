
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:51:02 2024

@author: Admin
"""

import pandas as pd
import numpy as np

df=pd.read_csv("D:/KLA/Final-Workshop/Dataset-1/4th/CareAreas.csv",header=None)

array=np.array(df)[:,1:]
noOfRows=len(array)

careArea=array[0][1]-array[0][0]
print("Cara area: ",careArea)

data=pd.read_csv("D:/KLA/Final-Workshop/Dataset-1/4th/metadata.csv")
mainField=list(data['Main Field'])
subField=list(data['Sub Field size'])


coordinates=[]
subcoordinates=[]
for a in array:
    x1,x2,y1,y2=a    
    
    
    temp=[]
    temp.append(x1)
    temp.append((x2+(mainField[0]-careArea)))
    temp.append(y1)
    temp.append((y2+(mainField[0]-careArea)))
    coordinates.append(temp)    
    
    #subfields

    temp1=[]
    temp1.append(x1)
    temp1.append((x2-(careArea-subField[0])))
    temp1.append(y1)
    temp1.append(y2-(careArea-subField[0]))
    temp1.append(len(coordinates)-1)
    
    subcoordinates.append(temp1)
    
    
    
    sx1,sx2,sy1,sy2,mf=temp1
    
     
    index=0
    flag=0
    
    
    while(sy1<y2):
        
        while((sx1+subField[0])<x2):
            
            temp1=[]
            if flag==0:
                if sy2<y2:
                    sx1+=subField[0]
                    sx2+=subField[0]
                else :
                    sx1+=subField[1]
                    sx2+=subField[1]
                    temp1.append(sx1)
                    temp1.append(sx2)
                    temp1.append(sy1)
                    temp1.append(sy2)
                    temp1.append(len(coordinates)-1)
                    subcoordinates.append(temp1)
                    sy1+=subField[1]
                    sy2+=subField[1]
            flag=0
            temp1.append(sx1)
            temp1.append(sx2)
            temp1.append(sy1)
            temp1.append(sy2)
            temp1.append(len(coordinates)-1)
            subcoordinates.append(temp1)
           

        sy1+=subField[0]
        sy2+=subField[0]
        flag=1
        sx1=x1
        sx2=x2-(careArea-subField[0])
        print("sx cord: ",sx1,sx2)
          
   
    
#for i in range(5):
print(subcoordinates)

into_csv=pd.DataFrame(coordinates)
into_csv.to_csv("D:/KLA/Final-Workshop/Dataset-1/4th/mainfields.csv",header=None)

into_csv=pd.DataFrame(subcoordinates)
into_csv.to_csv("D:/KLA/Final-Workshop/Dataset-1/4th/subfields.csv",header=None)



