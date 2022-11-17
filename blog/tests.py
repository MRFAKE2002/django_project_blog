from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from .models import Blog

User = get_user_model()

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username='test_user')
        cls.test_user.set_password('test_password')
        cls.test_user.save()
        
        cls.test_post1 = Blog.objects.create(
            user = cls.test_user,
            title = 'post1 Title',
            text = 'post1 text',
            status = Blog.STATUS_CHOICES[0][0],
            author = cls.test_user,
        )
        cls.test_post2 = Blog.objects.create(
            user = cls.test_user,
            title = 'post2 Title',
            text = 'post2 text',
            status = Blog.STATUS_CHOICES[1][0],
            author = cls.test_user,
        )
    
    # def setUp(self):
    #     self.test_user = User.objects.create(username='test_user')
    #     test_post = Blog.objects.create(
    #         user = self.test_user,
    #         title = 'post1 Title',
    #         text = 'post1 text',
    #         status = Blog.STATUS_CHOICES[0][0],
    #         author = self.test_user,
    #     )
    
    def test_login(self):
        # self.assertFalse(self.test_user(self.client).is_authenticated())
        test_login = self.client.login(username='test_user', password='test_password')
        self.assertTrue(test_login)
    
    def test_blog_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(200, response.status_code)
        
    def test_blog_list_url_by_name(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(200, response.status_code)
    
    def test_blog_detail_url_by_name(self):
        response = self.client.get(reverse('blog_detail', args=[self.test_post1.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_blog_detail_url(self):
        response = self.client.get(f'/blog/{self.test_post1.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_details_in_blog_detail_page(self):
        response = self.client.get(reverse('blog_detail', args=[self.test_post1.id]))
        print(response['location'])
        self.assertContains(response, self.test_post1.title)
        self.assertContains(response, self.test_post1.text)
    
    def test_draft_post_not_show_in_blog_list_page(self):
        response = self.client.get(reverse('blog_list')) 
        self.assertContains(response, self.test_post1.title)
        self.assertNotContains(response, self.test_post2.title)