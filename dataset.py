import csv
from typing import TextIO, Dict, List, Set
from departamento import Departamento

class DataSetInmobiliario:
    def __init__(self, archivo_csv:str): 
      ''' 
      Inicializa el DataSetInmobiliario, cargando los datos:
      archivo_csv: CSV con los departamentos;
      '''
      self.departamentolista:List[Departamento] = []                                                              # O(1)
      self.departamentosinsort:List[Departamento] = []                                                            # O(1)
      f:TextIO = open(archivo_csv, 'r', encoding = 'utf-8')                                                       # O(1)
      
      for linea in csv.DictReader(f):                                                                             # O(1)
        Direccion:str           = linea['Direccion']                                                              # O(1)
        PropiedadS:str          = linea['PropiedadS']                                                             # O(1)
        Metroscuadrados:float   = float(int(linea['Dolares'])/int(linea['DolaresM2']))                            # O(1)
        Dolares:int             = int(linea['Dolares'])                                                           # O(1)
        Pesos:int               = int(linea['Pesos'])                                                             # O(1)
        DolaresM2:int           = int(linea['DolaresM2'])                                                         # O(1)
        PesosM2:int             = int(linea['PesosM2'])                                                           # O(1)
        Ambientes:int           = int(linea['Ambientes'])                                                         # O(1)
        Cotizacion:str          = linea['Cotizacion']                                                             # O(1)
        Trimestre:str           = linea['Trimestre']                                                              # O(1)   
        Barrio:str              = linea['Barrio']                                                                 # O(1)
        Comunas:str             = linea['Comunas']                                                                # O(1)

        
        depto:Departamento = Departamento (Direccion, PropiedadS, Metroscuadrados, 
                                           Dolares, Pesos, DolaresM2, PesosM2, Ambientes, 
                                           Cotizacion, Trimestre, Barrio, Comunas)
        self.departamentolista.append(depto)                                                                      # O(1)
        self.departamentolista.sort()                                                                             # O(A*log(A))
        self.departamentosinsort.append(depto)                                                                    # O(1)                                                                    
        
      f.close()                                                                                                   # O(1)
      
    def tamano(self) -> int:# O(1)
      '''
      Requiere: Nada
      Devuelve: La cantidad de departamentos en el dataset d 
      '''
      return len(self.departamentolista)                                                                          # O(1)
    
    
    def barrios(self) -> Set:# O(N)
        '''
        Requiere: Nada
        Devuelve: Devuelve el conjunto de todos los barrios existentes en el dataset d.
        '''
        conjunto_de_barrios:Set[str] = set()                                                                     # O(1)
        for depto in self.departamentolista:                                                                     # O(N)
            conjunto_de_barrios.add(depto.barrio)                                                                # O(1)
                                                               
        return conjunto_de_barrios                                                                               # O(1)

    def deptos_del_barrio(self, barrio:str) -> List[Departamento]:# O(N)
      '''
      Requiere: Nada
      Devuelve: Una lista con los departamentos en el dataset d que estan en el barrio indicado, ordenados por 
      precio (en dolares) de menor a mayor.
      '''
      vr:List[Departamento] = []                                                                                # O(1)
      for ind in self.departamentolista:                                                                        # O(N)
        if ind.barrio == barrio:                                                                                # O(1)
          vr.append(ind)                                                                                        # O(1)
                                                                                       
      return vr                                                                                                 # O(1)


    def oferta_por_barrio(self, ambientes:int) -> Dict[str,int]:# O(N*B)
      '''
      Requiere: ambientes > 0
      Devuelve: Un diccionario que indica la cantidad de departamentos, con los ambientes indicados, en venta, en 
      cada barrio.
      '''
      oferta_por_barrio_dict: Dict[str, int] = {}                                                               # O(1)
      for depto in self.departamentolista:                                                                      # O(N)
          barrio:str = depto.barrio                                                                                 # O(1)                                          
          if depto.ambientes == ambientes:                                                                      # O(1)                                    
                                 
              if barrio in oferta_por_barrio_dict:                                                              # O(B)                                   
                  oferta_por_barrio_dict[barrio] = oferta_por_barrio_dict[barrio] + 1                           # O(1) 
                  
              else:                                                                                             # O(1)           
                  oferta_por_barrio_dict[barrio] = 1                                                            # O(1)
                                                             
          elif depto.ambientes != ambientes:                                                                    # O(1)
                  oferta_por_barrio_dict[barrio] = 0                                                            # O(1)
                  
      return oferta_por_barrio_dict                                                                             # O(1)                                  
  
    
    def filtrar(self, prec_min:int, prec_max:int, conj_barrios:Set[str]):# O(N*B)
        '''
        Requiere: Precio prec_minimo >= 0, prec_max >= 0 y los nombres de barrios deseados.
        Devuelve: Nada
        Modifica: El dataset d, dejando en el mismo únicamente departamentos que se encuentren en el rango de 
        precio indicado (entre prec_min inclusive y prec_max inclusive) y en los barrios indicados.
        '''
        nuevalista:List[Departamento] = []                                                                     # O(1)
        for depto in self.departamentolista:                                                                    # O(N)
            if prec_min <= depto.precio_en_dolares and depto.precio_en_dolares <= prec_max:                     # O(1)
               if depto.barrio in conj_barrios:                                                                 # O(B)
                   nuevalista.append(depto)                                                                     # O(1)
                   
        self.departamentolista = nuevalista                                                                     # O(1)


    def exportar(self, archivo_csv:str): # O(N)
      '''
      Requiere: Nada
      Devuelve: Un nuevo archivo.csv, con el nombre especificado en el parametro de 'archivo_csv', que es igual al 
      archivo_csv original, el cual contiene los departamentos del dataset d.
      '''
      f:TextIO = open (archivo_csv, 'w', encoding = 'utf-8')                                                    # O(1) 
      if len(self.departamentosinsort) == 0:                                                                    # O(1)
          f.write("Direccion,PropiedadS,Dolares,Pesos,DolaresM2,PesosM2,Ambientes,Cotizacion,Trimestre,Barrio,Comunas")
      
      else:                                                                                                     # O(1)
          f.write("Direccion,PropiedadS,Dolares,Pesos,DolaresM2,PesosM2,Ambientes,Cotizacion,Trimestre,Barrio,Comunas" + '\n')
          for depto in self.departamentosinsort:                                                                # O(N)
            
            if depto == self.departamentosinsort[-1]:                                                           # O(1)
                f.write( str(depto.direccion) + ',' + str(depto.propiedads) + ',' 
                        + str(depto.precio_en_dolares) + ',' + str(depto.precio_en_pesos) + ','
                        + str(depto.m2_en_dolares) + ',' + str(depto.m2_en_pesos) + ',' + str(depto.ambientes) 
                        + ',' + str(depto.cotizacion) + ',' + str(depto.trimestre) + ','+ str(depto.barrio) + ',' 
                        + str(depto.comunas))
                
            else:                                                                                               # O(1)                              
                f.write( str(depto.direccion) + ',' + str(depto.propiedads) + ',' 
                        + str(depto.precio_en_dolares) + ',' + str(depto.precio_en_pesos) + ','
                        + str(depto.m2_en_dolares) + ',' + str(depto.m2_en_pesos) + ',' + str(depto.ambientes) 
                        + ',' + str(depto.cotizacion) + ',' + str(depto.trimestre) + ','+ str(depto.barrio) + ',' 
                        + str(depto.comunas) + '\n')
          f.close()                                                                                             # O(1)          
          
