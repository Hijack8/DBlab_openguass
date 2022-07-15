

f = open("S575.txt", 'r',encoding = 'utf-8')

line = f.readline()

while(line != ''):
    y = line.split()
    
    line = f.readline()
    
    print("INSERT INTO S575 VALUES('" + y[0] + "','" + y[1] + "','" + y[2] + "','" + y[3] + "'," + str(y[4]) + ",'" + y[5] + "');")
    

f.close()


f = open("C575.txt", "r", encoding = 'utf-8')

line = f.readline()

while(line != ''):
    y = line.split()
    line = f.readline()
    print("INSERT INTO C575 VALUES('" + y[0] + "','" + y[1] + "'," + str(y[2]) + "," + str(y[3]) +",'" + y[4] + "');")
f.close()


f = open("SC575.txt", "r", encoding = 'utf-8')

line = f.readline()

while(line != ''):
    y = line.split()
    line = f.readline()
    if(len(y) == 2):
        print("INSERT INTO SC575 VALUES('" + y[0] + "','" + y[1] + "'," + "NULL" + ");")
    else:
        print("INSERT INTO SC575 VALUES('" + y[0] + "','" + y[1] + "'," + y[2] + ");")
