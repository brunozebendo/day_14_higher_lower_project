from art import logo
from game_data import data
import random
from replit import clear
#tem que apresentar duas opções randômicas, o usuário escolhe a ou b, o sistema compara o follower_count,
# se acertar, soma um aos pontos, e a opção derrotada vira a primeira, se errar, acaba o jogo,
# 'name': 'NBA', imprimir 'follower_count': 'description': 'country':

def get_random_account():
  return random.choice(data)
'''seleciona uma chaves do banco de dados (data)'''

def format_data(account):
  name = account["name"]
  descripition = account["descripition"]
  country = account["country"]
  return f"{name}, a {descripition}, from {country}"
'''a função transforma os dados em um formato imprimível, ele pega os dados do data,
 os guarda em outra variável e retorna uma string com essas variáveis'''

def check_answer(guess, a_followers, b_followers):
 if a_followers > b_followers:
  return guess == "a"
 else:
  return guess == "b"
'''checa se o número de seguidores contra a advinhação do usuário e retorna
 True se estiver certo ou False se errado, as variáveis vão ser estabelecidas mais a frente no código'''

def game():
 print(logo)
 score = 0
 game_should_continue = True
 account_a = get_random_account()
 account_b = get_random_account()
'''a função para chamar o jogo, os accounts chamam a função para selecionar randomicamente'''
game_should_continue = True
while game_should_continue:
  account_a = account_b
  account_b = get_random_account
'''essa função vai ser aplicada enquanto o jogo continuar e vai fazer a variável A receber B, e a variável b receber uma nova variável.'''
while account_a == account_b:
   account_b = get_random_account
'''função para evitar que as duas variáveis sejam iguais, ela está identada dentro da outra'''
print(f"compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B:{format_data(account_b)}.")
'''chamou a função que formata os dados para impressão e selecionou uma conta de cada vez'''

guess = input("Who has more more followers? Type 'A' or 'B':").lower()
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)
''' esse código estabelece que a variável a_follower_count recebe o account_a e b que são as variáveis de escolhas
 aleatórias para comparação e depois a variável is_correct chama a função check_answer. Prestar atenção que account
  é a variável para guardar a escolha randômica, já a variável follower_count serve para comparar o follower_count que 
  é chave que guarda o número de seguidores no data.'''
clear()
print(logo)
score = 0
if is_correct:
 score += 1
 print(f"You're right! Current score: {score}.")
else:
 game_should_continue = False
 print(f"Sorry, that's wrong. Final score: {score}")
'''se acertar, soma um ao score, se errar, acaba o jogo'''
game()