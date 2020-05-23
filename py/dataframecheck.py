def sum_info(df):
    print(f"Dataset Shape: {df.shape}")
    sum_ = pd.DataFrame(df.dtypes, columns=['dtypes'])
    sum_ = sum_.reset_index()
    sum_['Name'] = sum_['index']
    sum_ = sum_[['Name', 'dtypes']]
    sum_['Missing'] = df.isnull().sum().values    
    sum_['Uniques'] = df.nunique().values
    sum_['First Row'] = df.loc[0].values
    sum_['Last Row'] = df.loc[df.shape[0]-1].values

    return sum_