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

    def test_only_saves_item_whem_necessary(self):
        """тест: сохраняет элементы, только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        self.client.post('/', data={'item_text': 'Новый элемент списка'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Новый элемент списка')

    def test_redirects_after_POST(self):
        """тест: переадресует после post-запроса"""
        response = self.client.post('/', data={'item_text': 'Новый элемент списка'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_display_all_list_items(self):
        """тест: отображаются все элементы списка"""
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())