
import psycopg2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import boto3
import json
import warnings

import pandas as pd
from kafka import KafkaConsumer
from json import dumps, loads

import config


warnings.filterwarnings("ignore")

def list_files_in_bucket(bucket_name):
    s3 = boto3.client('s3',
                      region_name='us-east-1',
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key)
    response = s3.list_objects(Bucket=bucket_name)

    # Create an empty DataFrame
    df = pd.DataFrame()

    for file in response['Contents']:
        json_obj = s3.get_object(Bucket=bucket_name, Key=file['Key'])
        body = json_obj['Body'].read().decode('utf-8')
        data = json.loads(body)

        # Convert the data into DataFrame and append it to the main DataFrame
        df = df.append(pd.DataFrame([data]), ignore_index=True)

    print(df)


list_files_in_bucket('trac-kafka-price')



# style.use('fivethirtyeight')
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#     try:
#         connection = psycopg2.connect(
#             dbname="your_db_name",
#             user="your_db_username",
#             password="your_db_password",
#             host="your_db_host_endpoint",
#             port="your_db_port_number",
#         )
#
#         cursor = connection.cursor()
#
#         # Assuming your table has columns 'timestamp' and 'price'
#         cursor.execute("SELECT timestamp, price FROM your_table_name ORDER BY timestamp DESC LIMIT 100")
#
#         data = cursor.fetchall()
#         xs = []
#         ys = []
#         for row in data:
#             xs.append(row[0])  # timestamp
#             ys.append(row[1])  # price
#
#         ax1.clear()
#         ax1.plot(xs, ys)
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the connection
#         if connection:
#             cursor.close()
#             connection.close()
#
# ani = animation.FuncAnimation(fig, animate, interval=1000)  # 1000ms = 1 sec
# plt.show()
