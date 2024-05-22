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
#arthimetic operations
b=a
c=20
add=b+c
print(add)

sub=b-c
print(sub)

mul=a*b
print(mul)

div=b/c
print(div)

quotient=b//c
print(quotient)

remainder=b%c
print(remainder)

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