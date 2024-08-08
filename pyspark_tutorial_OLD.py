# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Data Processing").getOrCreate()


df = spark.read.json("data/test1.json")


df.show()