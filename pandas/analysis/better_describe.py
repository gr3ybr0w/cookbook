import pandas as pd

pd.concat([data.describe(include='all'),pd.DataFrame(data.dtypes, columns=['dtype']).T, pd.DataFrame(data.isna().any(), columns=['isna']).T])
