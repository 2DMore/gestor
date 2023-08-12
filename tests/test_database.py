import unittest
import database as db
import copy
import helpers

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista=[
            db.Cliente("21E","Mario", "Marquez"),
            db.Cliente("45R","Felipe","Caceres"),
            db.Cliente("87Y", "Gary", "Lopez")
        ]

    def test_buscar_cliente(self):
        cliente_existente=db.Clientes.buscar("45R")
        cliente_inexistente=db.Clientes.buscar("12L")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente=db.Clientes.crear("52Y", "Patricio", "Wonka")
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "52Y")
        self.assertEqual(nuevo_cliente.nombre, "Patricio")
        self.assertEqual(nuevo_cliente.apellido, "Wonka")

    def test_modificar_cliente(self):
        cliente_a_modificar=copy.copy(db.Clientes.buscar("87Y"))
        cliente_modificado=db.Clientes.modificar("87Y","Pepe","Castro")
        self.assertEqual(cliente_a_modificar.nombre, "Gary")
        self.assertEqual(cliente_modificado.nombre, "Pepe")
    
    def test_borrar_cliente(self):
        cliente_borrado=db.Clientes.borrar("21E")
        cliente_rebuscado=db.Clientes.buscar("21E")
        self.assertEqual(cliente_borrado.dni, "21E")
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido("00A", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("123123213132", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("F35", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("45R", db.Clientes.lista))