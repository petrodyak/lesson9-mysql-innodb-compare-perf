import threading
import datetime
import pymysql
import random
from datetime import date, timedelta
from concurrent.futures import ThreadPoolExecutor

# MySQL database configuration
host = "localhost"
user = "root"
password = "psw1234"
database = "mydb"

table_name = 'users_with_hash_index'

# Function to create table
def recreate_table(table_name):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        with conn.cursor() as cursor:
            # --CREATE TABLE {table_name} (
            create_table_query = f"""
            CREATE TABLE {table_name} (
                id INT,
                name VARCHAR(100) NOT NULL,
                date_of_birth DATE NOT NULL ,  
                INDEX IX_date_of_birth_hash (date_of_birth)  USING HASH
            ) ENGINE=InnoDB;
            """
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            cursor.execute(create_table_query)
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

# Function to insert a single row into the users table
def insert_user(user_id, name, date_of_birth):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, database=database)
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {table_name} (id, name, date_of_birth) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, name, date_of_birth))
        conn.commit()
    except Exception as e:
        print(f"Error inserting user {user_id}: {e}")
    finally:
        conn.close()

# Function to generate random names
def generate_random_name():
    first_names = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "James", "Sophia", "Petr", "Dima", "Olia", "Lena"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Himenes", "Bravo", "Stuart"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random date of birth
def generate_random_date_of_birth():
    start_date = date(1980, 1, 1)
    end_date = date(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

# Function to insert rows in parallel using threads
def insert_users_in_parallel():
    num_users =10000  # Change this number to adjust the number of users to insert
    num_threads = 5 # Change this number of threads
    print('num_users: ' , num_users)
    print('num_threads: ' , num_threads)

    try:
        recreate_table(table_name)
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            for i in range(num_users):
                user_id = i
                name = generate_random_name()
                date_of_birth = generate_random_date_of_birth()
                executor.submit(insert_user, user_id, name, date_of_birth)

    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    start_time  = datetime.datetime.now()

    insert_users_in_parallel()
    end_time  = datetime.datetime.now()
    print('Start time: ', start_time)
    print('End time: ', end_time)
    print('Duration, Sec: ', (end_time - start_time).seconds)

