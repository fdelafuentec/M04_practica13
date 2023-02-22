class book:
    #declarem constructor
    def __init__(self, titol, tipografia, editorial, autor, portada, tapa):
        self.titol = titol
        self.tipografia = tipografia
        self.editorial = editorial
        self.autor = autor
        self.portada = portada
        self.tapa = tapa
    #declarem setters i getters
    def getTitol(self):
        return self.titol

    def setTitol(self, titol):
        self.titol = titol

    def getTipografia(self):
        return self.tipografia

    def setTipografia(self, tipografia):
        self.tipografia = tipografia

    def getEditorial(self):
        return self.editorial

    def setEditorial(self, editorial):
        self.editorial = editorial

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getPortada(self):
        return self.portada

    def setPortada(self, portada):
        self.portada = portada

    def setTapa(self, tapa):
        self.tapa = tapa

    def getTapa(self):
        return self.tapa

    #cridem el print
    def info(self):
        informacio = "Aquest llibre té de titol {titol}, tipografia {tipografia}, és de l'editorial {editorial}, l'autor és {autor}, la portada és de color {portada} i és de tapa {tapa}"
        print(
            informacio.format(
            titol=self.titol, tipografia=self.tipografia, editorial=self.editorial, autor=self.autor, portada=self.portada, tapa=self.tapa))
