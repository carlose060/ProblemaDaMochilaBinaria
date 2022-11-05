from random import randint, random


class Mochila_binaria:
    def __init__(self, utilidade, peso, capacidade = 165):
        self.capacidade_max = capacidade
        self.utilidade = utilidade
        self.peso = peso
        self.populacao = []
        self.list_fitness = []
        self.melhor_individuo = None
    
    def gerar_populacao(self, individuos):
        self.populacao = [[randint(0,1) for _ in range(10)] for _ in range(individuos)]

    def pegar_melhor_individuo(self):  
        self.melhor_individuo = sorted(zip(self.populacao,self.list_fitness),key=lambda x:x[1])[-1]
    
    def fitness(self):
        self.list_fitness = []
        for lista in self.populacao:
            peso_total = 0
            qualidade_total = 0
            for tupla in zip(lista, self.peso, self.utilidade):
                peso_total += (tupla[0] * tupla[1])
                qualidade_total += (tupla[0] * tupla[2])
            if peso_total <= self.capacidade_max:
                fit = qualidade_total
            else:
                fit = 0
                somatorio_p = 0
                somatorio_v = 0
                for tupla in zip(lista, self.peso, self.utilidade):
                    somatorio_p += (tupla[0]*tupla[1])
                    somatorio_v += (tupla[0]*tupla[2])
                fit = somatorio_v - (somatorio_v * (somatorio_p - self.capacidade_max)) 
            self.list_fitness.append(fit)
        
    
    def torneio(self):
        novo_s = []
        dict_fitness = dict(enumerate(self.list_fitness))
        
        for _ in range(int(len(self.populacao)/2)):
            idx = [randint(0,len(self.populacao)-1) for _ in range(4)]

            if dict_fitness[idx[0]] > dict_fitness[idx[1]]:
                lista1 = self.populacao[idx[0]]
            else:
                lista1 = self.populacao[idx[0]]

            if dict_fitness[idx[2]] > dict_fitness[idx[3]]:
                lista2 = self.populacao[idx[2]]
            else:
                lista2 = self.populacao[idx[3]]
            x,y = self.cruzamento((lista1,lista2))
            novo_s.append(x)
            novo_s.append(y)
        self.populacao = novo_s
        
    
    def cruzamento(self,dupla):

        tamanho_cruzamento = randint(1,8) * (-1)
        x, y = dupla
        aux = x[tamanho_cruzamento:]
        new_x = x[:tamanho_cruzamento] + y[tamanho_cruzamento:]
        new_y = y[:tamanho_cruzamento] + aux
        return (new_x, new_y)
    
    def mutacao(self, porcentagem=0.1):

        for l in self.populacao:
            for idx in range(len(l)):
                if not random() > porcentagem:
                    if l[idx] == 1: l[idx] = 0 
                    else: l[idx] = 1
