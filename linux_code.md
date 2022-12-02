```shell
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/sources/hadoop-streaming-2.7.3.jar -files /root/map.py,/root/reduce.py -mapper "map.py" -reducer "reduce.py" -input test/facebook_combined.txt -output test/out_python1
```