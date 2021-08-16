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
