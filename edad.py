
class Edad(object):

	def __init__(self):
		self.edad = 0
		self.evaluacion = ''

	def obtener_evaluacion(self):
		return self.evaluacion

	def evaluar_edad(self, edad):
		try:
			if edad < 0:
				self.evaluacion = 'No existes'
			elif edad < 13:
				self.evaluacion = u'Eres niño'
			elif edad < 18:
				self.evaluacion = 'Eres adolescente'
			elif edad < 65:
				self.evaluacion = 'Eres adulto'
			elif edad < 120:
				self.evaluacion = 'Eres adulto mayor'
			else:
				self.evaluacion = 'Eres Mumm-Ra'	
		except:
			self.evaluacion = 'Datos Incorrectos'
