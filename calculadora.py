def menu():
        
        a = float(input("Escolha o primeiro número: "))
        b = float(input("Escolha o segundo número: "))

        print("""
Escolha uma operação:
1. Soma
2. Subtração
3. Multiplicação
4. Potência
5. Divisão
6. Divisão com resto
""")

        

        op = int(input("Escolha o código da operação: "))
        return a, b, op

def calcular():
        a, b, op = menu()

        if op == 1:
                print("Soma: {} + {} = {}".format(a,b,a+b))
        elif op == 2:
                print("Diferença: {} - {} = {}".format(a,b,a-b))
        elif op == 3:
                print("Produto: {} * {} = {}".format(a,b,a*b))
        elif op == 4:
                print("Potência: {}^{} = {}".format(a,b,a**b))
        elif op == 5:
                try:
                        print("Razão: {} / {} = {}".format(a,b,a/b))
                except:
                        print("Impossível dividir por 0!")
        elif op == 6:
                try:
                        print("Divisão com resto: {} / {} = {} Resto: {}".format(a,b,a//b,a%b))
                except:
                        print("Impossível dividir por 0!")
        else:
                print("Código inválido")
        novamente()

def novamente():
                escolha = int(input("""
Quer calcular de novo?
1: Sim
2: Não
"""))
                if escolha == 1:
                        calcular()
                elif escolha == 2: 
                        print("Até a próxima!")
                else:
                        print("Código inválido!")
calcular()
