from ast import Import
from http.client import ImproperConnectionState
from django.test import TestCase
from . models    import keyword

# import unittest

class TestStringUtils(TestCase):

    def test_Reverse(self):
        self.assertEqual(keyword.objects.create("Hello, world"      ),"dlrow ,olleH"      )
        self.assertEqual(keyword.objects.create("Crowdbotics"       ), "scitobdworC"      )
        self.assertEqual(keyword.objects.create("Hello, 世界"       ), "界世 ,olleH"       )
        self.assertEqual(keyword.objects.create("نص عربي"          ), "يبرع صن"          )
        self.assertEqual(keyword.objects.create("نَصٌ عَربِيٌّ"          ),"ٌّيِبرَع ٌصَن"           )
        self.assertEqual(keyword.objects.create("نَصٌ عَربِيٌّ!"         ), "!ٌّيِبرَع ٌصَن"         )
        self.assertEqual(keyword.objects.create("نَصٌ example, عَربِيٌّ!"), "!ٌّيِبرَع ,elpmaxe ٌصَن")
        self.assertEqual(keyword.objects.create(""                  ), ""                 )