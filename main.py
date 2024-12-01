import sqlite3
import csv

df = sqlite3.connect('data/example.bd')
cursor = df.cursor()

example = cursor.execute(''' SELECT * FROM example ''').fetchall()

with open('output/output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(example)

df.close()