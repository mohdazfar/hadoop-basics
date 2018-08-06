# hadoop-basics

Hadoop word count example is available on many blogs and websites but here I have tried to go a step forward to solve slightly more real life problems with Mapreduce. Of course these are still basic examples of how hadoop can be used for data processing and analysis but they'll allow you to understand Mapreduce programs in a better way.

Use the following steps to make it run yourself:
1. Download Hadoop on your linux machine. An easy way of working doing is to make a docker image of hadoop by using the following commands. For this you need to instal docker first
```sh
root@ubuntu:~$ docker pull sequenceiq/hadoop-docker:2.7.0  && docker run -it sequenceiq/hadoop-docker:2.7.0 
```

2. After performing step 1, you'll be inside the hadoop image and it will be interactive shell just like your terminal. You can now use the following command to check if hadoop nodes are running. `jps` command will return the following results:
```sh
bash-4.1# jps
545 ResourceManager
872 Jps
212 DataNode
366 SecondaryNameNode
125 NameNode
638 NodeManager
```

3. Now as your hadoop nodes are running let's run the examples in the repository. First you need to copy the repository to the hadoop image. You can do that using the following command
```sh
root@ubuntu:~$ docker cp /REPO_DIRECTORY IMAGE_NAME:/usr/local/hadoop/
```

4. After copying the repository into container we can now run the examples. Use the following command:
```sh
bash-4.1# bin/hadoop jar hadoop-streaming-2.7.0.jar -file salary/mapper.py -mapper "python mapper.py" -file salary/reducer.py -reducer "python reducer.py" -input YOUR_INPUT_FOLDER -output output
```
**Note:** 
i. You must copy the dataset into hdfs so that each example can work fine. Use the folloeing command to copy the data:
```sh
bash-4.1# bin/hadoop fs -mkdir salary_input_data
bash-4.1# bin/hadoop fs -copyFromLocal datasets/salarydata.txt salary_input_data/
```
ii. In this case we have run example of a mapreduce program on salary dataset. In order to run other examples, do the changes in the commands in step 4 accordingly.  

