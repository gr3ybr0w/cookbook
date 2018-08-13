import pandas as pd

def distChecker(df, columns):
  outdf = pd.DataFrame()
  for i in columns:
    tempdf = pd.concat([pd.DataFrame(df[i].describe()),
           pd.DataFrame(data=df[i].skew(), index=['skew'], columns=[i]),
           pd.DataFrame(data=df[i].kurt(), index=['kurt'], columns=[i]),
           pd.DataFrame(data=df[i].var(), index=['var'], columns=[i])]).T
    outdf = pd.concat([outdf, tempdf], axis=0)
  return outdf
  
  
