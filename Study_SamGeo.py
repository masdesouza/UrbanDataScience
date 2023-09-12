'''
Vamos a biblioteca samgeo baseado em sua documentação:
https://samgeo.gishub.org/

Exemplo de segmentação de imagem:
https://samgeo.gishub.org/examples/segmentation.html
https://samgeo.gishub.org/examples/satellite

Exemplo de segmentação de apenas um tipo de elemento:
https://samgeo.gishub.org/examples/text_prompts

'''

#Instalação das bibliotecas necessárias
#!pip install segment-geospatial leafmap localtileserver --quiet

#Importando as bibliotecas necessárias
import os
import leafmap
from samgeo import SamGeo, tms_to_geotiff, get_basemaps

#definição da região da análise
#Cedro do estado de Pernambuco
bbox = [-39.00000000000001, -7.000000000000001, -38.00000000000001, -6.000000000000001]

#nome da imagem a ser gerada
image = "satellite.tif"

#download da imagem tif da área a se analisada
tms_to_geotiff(bbox=bbox, ouput=image, zoom=20, source="Satellite, overwrites=True")

#Inicialização do modelo de IA

sam = SamGeo (
    quitmodel_type= "vit_h",
    checkpoint = "sam_vit_h_4b8939.pth",
    sam_kwargs=None
)

#Representação da imagem
mask = "segment.tif"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

sam.generate(
        image, 
        mask,  batch=True, 
        foreground=True, 
        erosion_kernel=(3,3), 
        mask_multiplier=255
)

#Definição da aparência do vetor
style = {

    "color": "#3388ff",
    "weight": 2,
    "fillColor": "#7c4185",
    "fillOpacity": 0.5,
}

#geração do mapa interativo

m = leafmap.Map(center=[-25.37097303577983,-51.46310188374696], zoom=19)
m.add_basemap("SATELLITE")
m.add_vector(vector, layer_name="Vector", style=style)





