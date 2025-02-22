#variables
a = 4
b = 3
print(a + b)

#functions,loops
def main():
    a = 3
    b = 0
    if a > b:  #if else statement
        print("a is greater than b")
    elif a < b:
        print("a is less than b")   
    else:
        print("a is equal to b")
        
txt = "I am soham" 
for i in range(3): #for loop  
 print(txt)

i = 1
while i < 6:  #while loop
  print(i)
  i += 1

if __name__ == "__main__":
    main()

#LISTS

list1 = ["stumps", "bat", "ball", "gloves", "pads", "helmet"]
list1.append("guard") #add element to last index
list1.insert(1, "thighpads") #add element to specific index
print(*list1)
list1.pop() #eliminates last element
list1.reverse() #reverses the list
print(*list1)

#DICTIONARY

dict  =  {
    "name" : "soham",
    "dob"  : "18 feb 2004" ,
    "age"  : "21",
    "education" : "Btech"
}
#print(dict)
for a, b in dict.items():  #looping method
   print(a,b)

w = dict["education"] #accessing specific element
dict["name"] = 'SOHAM'
print(dict)

#SET

bucket = {"apple", "banana", "cherry", "apple"}
print(bucket) #removes duplicate values also
print("apple" in bucket) #returns TRUE if present or returns FALSE

#TUPLES
bucket1 = ("apple", "banana", "cherry")
#print(bucket1)
print(bucket1[2]) #accessing specific element from tuple

#updating tuple
bucket2 = ("watermelon", "mango")
t = list(bucket2)
t[0] = "kiwi"
bucket2 = tuple(t)
print(bucket2)