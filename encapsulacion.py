# principio de encapsulacion

class Animal(object):

	def tipo(self):
		return self.tipo
	
	def es_veloz(self):
		return self.es_veloz

	def __init__(self):
		print 'fui creado'
		self.tipo = 'Animalia'

		#atributo privado
		self.__es_veloz = True

leon = Animal()
leon.es_veloz = False

print leon.es_veloz

