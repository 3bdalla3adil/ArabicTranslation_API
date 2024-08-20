 
import subprocess
from django.db    import models

    
class keyword(models.Model):

    keyword_text         = models.CharField("Keyword to Translate",max_length=150)
    keyword_translations = models.CharField("Translated Keyword", blank=True,default='لاشيء',max_length=200)
    
    objects = KeywordManager()
    
    # Meta class within the Model to define indexes that speed up query performance
    class Meta:
        indexes = [
            models.Index(fields=['keyword_text']),
        ]

    def get_translation(self):
        output = subprocess.check_output(['py' ,'babla',self.keyword_text], shell=True).decode('utf-8').strip('\r\n')
        
        return output

    def save(self,*args,**kwargs):
        self.keyword_translations = self.get_translation()
        super(keyword,self).save(*args,**kwargs)


    def __str__(self):
       return self.keyword_text


class ArabicKeywordQuerySet(models.QuerySet):
    def recent(self):
        return self.filter(created_at__gte='2024-01-01')

    def by_keyword(self, keyword):
        return self.filter(keyword__iexact=keyword)

class ArabicKeywordManager(models.Manager):
    def get_queryset(self):
        return ArabicKeywordQuerySet(self.model, using=self._db)

    def recent_keywords(self):
        return self.get_queryset().recent()

    def search_by_keyword(self, keyword):
        return self.get_queryset().by_keyword(keyword)

class ArabicKeyword(models.Model):
    keyword = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ArabicKeywordManager()

    def __str__(self):
        return self.keyword

    
