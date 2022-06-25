 
import subprocess
from django.db    import models

# from arabic_keyword_api  import stringutils
    
class keyword(models.Model):

    keyword_text         = models.CharField("KeyWord to Translate",max_length=150)
    keyword_translations = models.CharField("Ttranslated Keyword", blank=True,default='لاشيء',max_length=200)

    def get_translation(self):
        output = str(subprocess.check_output(['py' ,'babla',self.keyword_text], shell=True))
        
        self.keyword_translations = str({self.keyword_text:output})
        print('output='+output)
        return output
        

    def save(self,*args,**kwargs):
        self.keyword_translations = self.get_translation()
        super(keyword,self).save(*args,**kwargs)


    def __str__(self):
       return self.keyword_text
