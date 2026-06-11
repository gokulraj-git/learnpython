#filename="day004.json"
data=open("day004.json").read()
for row in data:
    if row("salary")>55000:
        print(row)
