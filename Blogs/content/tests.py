from urllib import response

from django.contrib.auth.models import User
from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse



# Create your tests here. 8 url test 8 CRUD test so total 16 tests are required

class TestUrls(TestCase):
    def setUp(self):
      self.user = User.objects.create(username='testuser')
      self.user.set_password('12345')
      self.user.save()
      self.c = Client()
      self.c.login(username='testuser', password='12345')
      self.admin_user = User.objects.create_superuser('admin1', 'admin@example.com', 'adminpass')
      self.admin = Client()
      self.admin.login(username='admin1', password='adminpass')


  

    def test_blog_update_url(self):
      self.assertEqual(
          reverse('blog_update_form' ,kwargs={'slug': "random-slug"}),
          '/blog/random-slug/update')
    
    def test_blog_delete_url(self):
      self.assertEqual(
          reverse('blog_delete_form' ,kwargs={'slug': "random-slug"}),
          '/blog/random-slug/delete')

    def test_blog_detail_url(self):
      self.assertEqual(
          reverse('blog_detail_view' ,kwargs={'slug': "random-slug"}),
          '/blog/random-slug/detail')

   

    def test_product_update_url(self):
      self.assertEqual(
          reverse('product_update_form' ,kwargs={'pk': "1"}),
          '/products/1/update')
    
    def test_blog_delete_url(self):
      self.assertEqual(
          reverse('product_delete_form' ,kwargs={'pk': "1"}),
          '/products/1/delete')

    def test_blog_detail_url(self):
      self.assertEqual(
          reverse('product_detail_view' ,kwargs={'pk': "1"}),
          '/products/1/detail')

    def test_blog_view(self):
      c = Client()
      req = self.c.get("/blog/")
      self.assertEqual(req.status_code, 200)

   

    def test_get_blogs(self):
      response = self.admin.get(reverse("blog_list"), follow=True)
      self.assertEqual(response.status_code, 200)

    def test_del_blog(self):
      response = self.admin.post(reverse('blog_delete_form', kwargs={"slug": "random-slug"}),follow=True) 
      self.assertEqual(response.status_code, 404) 

    def test_update_blog(self):
      response = self.admin.post(reverse('blog_update_form', kwargs={"slug":'random-slug'}),{
        "name": "upadted_test_product",
      },follow=True)
      self.assertEqual(response.status_code, 404)

    def test_register_user(self):
      response = self.c.post(reverse('register'),{
        "username": "test_user",
        "password": "test@pass123",
        "email":"test@user.com",
        "first_name": "test",
        "last_name": "test"
      },follow=True)
      
      self.assertEqual(response.status_code, 200)
