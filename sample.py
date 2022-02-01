	inputData = {
  "dimensions": [{
    "id": "dimension_re",
    "values": ["East", "East", "West", "SouthWest", "South","NorthEast"]
  }, {
    "id": "dimension_cnt",
    "values": ["London", "Italy", "Germany", "US", "Russia","India"]
  },{
    "id": "measure_sales",
    "values": [100, 156, 432, 462, 25,100]
  }, {
    "id": "measure_qty",
    "values": [85, 34, 153, 434, 52, 43]
  }, {
    "id": "measure_profit",
    "values": [123, 45, 421, 465, 451, 56]
  }],
  "metadata": [ {
    "id": "measure_sales",
    "label": "Sales",
    "type":"number"
  }, {
    "id": "measure_qty",
    "label": "Quantity",
     "type":"number"
  }, {
    "id": "measure_profit",
    "label": "Profit",
     "type":"number"
  },{
    "id": "dimension_re",
    "label": "Region",
    "type":"string"
  }, {
    "id": "dimension_cnt",
    "label": "County",
    "type":"string"
  }]
}


# print(inputData.keys())
# gettong the data into list for transposing the matrix
names=[]
value=[]
for i in inputData["dimensions"]:
    names.append(i["id"])
    value.append(i["values"])
    
# Transposing the matrix
new=[]
l=[]
for i in range(len(value[0])):
    for j in range(len(value)):
        l.append(value[j][i])
    new.append(l.copy())
    l.clear()
    
# getting the data into a dict and then appending 
# everythong into a list to make it into json format 
res=[]    
d=dict()
for i in range(len(new)):
    for j in range(len(new[0])):
        d[names[j]]=new[i][j]
    res.append(d.copy())
    
print(res)
















