from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class LoginTest(TestCase):
    def setUp(self):
        #create dummy user
        self.username = "test123"
        self.password = "@gnels2026"
        
        User.objects.create_user(username=self.username, password = self.password)
        
        #login che naav
        self.login_url = reverse("users:login-user") 
        
    def test_login_logic(self):
        #post requst ne check
        response = self.client.post(self.login_url, {
            'username' : self.username,
            'password' : self.password
        }, follow=True)        
        
        #check karave lagel
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login Success")

    def test_wrong_login_logic(self):
        response = self.client.post(self.login_url, {
            'username' : self.username,
            'password' : "wrong password"
        })
        
        self.assertNotContains(response, "Login success")



