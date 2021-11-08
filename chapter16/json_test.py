import json
data = {
    'roles':[
        {'role':'monster','type':'pig','life':50},
        {'role':'donkey','type':'dog','life':60},
    ]
}
j_str = json.dumps(data)
print("以前的数据类型：",type(data),data)
print("通过json转化后的数据类型",type(j_str),j_str)