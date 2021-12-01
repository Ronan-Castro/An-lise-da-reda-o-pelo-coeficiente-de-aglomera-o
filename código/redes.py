import nltk
import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
from string import punctuation
from nltk.tokenize import word_tokenize
#nltk.download('stopwords')
#nltk.download('punkt')

G = nx.Graph()

stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))

texto = open('redacao0.txt','r')

texto = texto.read()

palavras = word_tokenize(texto.lower())

pal = [palavra for palavra in palavras if palavra not in stopwords]



length = len(pal)
print(length)
for x in range(length):
	G.add_node(pal[x])
		


for x in range(length-1):
	if(pal[x] == pal[x+1]):
		continue
	else:
		if((G.has_edge(pal[x], pal[x+1])) or (G.has_edge(pal[x+1], pal[x])) ):
			G[pal[x]][pal[x+1]]['weight'] = G[pal[x]][pal[x+1]]['weight'] + 1
			
		else:
			G.add_edge(pal[x],pal[x+1], weight = 1)	
			
			

lista = list(find_cliques(G))


peso_cliques = []
somatorio = 0
for sasa in range(len(lista)):

	if(len(lista[sasa]) > 2):
	
		soma_atual = 0
		
		for j in range(len(lista[sasa])):
		
			for k in list(range(j+1, len(lista[sasa]), 1)):
			
				soma_atual += (G[lista[sasa][j]][lista[sasa][k]]['weight'])
				
		peso_cliques.append(soma_atual)
		somatorio += soma_atual
		
peso = 0
for sasa in range(len(lista)):

	if(len(lista[sasa]) > 2):
		print("\nPalavras dos nós que compõem um clique:",lista[sasa], "\n\nSomatório do peso deste clique :", peso_cliques[peso])
		peso += 1
		
		
if(len(peso_cliques) > 0):			
	#print("\ntotal de cliques", len(peso_cliques))
	print("\nO coeficiente de aglomeração da rede inteira é:", ((somatorio/len(peso_cliques)/G.number_of_nodes())))	
	
else:	
	print("\nO coeficiente de aglomeração da rede inteira é nulo, pois não foram encontrados cliques")
	
	
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
                 
pos = nx.spring_layout(G)

plt.figure(3, figsize = (12,12))

nx.draw(G, pos, with_labels = True, node_size = 700, font_size = 8)

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)


plt.show()





