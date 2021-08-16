# About this
this code was compute when i need to do homework and lazy to calculate  
so i decide to write code to make my progress faster  
[Full Code](#full_code)
# Explain
this code use to ask `string` to format the answer and the amount of point
```py 
string = input("Enter String : ").upper()
```
change length of string to amount of point
```py
n = len(string)
```
### Input
```
abc
```
### Output
```
A' (x, y)
B' (x, y)
C' (x, y)
```

Ask `angle to rotate the point` & `cordinate of center point`
```py
a = radians(int(input("Enter Deg : ")))
centerX = int(input(f"Enter X Cordinate of Center : "))
centerY = int(input(f"Enter Y Cordinate of Center : "))
```
made list of result to keep the answer
```py
result = []
```
Run program for len of string
### Program
```
ask for cordinate of current point
calculate it to rotate point
keep answer in the result list
run until end
```
### Code
```py
for i in range(n):
  #Ask for cordinate of current point
  x = int(input(f"Enter X Cordinate of Point {i+1} : "))
  y = int(input(f"Enter Y Cordinate of Point {i+1} : "))
  #calculate by formula
  x, y = ((x - centerX) * cos(a) - (y - centerY) * sin(a) + centerX, (x - centerX) * sin(a) + (y - centerY) * cos(a) + centerY)
  #at it to result list
  result.append(tuple((round(x), round(y))))
```
### Print The Result
```py
print("\n")
#print result
for i,j in enumerate(result):
   print(f"{string[i]}' ({j[0]}, {j[1]})")
```
<a name="full_code"></a>
# Full Code
```py
from math import radians, sin, cos

def main():
    #ask for string to use for format in result like "abc" it will become A', B', C'
    string = input("Enter String : ").upper()
    n = len(string)
    a = radians(int(input("Enter Deg : ")))
    centerX = int(input(f"Enter X Cordinate of Center : "))
    centerY = int(input(f"Enter Y Cordinate of Center : "))
    result = []
    for i in range(n):
        x = int(input(f"Enter X Cordinate of Point {i+1} : "))
        y = int(input(f"Enter Y Cordinate of Point {i+1} : "))
        #calculate by formula
        x, y = ((x - centerX) * cos(a) - (y - centerY) * sin(a) + centerX, (x - centerX) * sin(a) + (y - centerY) * cos(a) + centerY)
        #at it to result list
        result.append(tuple((round(x), round(y))))
    print("\n")
    #print result
    for i,j in enumerate(result):
        print(f"{string[i]}' ({j[0]}, {j[1]})")

if __name__ == "__main__":
    main()
#compute by Ace Fhid
```
