class Departamento:
    def __init__(self, direc:str, props:int, metroscuadrados:float, preciosendolares:int, precioenpesos:int, m2endolares:int, m2enpesos:int, amb:int, coti:int, tri:str, barr:str, comu:int):
      ''' 
      Inicializa un Departamento con direccion = direc, metros_cuadrados = metroscuadrados, 
      precio_en_dolares = preciosendolares, precio_en_pesos = precioenpesos, m2_en_dolares = m2endolares, 
      m2_en_pesos = m2enpesos, ambientes = amb, barrio = barr.
      '''
      
      self.direccion:str          = direc
      self.propiedads:int         = props
      self.metros_cuadrados:float = (preciosendolares/m2endolares)
      self.precio_en_dolares:int  = preciosendolares
      self.precio_en_pesos:int    = precioenpesos
      self.m2_en_dolares:int      = m2endolares
      self.m2_en_pesos:int        = m2enpesos
      self.ambientes:int          = amb
      self.cotizacion:int         = coti
      self.trimestre:str          = tri
      self.barrio:str             = barr
      self.comunas:int            = comu

    def __repr__(self) -> str:
      '''
      Requiere: Un departamento d
      Devuelve: Devuelve su superficie en metros cuadrados, redondeada, el string M2, una arroba y su barrio
      '''
      return ("<" + str(round(self.metros_cuadrados)) + "M2@" + str(self.barrio) + ">")
      



    def __lt__ ( self , other ) -> bool :
      ''' Devuelve True si precio_en_dolares < other.precio_en_dolares; False en caso     
      contrario. Es necesario para poder aplicar el metodo sort a nuestra lista en __init__ del dataset.
      '''
      return self.precio_en_dolares < other.precio_en_dolares
