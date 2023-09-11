# Step 0 - import sqlite3
import sqlite3
import queries as q

# Step 1
# Connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2
cursor = connection.cursor()

# Step 3
# (See the queries.py file)

# Step 4
# "pulling the results" from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])