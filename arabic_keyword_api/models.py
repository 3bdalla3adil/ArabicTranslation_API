 
from django.db    import models
    
class keyword(models.Model):

    keyword_text         = models.CharField("KeyWord to Translate",max_length=150)
    keyword_translations = models.CharField("Ttranslated Keyword", blank=True,default='لاشيء',max_length=200)

    def get_translation(self):
        import platform,subprocess
        if platform.system() == 'Linux' or 'Darwin' :
            output = str(subprocess.check_output(['python3' ,'babla',self.keyword_text], shell=True).decode('utf-8'))
          
        elif platform.system() == 'Windows':
            output = str(subprocess.check_output(['py' ,'babla',self.keyword_text], shell=True).decode('utf-8'))
        
        self.keyword_translations = str({self.keyword_text:output})
        # print('output='+output)
        return {self.keyword_text:output}
        

    def save(self,*args,**kwargs):
        self.keyword_translations = self.get_translation()
        super(keyword,self).save(*args,**kwargs)


    def __str__(self):
       return self.keyword_text
