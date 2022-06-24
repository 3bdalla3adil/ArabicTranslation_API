 
from django.db          import models
from arabic_keyword_api.babla import scrape
# from .arabic_keyword_api  import stringutils


"""class ReadOnlyWidget(widgets.Widget):
    #Some of these values are read only - just a bit of text...
    #def render(self, _, value, attrs=None):
        #return value """
    
class keyword(models.Model):

    keyword_text         = models.CharField("KeyWord to Translate",max_length=150)
    keyword_translations = models.CharField("Translated Keyword",default='لاشيء',editable=False,max_length=150)


    def save(self,*args,**kwargs):
        self.keyword_translations = scrape(self.keyword_text)
        super().save(self,*args,**kwargs)


    def __str__(self):
       return self.keyword_text

    
# Create your models here.
