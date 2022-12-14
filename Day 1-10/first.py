print("Hello World!")
#This is a single-line comment
print("The weather is\npleasant today!\nThanks to God!")

'''
This is a multi-line
comment
'''

#Double Quote escape sequence
print("Hey, I'm \"Mickey\" ")

#Join using seperator
print("Hi","5","Brother!",sep="$")

#list
list=['apple','orange',[1,4],'banana']
print(list)

#tuple
tuple1=('Orange',(-2,-4),'Litchi')
print(tuple1)

#dictionary
dict1={"name":"Shakshi","age":20,"address":"Kolkata"}
print(dict1)

#Tuple is immuatble

#Typecasting-Day9
#One type to another type

a="1"
b="2"
print(int(a)+int(b))

#Eplicit-> I'm converting
#Implicit -> Python is converting on it's own

c=1.9
d=8
ans=c+d
# ans converted to float implicitly to avoid data loss
print(ans)

#Input taking from user
m=int(input("Enter any thing: "))
print(m)



