#importem les classes dels arxius
from book import book
from user import user
from university import university

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
