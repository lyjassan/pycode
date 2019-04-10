import pandas as pd
df1=pd.read_csv(r'C:\Users\JAS\Desktop201512.csv',nrows=10)
ddf=df1.rename(columns={'RESULTS_ITEM_CODE':'RESULTS_ITEM_NAME'})
ddf.to_csv(r'C:\Users\JAS\Desktop\1201512.csv',index=None)