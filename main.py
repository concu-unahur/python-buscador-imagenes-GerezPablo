import logging
from api import PixabayAPI
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


carpeta_imagenes = './imagenes'
#query = 'computadoras'
query = input('Que imagenes desea buscar??\n')
cant = int(input(f'Cuantas imagenes de {query} quiere descargar??\n'))
api = PixabayAPI('15310263-3c077b8973067ba768708060a', carpeta_imagenes)
urls = api.buscar_imagenes(query, cant)
logging.info(f'Buscando imagenes de {query}...')

for u in urls:
  t = threading.Thread(target = api.descargar_imagen, args=[u])
  logging.info(f'Descargando {u}')
  t.start()

