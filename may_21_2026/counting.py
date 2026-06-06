#Fibanoci Series 1,2,3,5,8,13,.....
f_series=[]
a,b=1,2
f_series.append(a)
f_series.append(b)
while((a+b)<50):
    c=a+b
    a=b
    b=c
    f_series.append(c)
print('fibanoci Series',f_series);