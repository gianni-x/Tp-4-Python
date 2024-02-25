import unittest, filecmp
from dataset import DataSetInmobiliario
class TestDataSetInmobiliario(unittest.TestCase):
    
    '''Creamos los casos de test para cada funcion'''
    
    def setUp(self):
        '''Asignamos 3 archivos csv para testear, depto1 = sin departamentos, depto2 = 1 departamento, depto3 = 8 departamentos'''
        
        self.depto1:DataSetInmobiliario = DataSetInmobiliario('departamento_1.csv')
        self.depto2:DataSetInmobiliario = DataSetInmobiliario('departamento_2.csv')
        self.depto3:DataSetInmobiliario = DataSetInmobiliario('departamento_3.csv')   

  
    def test_tamano(self):
        ''' Cuenta la cantidad de departamentos en el dataset d'''
        
        self.assertEqual(self.depto1.tamano(),0)
        self.assertEqual(self.depto2.tamano(),1)
        self.assertEqual(self.depto3.tamano(),8)
        
        
    def test_barrios(self):
        ''' Devuelve el conjunto de barrios en el dataset d'''
        
        self.assertEqual(self.depto1.barrios(),  set())
        self.assertEqual(self.depto2.barrios(), {'ALMAGRO'})
        self.assertEqual(self.depto3.barrios(), {'ALMAGRO' , 'MONTSERRAT' , 'BALVANERA' , 'BELGRANO' , 'NUNEZ'})


    def test_oferta_por_barrio(self):
        ''' Devuelve el diccionario de barrios, con los ambientes pasados por parametro y su cantidad en cada barrio'''
        
        self.assertEqual(self.depto1.oferta_por_barrio(1),{})
        self.assertEqual(self.depto2.oferta_por_barrio(4),{'ALMAGRO':1})
        self.assertEqual(self.depto3.oferta_por_barrio(1),{'ALMAGRO':4 , 'MONTSERRAT':1 , 'BALVANERA':1 , 'BELGRANO':1 , 'NUNEZ': 0})
        
        
    def test_filtrar(self):
        ''' Modifica la lista de departamentos de forma que queden los departamentos filtrados pasados por parametro, precio minimo, precio maximo y conjunto de barrios '''
        
        depto1:DataSetInmobiliario()=DataSetInmobiliario('departamento_1.csv') 
        depto2:DataSetInmobiliario()=DataSetInmobiliario('departamento_2.csv')
        depto3:DataSetInmobiliario()=DataSetInmobiliario('departamento_3.csv')
        
        '''Primer filtrado para cada archivo'''      
        depto1.filtrar(54000,55000,{'ALMAGRO'})
        depto2.filtrar(54000,55000,{'ALMAGRO'})
        depto3.filtrar(50000,89000,{'ALMAGRO','NUNEZ','MONTSERRAT','BELGRANO'})

        '''Test primer filtrado'''
        self.assertEqual(depto1.tamano(),0)
        self.assertEqual(depto2.tamano(),1)
        self.assertEqual(depto3.tamano(),6)
        
        '''Segundo filtrado para cada archivo'''      
        depto1.filtrar(80000,90000,{'ALMAGRO'})
        depto2.filtrar(54900,56000,{'ALMAGRO'})
        depto3.filtrar(89000,89000,{'ALMAGRO','NUNEZ','BELGRANO'})
        
        '''Test segundo filtrado'''
        self.assertEqual(depto1.tamano(),0)
        self.assertEqual(depto2.tamano(),1)
        self.assertEqual(depto3.tamano(),1)
        

    def test_exportar(self):
        ''' Crea un archivo csv identico al pasado por parametro con el nombre de salida_archivo_csv'''
        
        ''' Somos conscientes de que filecmp.cmp no fue dado en clase, pero lo encontramos conveniente 
        para el caso ya que compara dos archivos evaluando que sean identicos y devolviendo un booleano'''
        
        self.depto4:DataSetInmobiliario = DataSetInmobiliario('departamento_3.csv')
        self.depto4.exportar('salida_archivo_csv.csv')
        self.assertTrue(filecmp.cmp('departamento_3.csv','salida_archivo_csv.csv'))
        
unittest.main()