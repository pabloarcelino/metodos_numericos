import math

def func(x,a0,a1,a2,a3,a4,a5):
    f = a0*x**2+a1*x+a2+math.exp(a3*math.sin(x**2)+a4*math.sin(x)+a5)
    f = float(f)
    return f

def der1(x,a0,a1,a2,a3,a4,a5):
    f = 2*a0*x+a1+(2*x*a3*math.cos(x**2)+a4*math.cos(x))*math.exp(a3*math.sin(x**2)+a4*math.sin(x)+a5)
    f = float(f)
    return f

def der2(x,a0,a1,a2,a3,a4,a5):
    f = 2*a0+((2*a3*math.cos(x**2)-4*(x**2)*a3*math.sin(x**2)-a4*math.sin(x))*math.exp(a3*math.sin(x**2)+a4*math.sin(x)+a5))+((2*x*a3*math.cos(x**2)+a4*math.cos(x))**2)*math.exp(a3*math.sin(x**2)+a4*math.sin(x)+a5)
    f = float(f)
    return f

def modulo(x):
        if x < 0:
                return x*(-1)
        else:
                return x

def newton(x,errom,nmax):
        
        print("******************************************************")
        print("****************** MÉTODO DE NEWTON ******************")
        print("******************************************************")
        n = 1
        print("Iteração        Raiz            Erro")
        ss="%.6f"%x
        print("    0        ",ss)
        
        if der1(x,a0,a1,a2,a3,a4,a5) != 0:
                x2 = x - (func(x,a0,a1,a2,a3,a4,a5)/der1(x,a0,a1,a2,a3,a4,a5))
                while (errom <= modulo(x2 - x)) and (n < nmax):
                        ss="%.6f"%x2
                        ff="%.6f"%modulo(x2 - x)
                        print("   ",n,"       ",ss,"      ",ff)
                        x = x2
                        if der1(x,a0,a1,a2,a3,a4,a5) != 0:    
                                x2 = x - (func(x,a0,a1,a2,a3,a4,a5)/der1(x,a0,a1,a2,a3,a4,a5))
                                n = n + 1
                        else:    
                                print("DERIVADA NULA!!!")
                                break
                if n < nmax:
                    ss="%.6f"%x2
                    ff="%.6f"%modulo(x2 - x)
                    print("   ",n,"       ",ss,"      ",ff)
                    x = x2
                    if der1(x,a0,a1,a2,a3,a4,a5) != 0:    
                        x2 = x - (func(x,a0,a1,a2,a3,a4,a5)/der1(x,a0,a1,a2,a3,a4,a5))
                    else:    
                        print("DERIVADA NULA!!!")
        else:
                print("DERIVADA NULA!!!")
        print()        

def newtonmodificado(x,errom,nmax):
        
        print("*******************************************************")
        print("************* MÉTODO DE NEWTON MODIFICADO *************")
        print("*******************************************************")
        n = 1
        print("Iteração        Raiz            Erro")
        ss="%.6f"%x
        print("    0        ",ss)
        
        if (2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)) != 0:
                x2 = x - ((2*func(x,a0,a1,a2,a3,a4,a5)*der1(x,a0,a1,a2,a3,a4,a5))/(2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)))
                while (modulo(x2-x) >= errom) and (n < nmax):
                        ss="%.6f"%x2
                        ff="%.6f"%modulo(x2 - x)
                        print("   ",n,"       ",ss,"      ",ff)
                        x = x2
                        if (2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)) != 0:    
                                x2 = x - ((2*func(x,a0,a1,a2,a3,a4,a5)*der1(x,a0,a1,a2,a3,a4,a5))/(2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)))
                                n = n + 1
                        else:    
                                print("DERIVADA NULA!!!")
                                break
                if n < nmax:
                    ss="%.6f"%x2
                    ff="%.6f"%modulo(x2 - x)
                    print("   ",n,"       ",ss,"      ",ff)
                    x = x2
                    if (2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)) != 0:    
                                x2 = x - ((2*func(x,a0,a1,a2,a3,a4,a5)*der1(x,a0,a1,a2,a3,a4,a5))/(2*(der1(x,a0,a1,a2,a3,a4,a5))**2 - func(x,a0,a1,a2,a3,a4,a5)*der2(x,a0,a1,a2,a3,a4,a5)))
                    else:    
                        print("DERIVADA NULA!!!")
        else:
                print("DERIVADA NULA!!!")
        print()        

def secantes(a,b,errom,nmax):
        n = 1
        print("*******************************************************")
        print("***************** MÉTODO DAS SECANTES *****************")
        print("*******************************************************")
        print("Iteração        Raiz            Erro")
        while modulo(b-a) > errom and n < nmax:
                if (func(b,a0,a1,a2,a3,a4,a5) - func(a,a0,a1,a2,a3,a4,a5)) != 0:
                        x3 = (a*func(b,a0,a1,a2,a3,a4,a5) - b*func(a,a0,a1,a2,a3,a4,a5))/(func(b,a0,a1,a2,a3,a4,a5) - func(a,a0,a1,a2,a3,a4,a5))
                        a = b
                        b = x3
                        ss="%.6f"%x3
                        ff="%.6f"%modulo(b - a)
                        print("   ",n,"       ",ss,"      ",ff)
                        n = n + 1
                else:
                        print("DENOMINADOR NULO!!!")
                        break
        """if n < nmax:
            if (func(b,a0,a1,a2,a3,a4,a5) - func(a,a0,a1,a2,a3,a4,a5)) != 0:
                x3 = (a*func(b,a0,a1,a2,a3,a4,a5) - b*func(a,a0,a1,a2,a3,a4,a5))/(func(b,a0,a1,a2,a3,a4,a5) - func(a,a0,a1,a2,a3,a4,a5))
                a = b
                b = x3
                ss="%.6f"%x3
                ff="%.6f"%modulo(b - a)
                print("   ",n,"       ",ss,"      ",ff)
            else:
                print("DENOMINADOR NULO!!!")"""
        print()

