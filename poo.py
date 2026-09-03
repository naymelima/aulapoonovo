def cachorro():
    
    dog = input('Digite o nome do seu animal: ')
    print('O nome do seu animal é: ' + dog)

    sexo = input('Qual o sexo do seu animal: Macho ou Fêmea: ')
    if sexo == 'Macho':
       print('Seu animal é macho')
    elif sexo == 'Fêmea':
       print('Seu animal é fêmea')

    race = input('Digite a raça do seu animal: ')
    print('Seu animal é da raça: ' + race)

    castro = input('Seu animal é castrado? Sim ou Não: ')
    if castro == 'Sim':
        print('Seu animal é castrado.')
    else:
        print('Seu animal não é castrado.')

    consulta = float(input('Digite a data para consulta do mês de Agosto do seu animal: '))
    if consulta >= 1.08 and consulta <= 31.08:
     print('Consulta marcada.')
    else:
     print('Você está em outro mês.')

def gato():

   cat = input('Digite o nome do seu animal: ')
   print(f'O nome do seu animal é: {cat}')

   sexo = input('Qual o sexo do seu animal: Macho ou Fêmea: ')
   if sexo == 'Macho':
      print('Seu animal é macho')
   elif sexo == 'Fêmea':
      print('Seu animal é fêmea')
   race = input('Digite a raça do seu animal: ')
   print('Seu animal é da raça: ' + race)
   
   castro = input('Seu animal é castrado? Sim ou Não: ')
   if castro == 'Sim':
      print('Seu animal é castrado.')
   else:
           print('Seu animal não é castrado.')
   
   consulta = float(input('Digite a data para consulta do mês de Agosto do seu animal: '))
   if consulta >= 1.08 and consulta <= 31.08:
        print('Consulta marcada.')
   else:
        print('Você está em outro mês.')






        
    

