import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by=['player_id','event_date'],ascending=[True,True])
    df = df.drop_duplicates('player_id',keep='first')
    return df[['player_id','event_date']].rename(columns={'event_date':'first_login'})
