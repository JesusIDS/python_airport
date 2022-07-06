class Empleado:
    def __init__(self, nombre, apellido, pais, idioma, aeropuerto):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.idioma = idioma
        self.aeropuerto = aeropuerto

    def get_dicc(self):
        language = {'name' : self.idioma}
        airports = {'name' : self.aeropuerto}
        country = {'name' : self.pais, 'airportsCountry' : [airports]}
        dicc = {'surname' : self.apellido, 'firstname' : self.nombre, 'languageSpeaks' : [language],
                'countryWork' : country}
        return dicc

