import sqlite3
import pandas as pd

example = sqlite3.connect('data/example.bd')
cursor = example.cursor()

df = pd.read_sql('select * from example', example)
df.to_csv('output\output.csv',index=False)