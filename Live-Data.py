
import psycopg2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    try:
        connection = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_username",
            password="your_db_password",
            host="your_db_host_endpoint",
            port="your_db_port_number",
        )

        cursor = connection.cursor()

        # Assuming your table has columns 'timestamp' and 'price'
        cursor.execute("SELECT timestamp, price FROM your_table_name ORDER BY timestamp DESC LIMIT 100")

        data = cursor.fetchall()
        xs = []
        ys = []
        for row in data:
            xs.append(row[0])  # timestamp
            ys.append(row[1])  # price

        ax1.clear()
        ax1.plot(xs, ys)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()

ani = animation.FuncAnimation(fig, animate, interval=1000)  # 1000ms = 1 sec
plt.show()
