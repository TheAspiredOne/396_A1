'''
Group members : Avery Tan(altan:1392212), Canopus Tong(canopus:1412275)

'''


input_list = input().split()
result_list = ''
for i in range(len(input_list),0,-1):
	result_list += input_list[i-1]
	if i!=1:
		result_list+=' '
print(result_list)
