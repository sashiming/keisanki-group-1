def func_read_data():
    import os
    dirname_2 = os.path.dirname(os.path.dirname(__file__))
    filename1 = os.path.join(dirname_2,"data",'data.txt')
    filename2 = os.path.join(dirname_2,"data",'dictionary1.txt')
    filename3 = os.path.join(dirname_2,"data",'dictionary2.txt')
    #print(filename1)
    with open(filename1,encoding = "utf-8") as f1:
        data = f1.read()
    with open(filename2,encoding="utf-8") as f2:
        dictionary1 = f2.read()
    with open(filename3,encoding="utf-8") as f3:
        dictionary2 =f3.read()
    return data,dictionary1,dictionary2 
