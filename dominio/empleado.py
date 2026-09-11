class Empleado:
    def __init__(self, rut, nombre, fecha_ingreso, sueldo_base):
        self.rut = rut
        self.nombre = nombre
        self.fecha_ingreso= fecha_ingreso
        self.sueldo_base = sueldo_base
        self.registros = []
        self.departamento = None

    def registrar_horas(self, registro):
        pass

    def total_horas(self):
        pass
