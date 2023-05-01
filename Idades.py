#criação da classe
class Idades: 
  
  def __init__(self, nome, sobrenome, idade): #criação do método construtor
    self.nome = nome                          #criação do argumento nome que serão instanciados ao objeto
    self.sobrenome = sobrenome                #criação do argumento sobrenome que serão instanciados ao objeto              
    self.idade = idade                        #criação do argumento idade que serão instanciados ao objeto     


  #criando uma função de apresentação                    
  def apresentacao(self):                    
    print(f'Olá, meu nome é {self.nome} {self.sobrenome} e tenho {self.idade}.')

  #criação da função de maior e de menor
  def maior_menor(self):
    if self.idade >= 18:
      print(f'{self.nome} é de maior, pois tem {self.idade}.')
      print('Acesso Liberado !')
    else:
      print(f'{self.nome} é de menor, e tem apenas {self.idade}.')
      print('Acesso Negado !')
