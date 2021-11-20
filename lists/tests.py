from django.test import TestCase
from lists.models import Item

class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранения и получения элементав списка"""
        first_item = Item()
        first_item.text = 'Первый (когда-либо) элемент списка'
        first_item.save()

        second_item = Item()
        second_item.text = 'Пункт второй'
        second_item.save()

        save_items = Item.objects.all()
        self.assertEqual(first_item.text, 'Первый (когда-либо) элемент списка')
        self.assertEqual(second_item.text, 'Пункт второй')

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
