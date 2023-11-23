# String to Integer (atoi)

# Input: s = "42"
# Output: 42

# Input: s = "+-4193 with words"
# Output: 0

def myAtoi(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    if s[0] == "-":
        sign = -1
        s = s[1:]
    elif s[0] == "+":
        sign = 1
        s = s[1:]
    else:
        sign = 1
    result = 0
    for i in range(len(s)):
        if s[i].isdigit():
            result = result*10 + ord(s[i]) - ord('0')
        else:
            break
    result = result * sign
    if result > 2**31-1:
        return 2**31-1
    elif result < -2**31:
        return -2**31
    else:
        return result
            
        

if __name__ == "__main__":
    a = "4200"
    b = "   -453452"
    c = "4193 with words"
    d = "words and 987"
    e = "-91283472332"
    f = "3.14159"
    g = "     "
    h = "    0000000000000   "
    i = "+-12" 
    j = "-"
    k = "  -04f"
    l = "+0  234"
    m = "-00001324000"
    n = "-5+"
    o = "-23+3"
    
    print("a",myAtoi(a))
    print("b",myAtoi(b))
    print("c",myAtoi(c))    
    print("d",myAtoi(d))
    print("e",myAtoi(e))    
    print("f",myAtoi(f))
    print("g",myAtoi(g))
    print("h",myAtoi(h))
    print("i",myAtoi(i))
    print("j",myAtoi(j))
    print("k",myAtoi(k))    
    print("l",myAtoi(l))
    print("m",myAtoi(m))
    print("n",myAtoi(n))
    print("o",myAtoi(o))
    
            