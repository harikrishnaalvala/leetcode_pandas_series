import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df=accounts[accounts['income']<20000].shape[0]
    ff=accounts[(accounts['income']>=20000)&(accounts['income']<=50000)].shape[0]
    ef=accounts[accounts['income']>50000].shape[0]
    result=pd.DataFrame({
        'category':['High Salary','Low Salary','Average Salary'],
        'accounts_count':[ef,df,ff]
    })
    return result
