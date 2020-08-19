print("a^2x+bx+c=0")

def roots(a,b,c):

    k = (b**2 - 4*a*c)**0.5        



    x_1 = (-b + k) / (2*a)

    x_2 = (-b - k) / (2*a)



    print('x= {0}'.format(x_1))

    print('or x= {0}'.format(x_2))



if __name__ == '__main__':

    a = input('Enter a: ')

    b = input('Enter b: ')

    c = input('Enter c: ')

    roots(float(a), float(b), float(c))
    
    exec(open("SaJaAi.py").read())