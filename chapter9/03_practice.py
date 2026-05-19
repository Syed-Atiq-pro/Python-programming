# printing a tables book from 2 to 20 in  folder called tables

def Gentable(n):
    table=""
    for i in range(1,11):
        table += f'{n}x{i}={n*i}\n'
    with open(f"tables/table{n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    Gentable(i)