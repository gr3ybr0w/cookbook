import pandas as pd

def removeCategoricalOutliers(df, feature, remove_to_threshold):
    if is_categorical_dtype(df[feature]):
        badF = pd.DataFrame(df[feature].value_counts() <= remove_to_threshold)
        df = df[~df[feature].isin(badF[badF[feature] == True].index.values)]
        df[feature].cat.remove_unused_categories(inplace=True)
        return df
    else:
        print('Not Category data type: {}'.format(df[feature].dtype))
