# resumes/tasks.py
from celery import shared_task
import fitz  
import spacy
from .models import Resume

nlp = spacy.load("en_core_web_sm")

@shared_task
def process_resume(resume_id):
    try:
        resume = Resume.objects.get(id=resume_id)
        with fitz.open(resume.file.path) as doc:
            text = ''.join([page.get_text() for page in doc])
        resume.extracted_text = text

        doc = nlp(text)
        skills = [token.text for token in doc if token.pos_ == 'NOUN']
        resume.skills = ', '.join(skills)
        resume.save()
        return f"Resume {resume_id} processed successfully"
    except Resume.DoesNotExist:
        return f"Resume {resume_id} not found"
