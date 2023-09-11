import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

#desenho do fundo-figura de Recife
oeste, lest, norte, sul = -34.95, -34.85, -8.05, -8.15

#requisição dos dados de base do Open Street Map
buildings = ox.features_from_bbox(norte, sul, lest, oeste, tags={'building':True})

#Dataframe com os dados de base do Open Street Map
buildings

#desenho da geometia na tela
buildings.plot(figsize=[10,10], facecolor='gray',markersize=0)

#importação dos dados de vias, edificios e áreas de agua
roads = ox.features_from_bbox(norte, sul, lest, oeste, tags={'highway':True})
water = ox.features_from_bbox(norte, sul, lest, oeste, tags={'natural':'water'})


#desenho da figura com vias, edificios e áreas de agua
fig,ax = plt.subplots(figsize=[20,20])

water.plot(ax=ax, color='#DADADA', linewidth=0.5, markersize=0)
roads[ roads['highway'].isin(['motorway','primary','primary_link'])].plot(ax=ax, color='#FFFFFF', linewidth=2.5, markersize=0)
roads[ roads['highway'].isin(['secondary'])].plot(ax=ax, color="black", linewidth=1.5, markersize=0)
roads[ roads['highway'].isin(['tertiary','residencial'])].plot(ax=ax, color="black", linewidth=0.5, markersize=0)
buildings.plot(ax=ax, color='black', linewidth=0.5, markersize=0)




'''
#Definição do Local de plotagem
place_name = "Santo Amaro, Recife, Brazil"
graph = ox.graph_from_place(place_name)
#desenho do fundo-figura de Recife
fig, ax = ox.plot_graph(graph)

#desenho do fundo-figura de Recife com ruas
#fig, ax = ox.plot_graph(graph, save=True, file_format='svg')

#desenho do fundo-figura de Recife com ruas e edificios
#fig, ax = ox.plot_graph(graph, save=True, file_format='svg', show=False, close=True, filepath='figura.svg')



'''




