class university:
    #declarem el constructor
    def __init__(self, altura, llargada, amplada, metresQuadrats, pais, ciutat):
        self.altura = altura
        self.llargada = llargada
        self.amplada = amplada
        self.metresQuadrats = metresQuadrats
        self.pais = pais
        self.ciutat = ciutat
    #declarem els setters i getters
    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getLlargada(self):
        return self.llargada

    def setLlargada(self, llargada):
        self.llargada = llargada

    def getAmplada(self):
        return self.amplada

    def setAmplada(self, amplada):
        self.amplada = amplada

    def getMetresQuadrats(self):
        return self.metresQuadrats

    def setMetresQuadrats(self, metresQuadrats):
        self.metresQuadrats = metresQuadrats

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def setCiutat(self, ciutat):
        self.ciutat = ciutat

    def getCiutat(self):
        return self.ciutat

    #cridem el print
    def university(self):
        informacio = "L'alçada de l'universitat és de {altura}, la llargada {llargada}, amplada {amplada}, els metres quadrats són {metresquadrats}, el país on està situada és {pais} i la ciutat és {ciutat}."
        print(
            informacio.format(
            altura=self.altura, llargada=self.llargada, amplada=self.amplada, metresquadrats=self.metresQuadrats, pais=self.pais, ciutat=self.ciutat))
