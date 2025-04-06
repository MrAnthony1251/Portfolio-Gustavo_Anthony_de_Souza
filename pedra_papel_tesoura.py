import random

def jogar():
    usuario = input("Qual é sua escolha? 'p' para pedra, 'pa' para papel, 't' para tesoura \n")
    computador = random.choice(['p', 'pa', 't'])
    
    if usuario == computador:
        return 'é um empate'
    
    
    # pedra > tesoura, tesoura > papel, papel > pedra
    if is_win(usuario, computador):
        return "Você venceu"
    
    
    return "Você perdeu"


def is_win(Jogador, Oponente):
    # Retorno "TRUE" se o jogador vencer
    # pedra > tesoura, tesoura > papel, papel > pedra
    if (Jogador == 'p' and Oponente == 't') or (Jogador == 't' and Oponente == 'pa') \
        or (Jogador == 'pa' and Oponente == 'r'):
            return True
        
        
print(jogar())
    
