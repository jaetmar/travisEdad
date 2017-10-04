Feature: Edad de un individuo
	Como usuario del sistema edad
	deseo realizar una evaluación de la edad
	para obtener una evaluación de su vejez


	Scenario: Edad de -2
		Dado que la edad del individuo es "-2"
		cuando realizo la operación
		entonces obtengo que el individuo "No existe"

	Scenario: Edad de 12
		Dado que la edad del individuo es "12"
		cuando realizo la operación
		entonces obtengo que el individuo "Eres infante"

	Scenario: Edad de 17
		Dado que la edad del individuo es "17"
		cuando realizo la operación
		entonces obtengo que el individuo "Eres adolescente"

	Scenario: Edad de 64
		Dado que la edad del individuo es "64"
		cuando realizo la operación
		entonces obtengo que el individuo "Eres adulto"

	Scenario: Edad de 118
		Dado que la edad del individuo es "118"
		cuando realizo la operación
		entonces obtengo que el individuo "Eres adulto mayor"

	Scenario: Edad de 500
		Dado que la edad del individuo es "500"
		cuando realizo la operación
		entonces obtengo que el individuo "Eres Mumm-Ra"