#importem les classes dels arxius
from book import book
from user import user
from university import university
from animal import Animal
from school import School
from vehicle import Vehicle

llibre1 = book("Hola", "Colibri", "Planeta", "Eduardo", "vermella", "dura")
llibre1.info()
llibre1.setTitol("Apuestas")
llibre1.info()
llibre2 = book("La historia interminable", "Arial", "Barcanova", "JK ROWLING", "blanca", "blanda")
llibre2.info()
llibre2.setTapa("dura")
llibre2.info()

user1 = user("8457e4", "Roger","Sobrino" , "PelotaFeliz", "blava", "Content!")
user1.user()
user1.setId("847e3")
user1.user()
user2 = user("12ez4y186", "Federico", "de la Fuente", "AldeanoTranquilo", "verda", "Energetic!")
user2.user()
user2.setPfp("groga")
user2.user()

uni1 = university("143m", "120m", "314m", "120m2", "Espanya", "Barcelona")
uni1.university()
uni1.setCiutat("Girona")
uni1.university()
uni2 = university("348m", "641m", "120m", "122m2", "Estats Units", "California")
uni2.university()
uni2.setAltura("120m")
uni2.university()



# creacion del objecto vehiculo y sus atributos, al igual con todos school, animal
vehicle1 = Vehicle("audi", "A3", "2016", "rojo", "5", "gasolina")
vehicle1.parts()
vehicle1.set_motor("diesel")
vehicle1.parts()
vehicle2 = Vehicle("mercedes", "45s", "2018", "azul", "5", "gasolina")
vehicle2.parts()
vehicle2.set_motor("hibrido")
vehicle2.parts()

animal1 = Animal("perro","cannis lupus", "2", "10", "blanco", "Pienso")
animal1.salutacio()
animal1.set_peso("11")
animal1.salutacio()
animal2 = Animal("gato","felis silvestris", "4", "8", "blanco y marron", "pienso")
animal2.salutacio()
animal2.set_color("naranja")
animal2.salutacio()

school1 = School("jaume balmes","pau claris","5000","120","973548762","9h-21h")
school1.info()
school1.set_numAlumnos("6000")
school1.info()
school2 = School("sagrada familia","calle falsa","4580","210","973546962","9h-21:30h")
school2.info()
school2.set_numProfesores("150")
school2.info()
