#Primeiro projeto criado de forma autônoma em Python!!!!

nome_cadastrado = str (input ('Seu primeiro nome: '))
sobrenome_cadastrado = str (input ('Seu sobrenome: '))
senha_cadastrado = str (input ('Cadastre uma senha: '))

print ('Usuário Cadastrado!')

print ('LOGIN')

nome = input ('Nome: ')
while nome != nome_cadastrado:
  print ('Usuário não identificado.')
  nome = input ('Nome: ')
  
senha = input ('Senha: ')
while senha != senha_cadastrado:
  print ('Senha incorreta, tente novamente. ')
  senha = input ('Senha: ')

print ('Bem vindo,', nome_cadastrado, sobrenome_cadastrado,'.')