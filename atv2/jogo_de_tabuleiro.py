import random

class FilaCircular:
    """
    Implementa uma fila circular para representar as casas do tabuleiro.
    As casas são armazenadas em uma lista, e a rotação é feita de forma circular.
    """
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = list(range(1, tamanho + 1))
    
    def __getitem__(self, index):
        # Acessa a casa considerando a circularidade
        return self.fila[index % self.tamanho]
    
    def __str__(self):
        return " -> ".join(str(casa) for casa in self.fila)

def jogo_tabuleiro():
    print("Bem-vindo ao jogo do tabuleiro!")
    while True:
        try:
            num_casas = int(input("Digite o número de casas do tabuleiro: "))
            if num_casas < 2:
                print("O tabuleiro deve ter pelo menos 2 casas.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    tabuleiro = FilaCircular(num_casas)
    print("Tabuleiro:", tabuleiro)
    
    posicao_atual = 0  # Começamos na primeira casa (índice 0)
    
    while True:
        input("\nPressione Enter para rolar o dado...")
        dado = random.randint(1, 6)
        print(f"Você rolou: {dado}")
        
        # Calcula a nova posição
        nova_posicao = posicao_atual + dado
        
        # Se a nova posição for maior ou igual à última casa, posiciona o jogador na última casa
        if nova_posicao >= num_casas - 1:
            posicao_atual = num_casas - 1
            casa_atual = tabuleiro[posicao_atual]
            print(f"Você avançou para a casa {casa_atual}.")
        else:
            posicao_atual = nova_posicao
            casa_atual = tabuleiro[posicao_atual]
            print(f"Você avançou para a casa {casa_atual}.")

        # Se o jogador alcançar a última casa, realizar o teste final
        if posicao_atual == num_casas - 1:
            input("Você chegou na última casa! Pressione Enter para tentar vencer...")
            final_dado = random.randint(1, 6)
            print(f"Você rolou: {final_dado}")
            if final_dado > 4:
                print("Parabéns! Você rolou acima de 4 e venceu o jogo!")
                break
            else:
                print("Você não rolou mais que 4. Portanto, volta ao início!")
                posicao_atual = 0

if __name__ == '__main__':
    jogo_tabuleiro()
