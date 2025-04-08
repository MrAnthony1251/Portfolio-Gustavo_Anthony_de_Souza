import random
import math

# Conjunto de caracteres 
letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiais = "@#$%&*"

# Solicitação o comprimento da senha
while True:
    try:
        tamanho_senha = int(input("Digite o tamanho da senha(mínimo 4 caracteres): "))
        if tamanho_senha >= 4:
            break
        else:
            print("A senha deve ter pelo menos 4 caracteres.")
    except ValueError:
        print("Por favor, digite um número válido.")
        
# Calcula a distribuição de caracteres
qtd_letras = tamanho_senha // 2
qtd_numeros = math.ceil(tamanho_senha * 0.3 )
qtd_especiais = tamanho_senha - (qtd_letras + qtd_numeros)

senha = []

def gerar_caracteres(quantidade, caracteres, eh_letra=False):
    """Gera caracteres aleatórios e adiciona à lista de senha"""
    for _ in range(quantidade):
        caractere = random.choice(caracteres)
        if eh_letra:
            
            caractere = caractere.upper() if random.randint(0, 1) else caractere
            senha.append(caractere)
            
            
gerar_caracteres(qtd_letras, letras, True)
gerar_caracteres(qtd_numeros, numeros)
gerar_caracteres(qtd_especiais, especiais)


random.shuffle(senha)
senha_gerada = ''.join(senha)


print("\nSenha gerada:", senha_gerada)
print(f"composição: {qtd_letras} letras, {qtd_numeros} numeros, {qtd_especiais} caracteres especiais")
    