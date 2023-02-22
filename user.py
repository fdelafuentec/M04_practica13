class user:
    #declarem constructor
    def __init__(self, id, nom, cognom, username, pfp, estat):
        self.id = id
        self.nom = nom
        self.cognom = cognom
        self.username = username
        self.pfp = pfp
        self.estat = estat
    #declarem setters i getters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom

    def setCognom(self, cognom):
        self.cognom = cognom

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPfp(self):
        return self.pfp

    def setPfp(self, pfp):
        self.pfp = pfp

    def setEstat(self, estat):
        self.estat = estat

    def getEstat(self):
        return self.estat

    #cridem el print
    def user(self):
        informacio = "El teu id és {id}, el teu username és {username}, el teu nom és {nom}, el teu cognom és {cognom}, la teva foto de perfil es de color {pfp} i el teu estat és {estat}"
        print(
            informacio.format(
            id=self.id, username=self.username, nom=self.nom, cognom=self.cognom, pfp=self.pfp, estat=self.estat))
