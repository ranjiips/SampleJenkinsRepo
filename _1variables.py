name="Ranjith"
gender="Male"
fname="Ranjith"
a="nyc"
a=123
xxx=''

def print_values():
    # print(a)
    print(name)
    xxx="ccc"
    # global xxx

def print_value1():
    # print(a)
    print(xxx)

def arthimetic_operations():
    #addition
    b=a
    c=20
    add=b+c
    print(add)
    #subtraction
    sub=b-c
    print(sub)
    #multiplication
    mul=a*b
    print(mul)
    #division
    div=b/c
    print(div)
    #quotient
    quotient=b//c
    print(quotient)
    #reminder
    remainder=b%c
    print(remainder)
    #exponents
    exponents = 2**3
    print(exponents)
    #orer of predence
    order_of_precedence = (2+6)*(6*4)/4
    print(order_of_precedence)

#boolean
print(bool(0))
print(bool(1))
print(bool(0.5))
a=True
print(bool(a))
print(bool(c))


a,b,c=5,4,6
d=e=f=10
print('a={} b={} c={}'.format(a,b,c))
print('d={} e={} f={}'.format(d,e,f))

print_values()
print_value1()

a=True
a=(5)
print(type(a))
