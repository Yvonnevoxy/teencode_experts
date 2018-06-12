#list,turples,#for$while loops,function
student = {'name': 'John', 'age': 25, 'courses': ['maths', 'english']}
student['phone'] = '0744345758'
student.update({'name': 'Yvonne', 'age': 22, 'country': 'Kenya'})
del student['age']
print(student)
print(student['name'])
print(student['courses'])

list = [1, 2, 3, 4, 5, 6 ];
print(list)


#for$while loops
nums = [1,2,3,4,5]

for num in nums:
	if num == 3:
		print('Found!')
		continue
	print(num)

	x = 0
	while x < 5:
		if x == 5:
			break
		print(x)
		x += 1

#function
def hello_func(greeting, name='Mary'):
	return '{}, {}'.format(greeting, name)

	print(hello_func('Hi'))

#tuple
tuple1 = ('what have you gained from andela classes')  
print(tuple1)
tuple2 = ('apple', 'banana', 'cherry')
print(tuple2)                      
tuple3 = ('do you think rural people should be expossed to the IT world?')
print(tuple3)