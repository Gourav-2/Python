t=(1,2,3,5,6,4,2,2,2)
print(t,type(t))

#creation a tuple with single element

t1=(2,)

print(t.count(2))


#modification in tuple some trick 

t2=(1,2,3)
t2=list(t2)
t2.append(4)
t2=tuple(t2)

print(t2)