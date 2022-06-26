from django.test import TestCase
from . models    import keyword

# import unittest

class testTranlations(TestCase):

    def test_create(self):
        self.assertEqual(keyword.objects.create("Hello, world"      ),""                  )
        self.assertEqual(keyword.objects.create("Crowdbotics"       ), "scitobdworC"      )
        self.assertEqual(keyword.objects.create("Hello, 世界"       ), "界世 ,olleH"       )
        self.assertEqual(keyword.objects.create("نص عربي"          ), "يبرع صن"          )
        self.assertEqual(keyword.objects.create("نَصٌ عَربِيٌّ"          ),"ٌّيِبرَع ٌصَن"           )
        self.assertEqual(keyword.objects.create("نَصٌ عَربِيٌّ!"         ), "!ٌّيِبرَع ٌصَن"         )
        self.assertEqual(keyword.objects.create("نَصٌ example, عَربِيٌّ!"), "!ٌّيِبرَع ,elpmaxe ٌصَن")
        self.assertEqual(keyword.objects.create(""                  ), ""                 )