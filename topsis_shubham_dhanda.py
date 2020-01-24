# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:03:09 2020

@author:Shubham DHANDA
"""

import numpy as np
import pandas as pd

class topsis:

     weight=[]
     impact=[]
     ideal_best=[]
     ideal_worst=[]
     rms=[]
     df=None

     def __init__(self,df,weight,impact):
           self.df= df#self.floater(a)
           self.weight=weight
           self.impact=impact
           print("Dataframe:")
           print (self.df)
           print("Weight List:")
           print (self.weight)
           print("Impact List:")
           print (self.impact)
     def choose(self):
         X_square=self.df.applymap( np.square)
         X_sum=X_square.apply(np.sum,axis=0)
         X_rms=np.sqrt(X_sum)
         #print(X_rms)


         for x in X_rms:
             self.rms.append(x)
         #print(self.rms)
         #print(self.df)
         df_new = self.df.loc[:,:].div(self.rms, axis=1)
         #self.weight=[.25,.25,.25,.25]
         df_w_new=df_new.loc[:,:].mul(self.weight,axis=1)
         #self.impact=[0,1,1,1]

         for i in range(len(df_w_new.columns)):
             if(self.impact[i]=='-'):
                    self.ideal_best.append(df_w_new.iloc[:,i].min())
                    self.ideal_worst.append(df_w_new.iloc[:,i].max())
             else:
                   self.ideal_best.append(df_w_new.iloc[:,i].max())
                   self.ideal_worst.append(df_w_new.iloc[:,i].min())
            #print(ideal_best)
            #print(ideal_worst)
         E_ideal_best = np.linalg.norm(df_w_new[list(df_w_new)].sub(np.array(self.ideal_best)), axis=1)
         E_ideal_worst = np.linalg.norm(df_w_new[list(df_w_new)].sub(np.array(self.ideal_worst)), axis=1)

         seq=np.array([E_ideal_best,E_ideal_worst])
         E_ideal=np.sum(seq,axis=0)


         P= np.divide(E_ideal_worst,E_ideal)
         order=P.argsort()
         points=order.argsort()
         points=points+1
         self.df.insert(len(self.df.columns), "Points",points)
         #print( self.df['Points'].idxmax())
         return self.df['Points'].idxmax()

#from  topsis_shubham_dhanda import topsis
#import pandas as pd

#'-' -----you want to minimize it
#'+' ---- you want to maximize it
#df=pd.read_csv('topsis.csv', index_col="Atribute")
#s=topsis(df,[.25,.25,.25,.25],['-','+','+','+'])
#print("You should Choose item at:"+str(s.choose()))