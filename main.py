from matplotlib import pyplot as plt
from statistics import mean
from mochila import Mochila_binaria

def ler_txt():
    with open('c.txt', 'r') as f:
        c = int(f.read())
    with open('p.txt', 'r') as f:
        # Qualidade 
        v = [int(line) for line in f.readlines() if line[:-1].isnumeric()]
    with open('w.txt', 'r') as f:
        p = [int(line) for line in f.readlines() if line[:-1].isnumeric()]
    return c,v,p

if __name__ == '__main__':

    eixo_x, media, porcentagem = [],[], 0.00
    # c = Capacidade mochila
    # v = Qualidade dos itens
    # p = Peso dos itens
    c,v,p = ler_txt()
    
    mochila = Mochila_binaria(v,p,c)
 
    # 3 for aninhados para variar os parametros
    for varia_porcentagem in range(3):
        porcentagem += 0.05
        for varia_geracoes in range(3):
            geracoes = 20
            if not varia_geracoes == 0: geracoes = 50 * varia_geracoes
            for varia_individuos in range(3):
                individuos = 20
                if not varia_individuos == 0: individuos = 50 * varia_individuos
                melhores = []
                # For para executar 10 cada geração, para evitar valores arbitrarios
                for _ in range(10):
                    mochila.gerar_populacao(individuos)
                    mochila.fitness()
                    # For pra executar as n gerações
                    for _ in range(geracoes):
                        mochila.pegar_melhor_individuo()
                        mochila.torneio()
                        mochila.mutacao(porcentagem)
                        mochila.populacao[-1] = mochila.melhor_individuo[0]
                        mochila.fitness()
                    melhores.append(mochila.melhor_individuo[1])

                eixo_x.append(f'{varia_porcentagem}{varia_geracoes}{varia_individuos}')
                # Media dos melhores de cada geração
                media.append(mean(melhores))

    # Gero os dados necessarios executa 10 vezes as gerações de cada parametros,
    #  pega o melhor de cada geração e salva.
    plt.plot(eixo_x, media,)
    plt.show()
