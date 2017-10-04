import unittest
from edad import Edad

class EdadTest(unittest.TestCase):

	def setUp(self):
		self.edad = Edad()

	#INICIA TEST EVALUAR EDAD
	def test_evaluar_2_negativo_igual_noexistes(self):
		self.edad.evaluar_edad(-2)
		self.assertEqual(self.edad.obtener_evaluacion(), 'No existes')

	def test_evaluar_0_igual_eresninio(self):
		self.edad.evaluar_edad(0)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres infante')

	def test_evaluar_10_igual_eresninio(self):
		self.edad.evaluar_edad(10)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres infante')

	def test_evaluar_13_igual_eresadolescente(self):
		self.edad.evaluar_edad(13)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adolescente')

	def test_evaluar_15_igual_eresadolescente(self):
		self.edad.evaluar_edad(15)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adolescente')

	def test_evaluar_18_igual_eresadulto(self):
		self.edad.evaluar_edad(18)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adulto')

	def test_evaluar_33_igual_eresadulto(self):
		self.edad.evaluar_edad(33)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adulto')

	def test_evaluar_65_igual_eresadultomayor(self):
		self.edad.evaluar_edad(65)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adulto mayor')

	def test_evaluar_93_igual_eresadultomayor(self):
		self.edad.evaluar_edad(93)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres adulto mayor')

	def test_evaluar_120_igual_eresmummra(self):
		self.edad.evaluar_edad(120)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres Mumm-Ra')

	def test_evaluar_500_igual_eresmummra(self):
		self.edad.evaluar_edad(500)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres Mumm-Ra')

	def test_evaluar_1000_igual_eresmummra(self):
		self.edad.evaluar_edad(1000)
		self.assertEqual(self.edad.obtener_evaluacion(), 'Eres Mumm-Ra')

	def test_evaluar_holamundo_igual_datosincorrectos(self):
		self.edad.evaluar_edad('Hola Mundo')
		self.assertEqual(self.edad.obtener_evaluacion(), 'Datos Incorrectos')

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
