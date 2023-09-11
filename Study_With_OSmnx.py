import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

#desenho do fundo-figura de Recife
oeste, lest, norte, sul = -34.95, -34.85, -8.05, -8.15

#requisição dos dados de base do Open Street Map
buildings = ox.features_from_bbox(norte, sul, lest, oeste, tags={'building':True})

#desenho da geometia na tela
buildings.plot(figsize=[10,10], facecolor='gray',markersize=0)



'''
#Definição do Local de plotagem
place_name = "Recife, Brazil"
graph = ox.graph_from_place(place_name)
fig, ax = ox.plot_graph(graph)

#desenho do fundo-figura de Recife com ruas
fig, ax = ox.plot_graph(graph, save=True, file_format='svg')

#desenho do fundo-figura de Recife com ruas e edificios
fig, ax = ox.plot_graph(graph, save=True, file_format='svg', show=False, close=True, filepath='figura.svg')
'''




