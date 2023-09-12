'''
Google Open Buildings: https://sites.google.com/corp/view/open-buildings/home

O código abaixo foi elaborado a partir do seguinte Colab disponibilidado pelo Google:

https://colab.research.google.com/github/google-research/google-research/blob/master/building_detection/open_buildings_download_region_polygons.ipynb


https://github.com/google-research/google-research/blob/master/building_detection/open_buildings_spatial_analysis_examples.ipynb

'''
#importando da biblioteca necessárias

import functools
import glob
import gzip
import multiprocessing
import os
import shutil
import tempfile
from typing import List, Tuple, Optional
import geopandas as gpd
from IPython import display
import pandas as pd
import s2geometry as s2
import shapely
import tensorflow as tf
import tqdm.notebook







