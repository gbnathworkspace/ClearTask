# db_utils.py

def insert_into_table(conn, table_name, data):
	try:
		# Create a cursor object
		cursor = conn.cursor()
		
		# Generate the SQL query for insertion
		columns = ', '.join(data.keys())
		values = ', '.join(['%s'] * len(data))
		insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
		
		# Execute the SQL query
		cursor.execute(insert_query, list(data.values()))
		
		# Commit the transaction
		conn.commit()
		
		print(f"Data inserted into {table_name} successfully.")
	except Exception as e:
		print(f"Error inserting data into {table_name}: {e}")
	finally:
		# Close the cursor
		cursor.close()