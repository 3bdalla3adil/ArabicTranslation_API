from celery import shared_task
from django.utils import timezone
from .models import Keyword

import requests
import logging


@shared_task
def translate_keyword(keyword_id):
    try:
        keyword = Keyword.objects.get(id=keyword_id)
        # Mock external translation service call
        response = requests.get(f'https://api.translation-service.com/translate', params={'text': keyword.keyword_text})
        response.raise_for_status()
        translation = response.json().get('translation', 'No Translation Found')
        
        keyword.keyword_translations = translation
        keyword.last_translated = timezone.now()
        keyword.save()
    except Exception as e:
        logging.error(f"Failed to translate keyword {keyword_id}: {e}")
