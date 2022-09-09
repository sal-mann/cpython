from asyncore import write


# write a program to calculater simple iterest  
# input
# Enter principal:1300
# Enter rate(per year):7
# Enter time(in year):4

## total interest
## total ammount

principal= int (input("Enter principle:"))
rate=int (input("Enter rate(per year):"))
time=int (input("Enter time(in year):"))

simple_interest=(principal * rate *time)/100
total_ammount=principal + simple_interest

print("total interest:" + str (simple_interest))
print("total_ammount:" + str(total_ammount))




# Hey Salman Nazir you're 20 year old
f_name= "Salman"
l_name= "Nazir"
age= 20
print(f"Hey {f_name}{l_name} you're {20} year old")
