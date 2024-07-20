import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['population'] >= 25_000_000) |
                     (world['area'] >=  3_000_000)].iloc[:,[0,3,2]]
