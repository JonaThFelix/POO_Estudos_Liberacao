from Idades import Idades

#Criação dos objetos e atribuição dos argumentos aos mesmos
#Observa-se que os objetos agora estão 'atrelados' a classe Idades, portanto puxara os argumentos definidos no construtor

pessoa1 = Idades('Jonathan', 'Felix', 18)
pessoa2 = Idades('Gabriel', 'Ferreira',12)
pessoa3 = Idades('Maria','Carmelita',33)

#Execução da funçao apresentação
pessoa1.apresentacao()
pessoa2.apresentacao()
pessoa3.apresentacao()

print('\n')

#Execução das liberação
pessoa1.maior_menor()
pessoa2.maior_menor()
pessoa3.maior_menor()
