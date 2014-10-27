Feature: Obtener una calculadora básica
	Como usuario del sistema
	Quiero obtener una calculadora que realice las funciones básicas
	de suma, resta multiplicación y división 
	para facilitar la realización de esos cálculos.

Scenario: "Suma" de "4" más "4"
	Given La operación es una "Suma" y sus sumandos son "4" y "4"
	when realizo el cálculo
	then obtengo como resultado "8"

Scenario: "Resta" de "4" más "4"
	Given La operación es una "Resta" y sus sumandos son "4" y "4"
	when realizo el cálculo
	then obtengo como resultado "0"

Scenario: "Multiplicacion" de "4" más "4"
	Given La operación es una "Multiplicacion" y sus sumandos son "4" y "4"
	when realizo el cálculo
	then obtengo como resultado "16"


Scenario: "Division" de "4" más "4"
	Given La operación es una "Division" y sus sumandos son "4" y "4"
	when realizo el cálculo
	then obtengo como resultado "1"