from stringutils import Reverse,SmartLength,RemoveTashkeel,RemoveTatweel,ToGlyph,RemoveAllNonArabicChars

import unittest

class TestStringUtils(unittest.TestCase):

    def test_Reverse(self):
        self.assertEqual(Reverse("Hello, world"      ),"dlrow ,olleH"      )
        self.assertEqual(Reverse("Crowdbotics"       ), "scitobdworC"      )
        self.assertEqual(Reverse("Hello, 世界"       ), "界世 ,olleH"       )
        self.assertEqual(Reverse("نص عربي"          ), "يبرع صن"          )
        self.assertEqual(Reverse("نَصٌ عَربِيٌّ"          ),"ٌّيِبرَع ٌصَن"           )
        self.assertEqual(Reverse("نَصٌ عَربِيٌّ!"         ), "!ٌّيِبرَع ٌصَن"         )
        self.assertEqual(Reverse("نَصٌ example, عَربِيٌّ!"), "!ٌّيِبرَع ,elpmaxe ٌصَن")
        self.assertEqual(Reverse(""                  ), ""                 )
       
    def test_SmartLength(self):
        self.assertEqual(SmartLength("نَصٌ عَربِيٌّ")    , 7 ) 
        self.assertEqual(SmartLength("نص عربي")    , 7 )
        self.assertEqual(SmartLength("Hello, world"), 12)
        self.assertEqual(SmartLength("Hello, 世界") , 9 )
        self.assertEqual(SmartLength("")            , 0 )

    def test_RemoveTashkeel(self):
        self.assertEqual(RemoveTashkeel("نَصٌ عَربِيٌّ"), "نص عربي")
        self.assertEqual(RemoveTashkeel("نص عربي"), "نص عربي")
        self.assertEqual(RemoveTashkeel(""       ), ""        )

    def test_ToGlyph(self):
        self.assertEqual(ToGlyph("تجربة النص العربي"), "\ufe97\ufea0\ufeae\ufe91\ufe94 \u0627\ufedf\ufee8\ufeba \u0627\ufedf\ufecc\ufeae\ufe91\ufef2" )

    def test_RemoveTatweel(self):
        self.assertEqual(RemoveTatweel("نـــص عــربــي"), "نص عربي" )
        self.assertEqual(RemoveTatweel("نـــَصٌ عَـربي"   ), "نَصٌ عَربي" )
        self.assertEqual(RemoveTatweel(""               ), ""        )

    def test_RemoveAllNonArabicChars(self):
        self.assertEqual(RemoveAllNonArabicChars("عــربـabcـينـــص"     ), "عــربــينـــص" )
        self.assertEqual(RemoveAllNonArabicChars("عــربــينwo%%rd_ـــصa"), "عــربــينـــص" )
        self.assertEqual(RemoveAllNonArabicChars(""                      ), ""               )
        
if __name__ == '__main__':
    unittest.main()


