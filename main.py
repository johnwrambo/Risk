import pandas as pd

df = pd.read_csv(r"database\game_data.csv")
df = df.set_index("territory")
print(df.loc["alaska"]["connections"])

connection_list = df.loc["alaska"]["connections"].split(",")
for n, connected in enumerate(connection_list):
    connection_list[n] = connected.strip().replace(" ", "_")
print(connection_list)

# df.loc["alaska"]["connections"]
connection_list = df.loc["alaska"]["connections"].split(",")
for n, connected in enumerate(connection_list):
    connection_list[n] = connected.strip().replace(" ", "_")
print(connection_list)