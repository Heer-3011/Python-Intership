#dict
student={
    'name': "Heer",
    'enrollment':54009,
    'sem':8,
    'course':'Information Technology'
}

print(len(student)) 
print("Student name=",student['name'])
#nested dict

student1={
    'name': "Heer",
    'enrollment':54009,
    'sem':8,
    'subject':{
        'sub1':'Internet of things(IOT)',
        'sub2':'Agument and relaity(ARVR)',
        'sub3':'Distributed andd parllel compunting(DPC)',
    },
    'course':'Information Technology'
}

print(student1['subject']['sub1'])
print(student1['subject']['sub2']) 

#list
fruits=['kiwi','guava','pineapple','mangoes']
print(fruits)
count=0
for i in range(0,len(fruits),1):
    print(fruits[i])
    count+=1

print(count)

print(fruits[2:5])
fruits.append('watermelon')

fruits.remove('kiwi')
print(fruits)

print(fruits.pop())
print(fruits)
 

#Tuple
tuple1=(15,23,'Shobhana',45,[1,2,3],{'name':'heer'})
tuple2=(52,42,43,'Heer')
print(tuple1[4][2])
print(tuple1[5]['name'])
tup=tuple1+tuple2
print(tup)
print(type(tup))

set = {'Patel',364,12.3,'h'}
print(set) 
