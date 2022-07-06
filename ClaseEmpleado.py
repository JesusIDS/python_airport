class Empleado:
    def __init__(self, nombre, apellido, pais, idioma, aeropuerto):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.idioma = idioma
        self.aeropuerto = aeropuerto

    def get_dicc(self):
        codeC = None
        codeI = None
        if self.pais == ' Mexico':
            codeC = 'mx'
        elif self.pais == ' Francia':
            codeC = 'fr'

        if self.idioma == ' EspaÃ±ol':
            codeI = 'es'
        elif self.idioma == ' Frances':
            codeI = 'fr'

        language = {'code' : codeI, 'name' : self.idioma}
        airports = {'name' : self.aeropuerto}
        country = {'code' : codeC, 'name' : self.pais, 'airportsCountry' : [airports]}
        dicc = {'surname' : self.apellido, 'firstname' : self.nombre, 'languageSpeaks' : [language],
                'countryWork' : country}
        return dicc

