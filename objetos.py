class cursos:

    def __init__(self, computadora, tablet, mochila, programas):
        self.computadora = computadora
        self.tablet = tablet
        self.mochila = mochila
        self.programas = programas

    def __str__(self,):
        return f"{self.computadora}"

diseño = cursos ("mac", "ipad", "timberland", "adobe")
print (diseño)
print (diseño.computadora)