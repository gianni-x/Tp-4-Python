import unittest

# Importamos el codigo a testear.
from departamento import Departamento

####################################################################

class TestDepartamento(unittest.TestCase):
    def setUp(self):            #Direccion,PropiedadS, Dolares,Pesos,DolaresM2,PesosM2,Ambientes,Cotizacion,Trimestre,Barrio,Comunas
        self.d1 = Departamento('Pje Cnel J F Bogado 4561', 17 , 17.002167853824712 , 54900 , 3513600 , 3229 , 206682 , 1 , 64 ,'SEGUNDO' ,'ALMAGRO'   , 5 ) 
        self.d2 = Departamento('Capital 0'               , 26 , 21.997206703910614 , 63000 , 4032000 , 2864 , 183273 , 1 , 64 ,'SEGUNDO' ,'ALMAGRO'   , 5 )
        self.d3 = Departamento('COLOMBRES 43'            , 22 , 21.998166819431713 , 48000 , 3072000 , 2182 , 139636 , 1 , 64 ,'SEGUNDO' ,'ALMAGRO'   , 5 )
        self.d4 = Departamento('Rawson 200 0'            , 22 , 22.000687521485048 , 64000 , 4096000 , 2909 , 186182 , 1 , 64 ,'SEGUNDO' ,'ALMAGRO'   , 5 )
        self.d5 = Departamento('Mexico 1800'             , 27 , 27.003098716246125 , 61000 , 3904000 , 2259 , 144593 , 1 , 64 ,'SEGUNDO' ,'MONTSERRAT', 1 )
        self.d6 = Departamento('AVDA. INDEPENDENCIA 2000', 31 , 28.997867803837952 , 68000 , 4352000 , 2345 , 150069 , 1 , 64 ,'SEGUNDO' ,'BALVANERA' , 3 )
        self.d7 = Departamento('Mendoza 1700'            , 28 , 24.002157497303127 , 89000 , 5696000 , 3708 , 237333 , 1 , 64 ,'SEGUNDO' , 'BELGRANO' , 13)

    def test_direccion(self):
        self.assertAlmostEqual(self.d1.direccion, 'Pje Cnel J F Bogado 4561' )
        self.assertAlmostEqual(self.d2.direccion, 'Capital 0'                )
        self.assertAlmostEqual(self.d3.direccion, 'COLOMBRES 43'             )
        self.assertAlmostEqual(self.d4.direccion, 'Rawson 200 0'             )
        self.assertAlmostEqual(self.d5.direccion, 'Mexico 1800'              )
        self.assertAlmostEqual(self.d6.direccion, 'AVDA. INDEPENDENCIA 2000' )
        self.assertAlmostEqual(self.d7.direccion, 'Mendoza 1700'             )
        
    def test_propiedads(self):
        self.assertAlmostEqual(self.d1.propiedads, 17)
        self.assertAlmostEqual(self.d2.propiedads, 26)
        self.assertAlmostEqual(self.d3.propiedads, 22)
        self.assertAlmostEqual(self.d4.propiedads, 22)
        self.assertAlmostEqual(self.d5.propiedads, 27)
        self.assertAlmostEqual(self.d6.propiedads, 31)
        self.assertAlmostEqual(self.d7.propiedads, 28)       
        
    def test_metros_cuadrados(self):
        self.assertAlmostEqual(self.d1.metros_cuadrados, 17.002167853824712 )
        self.assertAlmostEqual(self.d2.metros_cuadrados, 21.997206703910614 )
        self.assertAlmostEqual(self.d3.metros_cuadrados, 21.998166819431713 )
        self.assertAlmostEqual(self.d4.metros_cuadrados, 22.000687521485048 )
        self.assertAlmostEqual(self.d5.metros_cuadrados, 27.003098716246125 )
        self.assertAlmostEqual(self.d6.metros_cuadrados, 28.997867803837952 )
        self.assertAlmostEqual(self.d7.metros_cuadrados, 24.002157497303127 )
        
    def test_precio_en_dolares(self):
        self.assertEqual(self.d1.precio_en_dolares, 54900 )
        self.assertEqual(self.d2.precio_en_dolares, 63000 )
        self.assertEqual(self.d3.precio_en_dolares, 48000 )
        self.assertEqual(self.d4.precio_en_dolares, 64000 )
        self.assertEqual(self.d5.precio_en_dolares, 61000 )
        self.assertEqual(self.d6.precio_en_dolares, 68000 )
        self.assertEqual(self.d7.precio_en_dolares, 89000 )
        
    def test_precio_en_pesos(self):
        self.assertEqual(self.d1.precio_en_pesos, 3513600 )
        self.assertEqual(self.d2.precio_en_pesos, 4032000 )
        self.assertEqual(self.d3.precio_en_pesos, 3072000 )
        self.assertEqual(self.d4.precio_en_pesos, 4096000 )
        self.assertEqual(self.d5.precio_en_pesos, 3904000 )
        self.assertEqual(self.d6.precio_en_pesos, 4352000 )
        self.assertEqual(self.d7.precio_en_pesos, 5696000 )

    def test_m2_en_dolares(self):
        self.assertEqual(self.d1.m2_en_dolares, 3229 )
        self.assertEqual(self.d2.m2_en_dolares, 2864 )
        self.assertEqual(self.d3.m2_en_dolares, 2182 )
        self.assertEqual(self.d4.m2_en_dolares, 2909 )
        self.assertEqual(self.d5.m2_en_dolares, 2259 )
        self.assertEqual(self.d6.m2_en_dolares, 2345 )
        self.assertEqual(self.d7.m2_en_dolares, 3708 )
        
    def test_m2_en_pesos(self):
        self.assertEqual(self.d1.m2_en_pesos, 206682 )
        self.assertEqual(self.d2.m2_en_pesos, 183273 )
        self.assertEqual(self.d3.m2_en_pesos, 139636 )
        self.assertEqual(self.d4.m2_en_pesos, 186182 )
        self.assertEqual(self.d5.m2_en_pesos, 144593 )
        self.assertEqual(self.d6.m2_en_pesos, 150069 )
        self.assertEqual(self.d7.m2_en_pesos, 237333 )

    def test_ambientes(self):
        self.assertEqual(self.d1.ambientes, 1 )
        self.assertEqual(self.d2.ambientes, 1 )
        self.assertEqual(self.d3.ambientes, 1 )
        self.assertEqual(self.d4.ambientes, 1 )
        self.assertEqual(self.d5.ambientes, 1 )
        self.assertEqual(self.d6.ambientes, 1 )
        self.assertEqual(self.d7.ambientes, 1 )  
        
    def test_cotizacion(self):
        self.assertAlmostEqual(self.d1.cotizacion, 64)
        self.assertAlmostEqual(self.d2.cotizacion, 64)
        self.assertAlmostEqual(self.d3.cotizacion, 64)
        self.assertAlmostEqual(self.d4.cotizacion, 64)
        self.assertAlmostEqual(self.d5.cotizacion, 64)
        self.assertAlmostEqual(self.d6.cotizacion, 64)
        self.assertAlmostEqual(self.d7.cotizacion, 64)    
        
    def test_trimestre(self):
        self.assertAlmostEqual(self.d1.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d2.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d3.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d4.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d5.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d6.trimestre, 'SEGUNDO')
        self.assertAlmostEqual(self.d7.trimestre, 'SEGUNDO')    

    def test_barrio(self):
        self.assertEqual(self.d1.barrio, 'ALMAGRO'    )
        self.assertEqual(self.d2.barrio, 'ALMAGRO'    )
        self.assertEqual(self.d3.barrio, 'ALMAGRO'    )
        self.assertEqual(self.d4.barrio, 'ALMAGRO'    )
        self.assertEqual(self.d5.barrio, 'MONTSERRAT' )
        self.assertEqual(self.d6.barrio, 'BALVANERA'  )
        self.assertEqual(self.d7.barrio, 'BELGRANO'   )

    def test_comunas(self):
        self.assertAlmostEqual(self.d1.comunas, 5 )
        self.assertAlmostEqual(self.d2.comunas, 5 )
        self.assertAlmostEqual(self.d3.comunas, 5 )
        self.assertAlmostEqual(self.d4.comunas, 5 )
        self.assertAlmostEqual(self.d5.comunas, 1 )
        self.assertAlmostEqual(self.d6.comunas, 3 )
        self.assertAlmostEqual(self.d7.comunas, 13)
        
unittest.main()
    
