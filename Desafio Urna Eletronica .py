candidatos = {
"a" : {"votos": 0},
"b" : {"votos": 0},
"c" : {"votos": 0}
}
max_votos = 0
vencedor = ''
for candidato in candidatos:
      print(candidato)
while True:
    voto = input("Digite o voto (Ou sair para encerrar.): ").lower()
    if voto == 'sair':
      print('fim')
      for candidato, votos in candidatos.items():
       print(f"{candidato}: {votos['votos']}")
      break
    elif voto == voto:
      print(f"Voto registrado para Candidato {voto}.")
    if voto in candidatos:
     candidatos[voto]['votos'] += 1
    elif voto != candidatos:
      print("Candidato não encontrado, verifique o nome e tente novamente..") 
total_votos = sum(candidato['votos'] for candidato in candidatos.values())
for candidato, valor in candidatos.items():
    votos = valor['votos']
    porcentagem = (votos / total_votos)
    print(f"{candidato} : {porcentagem:.2f} %")
for candidato in candidatos:
 voto = candidatos[candidato]["votos"]
if voto > max_votos:
    max_votos = voto
    vencedor = candidato
    print(f"O vencedor da eleição é: {vencedor}")






    



  
    
          


     
    
        
    
    
      

   # for candidato, votos in candidatos.items():   #codigo que mostra o total dos votos.
    #  print(f"{candidato}: {votos['votos']}")     
    
        

       
        
    
