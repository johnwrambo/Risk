import pandas as pd


def get_territory_status(df:pd.DataFrame):

    slice_view = df[["territory", "is_occupied", "is_neutral"]]
    return slice_view


def get_territory_index(df, territory: str = None):
    territory_list = df["territory"].tolist()
    if territory in territory_list:
        territory_index = int(territory_list.index(territory))
        return territory_index
    else:
        return None


def check_is_occupied(df, territory):
    # index = get_territory_index(df, territory)
    occupied = df.at[territory, "is_occupied"]
    neutral = df.at[territory, "is_neutral"]
    return ""

def set_occupied(df, territory: str = None, status: bool = None):
    if status == True:
        df.loc[territory, "is_occupied"] = 1
    else:
        df.loc[territory, "is_occupied"] = 0
    return df.loc[territory, "is_occupied"]

def territory_connections(df, territory: str):
    return df.loc[territory, "connections"].split()


def init_gamedata(df):
    df[["value", "x_cor", "y_cor", "troops", "is_occupied", "is_neutral"]] = df[
        ["value", "x_cor", "y_cor", "troops", "is_occupied", "is_neutral"]].astype(int)
    df = df.set_index(df.columns[0])
    # Turn connections column in list data type
    for i in df.index:
        # print(i)
        df.at[i, "connections"] = df.at[i, "connections"].split(",")
    return df

