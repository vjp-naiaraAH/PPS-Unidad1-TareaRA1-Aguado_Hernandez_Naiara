import unittest
from src.lavadero import Lavadero


class TestLavadero(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test: crea un lavadero vacío."""
        self.lavadero = Lavadero()

    # ==============================================================
    # TEST 1: Estado inicial
    # ==============================================================
    def test1_estado_inicial_inactivo(self):
        """Test 1: Verifica el estado inicial del lavadero."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)

    # ==============================================================
    # TEST 2: Excepción encerado sin secado
    # ==============================================================
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        with self.assertRaises(ValueError) as context:
            self.lavadero.hacerLavado(False, False, True)
        self.assertIn("sin secado a mano", str(context.exception))  # Opcional: comprueba mensaje

    # ==============================================================
    # TEST 3: Excepción lavado mientras ocupado
    # ==============================================================
    def test3_excepcion_lavado_mientras_ocupado(self):
        """Test 3: Comprueba que no se puede iniciar lavado mientras está ocupado."""
        self.lavadero.hacerLavado(False, False, False)  # Ocupamos el lavadero
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, False)

    # ==============================================================
    # TESTS 4 a 8: Ingresos
    # ==============================================================
    def test4_ingresos_con_prelavado(self):
        """Test 4: Solo prelavado → 6.50€."""
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero.avanzarFase()  # Para cobrar
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50, places=2)

    def test5_ingresos_con_secado(self):
        """Test 5: Solo secado → 6.00€."""
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 6.00, places=2)

    def test6_ingresos_secado_y_encerado(self):
        """Test 6: Secado + encerado → 7.20€."""
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.20, places=2)

    def test7_ingresos_prelavado_y_secado(self):
        """Test 7: Prelavado + secado → 7.50€."""
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 7.50, places=2)

    def test8_ingresos_todo(self):
        """Test 8: Todos los extras → 8.70€."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero.avanzarFase()
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70, places=2)

    # ==============================================================
    # FUNCIÓN AUXILIAR PARA TESTS 9-14
    # ==============================================================
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
        lav = Lavadero()  # Lavadero nuevo para no afectar otros tests
        lav.hacerLavado(prelavado, secado, encerado)
        fases_visitadas = [lav.fase]

        while lav.ocupado:
            if len(fases_visitadas) > 20:
                raise Exception("Bucle infinito detectado")
            lav.avanzarFase()
            fases_visitadas.append(lav.fase)

        return fases_visitadas

    # ==============================================================
    # TESTS 9 a 14: Flujo de fases
    # ==============================================================
    def test9_flujo_sin_extras(self):
        """Test 9: Sin extras → 0, 1, 3, 4, 5, 6, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        fases = self.ejecutar_y_obtener_fases(False, False, False)
        self.assertEqual(fases, fases_esperadas)

    def test10_flujo_con_prelavado(self):
        """Test 10: Solo prelavado → 0, 1, 2, 3, 4, 5, 6, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases = self.ejecutar_y_obtener_fases(True, False, False)
        self.assertEqual(fases, fases_esperadas)

    def test11_flujo_con_secado(self):
        """Test 11: Solo secado → 0, 1, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases = self.ejecutar_y_obtener_fases(False, True, False)
        self.assertEqual(fases, fases_esperadas)

    def test12_flujo_secado_y_encerado(self):
        """Test 12: Secado + encerado → 0, 1, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases = self.ejecutar_y_obtener_fases(False, True, True)
        self.assertEqual(fases, fases_esperadas)

    def test13_flujo_prelavado_y_secado(self):
        """Test 13: Prelavado + secado → 0, 1, 2, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases = self.ejecutar_y_obtener_fases(True, True, False)
        self.assertEqual(fases, fases_esperadas)

    def test14_flujo_todo(self):
        """Test 14: Todos los extras → 0, 1, 2, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases = self.ejecutar_y_obtener_fases(True, True, True)
        self.assertEqual(fases, fases_esperadas)


if __name__ == '__main__':
    unittest.main()