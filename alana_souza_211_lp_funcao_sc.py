# -*- coding: utf-8 -*-
"""Alana Souza - 211_LP_Funcao_sc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r94Su4vUWGJSQDi2Gga4mgx9JYH8uv_S

### 1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.
"""

def multiplicar(numero):
    r = numero * 2
    print('O resultado de',numero,'* 2 =',r)
def main():
    n = int (input('Informe um valor na main:   '))
    multiplicar(n)
main()

"""### 2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado."""

def subtrair(n1,n2):
    st = n1 - n2
    print('Resultado:',st)
def main():
    n1 = float (input('Insira um numero:    '))
    n2 = float (input('Insira outro numero: '))
    subtrair(n1,n2)
main()

"""### 3. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.

"""

def nota(media):
    p1 = float (input('Digite a nota da p1: '))
    p2 = float (input('Digite a nota da p2: '))
    mediaA = (p1+p2)/2
    print('Media do aluno:',mediaA)

def aprova(p1,p2):
    nota('mediaA')
    while mediaA >= 6:
        print('Aprovado!')
    else:
        print('Reprovado!')
        
def main():
    aprova(p1,p2)
    nota(mediaA)
main()

"""### 4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%."""

def valor(novoValor):
    reajuste = preco * 9 / 100
    novoPreco = reajuste + preco
    print('O novo preço é de',novoPreco)
def main():
    preco = float (input('Insira o preço do produto:    '))
    valor(novoPreco)
main()

"""### 5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem lida."""

def valor(novoValor):
    reajuste = preco * porcentagem / 100
    novoPreco = reajuste + preco
    print('O novo preço é de',novoPreco)
def main():
    preco = float (input('Insira o preço do produto:    '))
    porcentagem = float (input('Insira o percentual de aumento sob o preço do produto:  '))
    valor(novoPreco)
main()

"""### 6. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado.
    Exemplo:
        a = 2
        b = 8
        // 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
        r = 35
"""

def soma(acumulo):
    sum = 0
    if (a > 0 and b > 0) and a <= b:
        for a in range(a,b+1):
            sum = sum + a
    print('Result: ',sum)
def main():
    a = int (input('Type a value:   '))
    b = int (input('Type an another value:  '))
    soma(sum)
main()

"""### 7. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar."""

def recebe_numero():
    numero = float (input('Informe um valor:    '))
    def decide(imparoupar):
    if (numero % 2 == 0):
        return "Par"
    else:
        return "Ímpar"
    decide("imparoupar")
def main():
    recebe_numero()
main()

"""### 8. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário."""

def tabuada(valor):
    aux = 0  
    print('*' * 18)  
    print('Tabuada de {}'.format(valor))  
    print('*' * 18)  
    while (aux <= 10):  
        print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))  
        aux = aux + 1
def main():
    valor = int (input('Entre com um número para saber a tabuada: '))  
    tabuada(aux)
main()

"""### 9. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta."""

def main(valorAna):
    nome = str (input('Digite um nome:  '))
    if nome == "Ana":
        print(True)
    else:
        print(False)
main('valorAna')

"""### 10. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras **a** tem numa frase."""

def frase(a)
    a = frase.count("a")
    print(a)
def main():
    frase = str (input('Digite uma frase: '))
    frase(a)
main()