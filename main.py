import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    IceCreamSales=[]
    Temperature=[]
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
           Temperature.append(float(row["Temperature"]))
           IceCreamSales.append(float(row["Ice-cream Sales"]))
    return {"x":IceCreamSales,"y":Temperature}

def findCorrelation(datasource):
    Correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between temperature vs IceCreamSales",Correlation[0,1])
def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()
       