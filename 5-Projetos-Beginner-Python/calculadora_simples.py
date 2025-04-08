def Calculadora_Simples():
    print("Calculadora Simples")
    print("Operações:")
    print("1. Adição(+)")
    print("2. Subtração(-)")
    print("3. Multiplicação(*)")
    print("4. Divisão(/)")
    print("5. Sair")
    
    
    while True:
        try:
            
            Escolha = input(("Entrado em Operação(1/2/3/4/5):"))
            
            if Escolha == '5':
                print("Desligando a calculadora, Até mais!")
                
                
            if Escolha not in ['1', '2', '3', '4']:
                print("Escolha Inválida. Por favor tente novamente.")
                continue
            
            
            Número1 = float(input("Digite o primeiro número: "))
            Número2 = float(input("Digite o segundo número: "))
            
            
            if Escolha == '1':
                print(f"Resultado: {Número1} + {Número2} = {Número1 + Número2}")
            elif Escolha == '2': 
                print(f"Resultado: {Número1} - {Número2} = {Número1 - Número2}")
            elif Escolha == '3':
                print(f"Resultado: {Número1} * {Número2} = {Número1 * Número2}")
            elif Escolha == '4':
                if Número2 == 0:
                    print("Erro não há possibilidade de dividir por zero")
                else: 
                    print(f"Resultado:{Número1} / {Número2} = {Número1} / {Número2} ")
                    
        except ValueError:
            print("Botão Inválido. Por favor digite números apenas.")
            
            
    
Calculadora_Simples()
            
            