import csv
import pyodbc

conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=localhost;PORT=8888;DATABASE=kaggle;UID=sa;PWD=Super@secret1234;TDS_Version=7.3')
cursor = conn.cursor()
cursor.execute("""
  IF OBJECT_ID('sales', 'U') IS NOT NULL
    DROP TABLE sales

  CREATE TABLE sales
  (
    id                  int,
    name                varchar(250),
    platform            varchar(100),
    year_of_release     int,
    genre               varchar(100),
    publisher           varchar(100),
    na_sales            float,
    eu_sales            float,
    jp_sales           float,
    other_sales        float,
    global_sales       float,
    critic_score       float,
    critic_count       float,
    user_score         float,
    user_count         int,
    developer          varchar(100),
    rating             varchar(5)
  )
""")
conn.commit()

with open ('./sales.csv', 'r') as f:
    reader = csv.reader(f)
    id = 1;
    for row in reader:
        try:
            data = tuple("0" if (x=="N/A" or x=="tbd") else x for x in [id] + row)
            id += 1
            placeholders = ','.join(['?' for i in range(len(data))])
            query = 'INSERT INTO sales VALUES ({0})'.format(placeholders)
            cursor.execute(query, data)
        except:
            print("ERROR:", data)
            pass

conn.commit()
conn.close()


#NOTES:
# TDSVER=7.3 tsql -H localhost -p 8888 -U sa -P Super@secret1234
