 
import subprocess
from django.db import models

    
class keyword(models.Model):

    keyword_text         = models.CharField("Keyword to Translate", max_length=150)
    keyword_translations = models.CharField("Translated Keyword", blank=True,default='لاشيء', max_length=200)
    
    last_translated      = models.DateTimeField("Last Translated", null=True, blank=True)
    objects = KeywordManager()
    
    # Meta class within the Model to define indexes that speed up query performance
    class Meta:
        indexes = [
            models.Index(fields=['keyword_text']),
            models.Index(fields=['last_translated']),
        ]
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"
        ordering = ['keyword_text']

    def update_translation(self):
        from .tasks import translate_keyword
        translate_keyword.delay(self.id)

    def get_translation(self):
        output = subprocess.check_output(['py' ,'babla',self.keyword_text], shell=True).decode('utf-8').strip('\r\n')
        
        return output

    def save(self,*args,**kwargs):
        self.keyword_translations = self.get_translation()
        super(keyword,self).save(*args,**kwargs)


    def __str__(self):
       return self.keyword_text


class KeywordManager(models.Manager):
    def recent_keyword(self):
        return self.filter()

    
