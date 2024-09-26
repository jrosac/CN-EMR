import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

a ="21"
b ="50" 
c = "12"
d = "89"
e = "40"
f = "15"
g = "27"
h = "38"

a1=('Joao',a)
b1=('Pedro',b)
c1=('Gabriel',c)
d1=('Antonio',d)
e1=('Tarcisio', e)
f1=('Gabigol',f)
g1=('Rogerio', g)
h1=('Rafael',h)

data=[a1, b1, c1, d1, e1, f1, g1, h1]
teste1 = spark.createDataFrame(data, ["nome", "idade"])
teste1.show()

sample=teste1.sample(0.6, seed=1234)
sample.show()