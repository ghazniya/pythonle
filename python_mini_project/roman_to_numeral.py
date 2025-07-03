def roman_to_numeral(s):
    num=0
    if "CM"in s:
        num+=900
        s=s.replace("CM","")
    if "CD"in s:
        num+=400
        s=s.replace("CD","")
    if "XC" in s:
        num+=90
        s=s.replace("XC","")
    if "XL" in s:
        num+=40
    if "IX"in s:
        num+=9
        s=s.replace("IX","")
    if "IV" in s:
        num+=4
        s=s.replace("IV","")
    for i in s:
        if i=='M':
            num+=1000
        elif i=='D':
            num+=500
        elif i=='C':
            num+=100
        elif i=='L':
            num+=50
        elif i=='X':
            num+=10
        elif i=='V':
            num+=5
        elif i=='I':
            num+=1
    return num
l=input("Enter the roman numeral to be translated:")
print("The roman numeral",l,"is translated to",roman_to_numeral(l))