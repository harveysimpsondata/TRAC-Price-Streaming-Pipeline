# EC2 Kafka Instance

### Key
If using MAC OS use following command to change permission of key file
```bash
sudo chmod 400 YOUR_KEY.pem
```

### Kafka Installation and Setup
ssh into the instance then download kafka version 2.12-3.3.1
```bash
wget https://archive.apache.org/dist/kafka/3.3.1/kafka_2.12-3.3.1.tgz
```
Unzip
```bash
tar -xzf kafka_2.12-3.3.1.tgz
```
Download Java
```bash
sudo yum install java-1.8.0-openjdk
```
NOTE: Java Download For EC3
```bash
sudo yum install java-1.8.0-amazon-corretto
```
Kafka server is pointing to a private server. Change server.properties so it can run your ec2 public ip address. Before you do that you must add an ec2 security group for incoming traffic to be able to create a broker. I had to change inbounding traffic to all traffic instread of My IP address to prevent connection timeouts. After security changes run this command to configure kafka server. 
```bash
sudo nano /home/ec2-user/kafka_2.12-3.3.1/config/server.properties
```
Change the following lines
```bash
advertised.listeners=PLAINTEXT://YOUR_EC2_PUBLIC_IP:9092
```
### Start Zookeeper
```bash
cd kafka_2.12-3.3.1
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka Server
Open another terminal window and ssh into ec2 instance. Run the following command to increase memory for server. This will allocate some amount of memory to kafka server.
```bash
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
```
Then run the following command to start kafka server

```bash
cd kafka_2.12-3.3.1
bin/kafka-server-start.sh config/server.properties
```
### Create a Topic
Open another terminal window and ssh into ec2 instance. Run the following command to create a topic
```bash
cd kafka_2.12-3.3.1
bin/kafka-topics.sh --create --topic TOPIC_NAME --bootstrap-server EC2_PUBLIC_IP:9092 --replication-factor 1 --partitions 1
```

### Start Producer
Run the following command to start producer
```bash
bin/kafka-console-producer.sh --topic TOPIC_NAME --bootstrap-server EC2_PUBLIC_IP:9092
```

### Start Consumer
Run the following command to start consumer
```bash
bin/kafka-console-consumer.sh --topic TOPIC_NAME --bootstrap-server EC2_PUBLIC_IP:9092
```






