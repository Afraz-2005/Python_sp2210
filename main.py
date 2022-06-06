#Answer to question 1 (used nested for loops)

n_rows = 7
for i in range(0, n_rows + 1):
    for j in range(n_rows-i, 0, -1):
        print(j, end=' ')
    print('')
    
#Answer to question 2 

input = int(input("Enter employee ID: "))

def get_employee(inp_id,):
    employee_id = [1001, 1002, 1003, 1004, 1005]
    if inp_id in employee_id:
        return "Valid ID : ", inp_id
    else:
        return "Invalid ID"

print(get_employee(input))
