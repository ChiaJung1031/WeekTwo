def avg(data):
# 請用你的程式補完這個函式的區塊
 count = data["count"]
 sum=0
 averge=0
 for i in range(3):
  salary = data["employees"][i]["salary"]
  sum += salary
  averge = sum / count
 print(averge)
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式