# Apache_Mahout_Application

## 1. system requirements
1. Java 8
2. Hadoop version 3.2.4
3. Mahout version 0.13.0

### 1.1, Install Java
- Install java 8
```bash
sudo apt-get install openjdk-8-jdk
```
- check version
```bass
java -version
```
- add evironment
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
export PATH=$PATH:/usr/lib/jvm/java-8-openjdk-amd64/bin 
```

### 1.2. Install Hadoop
- Download Hadoop version 3.2.4 from [here](https://hadoop.apache.org/release/3.2.4.html). After extracting, configure hadoop as following [hadoop folder](./hadoop)
- evironment
```
export HADOOP_HOME=~/hadoop/ 
export PATH=$PATH:/usr/local/hadoop/bin/
export PATH=$PATH:$HADOOP_HOME/bin 
export PATH=$PATH:$HADOOP_HOME/sbin 
export HADOOP_MAPRED_HOME=$HADOOP_HOME 
export YARN_HOME=$HADOOP_HOME 
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop 
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native 
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native" 
export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar
export HADOOP_LOG_DIR=$HADOOP_HOME/logs 
export PDSH_RCMD_TYPE=ssh
```
### 1.3. Install Mahout
- Download Mahout version 0.13.0 from [here](http://archive.apache.org/dist/mahout/)
- Environment
```
export MAHOUT_HOME=~/mahout/
export PATH=$PATH:$MAHOUT_HOME/bin
```
## 2. Data
First, I got dataset [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews) from  [kaggle](www.kaggle.com). And then, I preprocessed the data to get field (user_id, book_id and rating) need for recommendation algorithm (item-based), see [here](./data/recommendation/rating.csv).

## 3. Run Mahout
- training
```python
>> from mahout import Mahout
>> book_recommendation = Mahout(data_name="rating.csv")
>> book_recommendation.training()
```
- export result to csv file
```python
>> book_recommendation.export_csv()
```
