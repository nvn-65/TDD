from django.test import TestCase


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        response = self.client.post('/', data={'item_text': 'Новый элемент списка'})
        self.assertIn('Новый элемент списка', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
