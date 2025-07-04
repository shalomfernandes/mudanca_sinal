# Mudança de Sinal

Este é um simulador de semáforos que demonstra o funcionamento de um sistema de controle de tráfego em um cruzamento. O projeto foi desenvolvido em Python usando a biblioteca Pygame.

## Funcionalidades

- Simulação de um cruzamento com semáforos
- Controle de fluxo de carros em duas direções (vertical e horizontal)
- Sistema adaptativo que ajusta o tempo do semáforo baseado no tamanho das filas
- Interface gráfica interativa

## Requisitos

- Python 3.x
- Pygame
- Numpy (opcional)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/shalomfernandes/mudanca_sinal.git
cd mudanca_sinal
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

Execute o arquivo principal:
```bash
python main.py
```

### Controles
- Tecla 'V': Adiciona um carro na direção vertical
- Tecla 'H': Adiciona um carro na direção horizontal
- Fechar a janela para encerrar o programa

## Características do Sistema

- O semáforo mantém o sinal verde na direção atual se não houver carros na direção oposta
- Quando há carros em ambas as direções, o sistema alterna o sinal a cada 2 rodadas
- O tempo de verde é ajustado com base no tamanho da fila
- Interface mostra o tempo restante e número de carros em cada direção

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests ou reportando issues.
