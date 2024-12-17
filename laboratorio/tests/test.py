from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio, DirectorGeneral

class LaboratorioTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un director general
        director = DirectorGeneral.objects.create(
            nombre="Director General 6",
            especialidad="Biología"
        )

        # Crear un laboratorio
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio6",
            ciudad="Santiago",
            pais="Chile",
            director=director
        )

    def test_laboratorio_data(self):
        """
        Verificar que los datos del laboratorio coincidan con los datos que se crearon
        en setUpTestData.
        """
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        
        self.assertEqual(laboratorio.nombre, "Laboratorio6")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")
        self.assertEqual(laboratorio.director.nombre, "Director General 6")

    def test_laboratorio_url(self):
        """
        Verificar que la URL del laboratorio devuelve una respuesta HTTP 200.
        """
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_template_and_content(self):
        """
        Verificar que la página usa la plantilla correcta y que el contenido HTML
        coincida con lo esperado.
        """
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        
        # Verificar que se está usando la plantilla correcta
        self.assertTemplateUsed(response, 'laboratorio/listar_laboratorios.html')
        
        # Verificar que el contenido de la página coincida con lo esperado
        self.assertContains(response, "Laboratorio6")
        self.assertContains(response, "Santiago")
        self.assertContains(response, "Chile")
        self.assertContains(response, "Director General 6")
