def long_one(lst):
    max_one=0
    count=0
    for i in lst:
        if i==1:
            count+=1
        else:
            if count>max_one:
                max_one=count
                count=0
            else:
                count=0
    else:
        if count>max_one:
                max_one=count
                count=0
        else:
            pass
    return max_one

a=[0,1,0,1,0,1,0,1]
print(long_one(a))