print("COEFICIENTES DA EQUAÇÃO:")

a0 = input("a0:")
a1 = input("a1:")
a2 = input("a2:")
a3 = input("a3:")
a4 = input("a4:")
a5 = input("a5:")

a0 = float(a0)
a1 = float(a1)
a2 = float(a2)
a3 = float(a3)
a4 = float(a4)
a5 = float(a5)

errom = input("Entre com o valor do erro máximo: ")
errom = float(errom)

nmax = input("Entre com o número máximo de iterações: ")
nmax = float(nmax)

opcao = -1

print("OPÇÕES DE ENTRADA PARA O MÉTODO DE NEWTON-RAPHSON:")
while opcao!=1 and opcao!=2 and opcao!=3:
        print("Digite o número correspondente à opção desejada para a escolha da aproximação inicial:")
        print("1 - Entrar com o ponto médio do intervalo dado.")
        print("2 - Entrar com um ponto qualquer no intervalo dado.")
        print("3 - Entrar com um ponto qualquer, sem intervalo.")
        opcao = input("Digite a opção desejada:")
        opcao = int(opcao)

if opcao == 1:
        
        aux7 = 0.0
        while aux7 >= 0.0:
            print("Entre com o intervalo [a,b] válido")
            a = input("a = ")
            b = input("b = ")
            a = float(a)
            b = float(b)
            aux7 = func(a,a0,a1,a2,a3,a4,a5)*func(b,a0,a1,a2,a3,a4,a5)
            pn = (a + b)/2
            float(pn)
            print("")
elif opcao == 2:
        aux7 = 0.0
        while aux7 >= 0.0:
            print("Entre com o intervalo [a,b] válido")
            a = input("a = ")
            b = input("b = ")
            a = float(a)
            b = float(b)
            aux7 = func(a,a0,a1,a2,a3,a4,a5)*func(b,a0,a1,a2,a3,a4,a5)
        if a > b:
                aux = b
                b = a
                a = aux
        pn = input("Entre com um ponto qualquer do intervalo dado ")
        pn = float(pn)
        if pn < a or pn > b:
                while pn < a or pn > b:
                        pn = input("Entre com um ponto qualquer do intervalo dado ")
                        pn = float(pn)
else:
        pn = input("Digite um ponto qualquer como aproximação inicial: ")
        pn = float(pn)

newton(pn,errom,nmax)

opcao = -1

print("OPÇÕES DE ENTRADA PARA O MÉTODO DE NEWTON MODIFICADO:")
while opcao!=1 and opcao!=2 and opcao!=3:
        print("Digite o número correspondente à opção desejada para a escolha da aproximação inicial:")
        print("1 - Entrar com o ponto médio do intervalo dado.")
        print("2 - Entrar com um ponto qualquer no intervalo dado.")
        print("3 - Entrar com um ponto qualquer, sem intervalo.")
        opcao = input("Digite a opção desejada:")
        opcao = int(opcao)

if opcao == 1:
        aux7 = 0.0
        while aux7 >= 0.0:
            print("Entre com o intervalo [a,b] válido")
            a = input("a = ")
            b = input("b = ")
            a = float(a)
            b = float(b)
            aux7 = func(a,a0,a1,a2,a3,a4,a5)*func(b,a0,a1,a2,a3,a4,a5)
            pnm = (a + b)/2
            float(pnm)
            print(pnm)
elif opcao == 2:
        aux7 = 0.0
        while aux7 >= 0.0:
            print("Entre com o intervalo [a,b] válido")
            a = input("a = ")
            b = input("b = ")
            a = float(a)
            b = float(b)
            aux7 = func(a,a0,a1,a2,a3,a4,a5)*func(b,a0,a1,a2,a3,a4,a5)
        if a > b:
            aux = b
            b = a
            a = aux
        pnm = input("Entre com um ponto qualquer do intervalo dado ")
        pnm = float(pnm)
        if pnm < a or pnm > b:
                while pnm < a or pnm > b:
                        pnm = input("Entre com um ponto qualquer do intervalo dado ")
                        pnm = float(pnm)
else:
        pnm = input("Digite um ponto qualquer como aproximação inicial: ")
        pnm = float(pnm)

newtonmodificado(pnm,errom,nmax)

#aux7 = 0.0
#while aux7 >= 0.0:
print("Para o método das secantes, entre com o intervalo de separação válido:")################SE EU COLOCAR A RAÍZ COMO O EXTREMO DO INTERVALO, ELE NÃO ACEITA!
asec = input("a = ")
bsec = input("b = ")
asec = float(asec)
bsec = float(bsec)
 #   aux7 = func(asec,a0,a1,a2,a3,a4,a5)*func(bsec,a0,a1,a2,a3,a4,a5)

secantes(asec,bsec,errom,nmax)


















