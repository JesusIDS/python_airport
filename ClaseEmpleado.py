class Empleado:
    def __init__(self, nombre, apellido, pais, idioma, aeropuerto):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.idioma = idioma
        self.aeropuerto = aeropuerto

    def __str__(self):
        return "{\n'name' : '" + self.nombre + "',\n" + "'surname' : '" + self.apellido + "',\n" + \
        "'country' : '" + self.pais + "',\n" + "'language' : '" + self.idioma + "',\n" + \
        "'airport' : '" + self.aeropuerto + "'\n}"
