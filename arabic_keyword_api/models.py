<<<<<<< HEAD
#from . babla     import scrape 
from django.db import models
from .babla    import scrape
=======
 
from django.db              import models
# from .arabic_keyword_api  import stringutils

>>>>>>> 8771cc18b1ab13e02f90578b7ddef2b7fc253895

"""class ReadOnlyWidget(widgets.Widget):
    #Some of these values are read only - just a bit of text...
    #def render(self, _, value, attrs=None):
        #return value """
    
class keyword(models.Model):

<<<<<<< HEAD
    keyword_text         = models.CharField("KeyWord to Translate",max_length=150)
    keyword_translations = models.CharField("Ttranslated Keyword", default='لاشيء',editable=False,max_length=150)


    def save(self,*args,**kwargs):
        self.keyword_translations = scrape(self.keyword_text)
        super().save(self,*args,**kwargs)

=======
    keyword_text = models.CharField("KeyWord",max_length=150)
    key_out_text = models.CharField("keyword output",default='Nothing',max_length=150)


    # def value_to_string(self, obj):
    #     self.keyword_text = 
>>>>>>> 8771cc18b1ab13e02f90578b7ddef2b7fc253895

    def __str__(self):
       return self.keyword_text

    
# Create your models here.
