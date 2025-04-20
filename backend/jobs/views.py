from rest_framework import viewsets, permissions
from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from resumes.models import Resume 
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
nlp = spacy.load("en_core_web_sm")
class MatchedVacanciesView(APIView):
    """
    Получает ID резюме (resume_id) и сравнивает текст резюме с описаниями вакансий.
    Возвращает список вакансий с полем match_score (процент совпадения).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):
        try:
            resume = Resume.objects.get(id=resume_id, user=request.user)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found"}, status=404)
        
        resume_text = resume.extracted_text
        vacancies = Vacancy.objects.filter(is_active=True)
        if not vacancies.exists():
            return Response([])
        vacancy_descriptions = [vacancy.description for vacancy in vacancies]
        corpus = [resume_text] + vacancy_descriptions
        vectorizer = TfidfVectorizer(stop_words='english')
        try:
            tfidf_matrix = vectorizer.fit_transform(corpus)
            similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        except Exception as e:
            similarity_scores = np.zeros(len(vacancies))
        vacancy_data = []
        for vacancy, score in zip(vacancies, similarity_scores):
            serialized = VacancySerializer(vacancy).data
            serialized['match_score'] = round(score * 100, 2)  # переводим в проценты
            vacancy_data.append(serialized)
        
        vacancy_data.sort(key=lambda x: x['match_score'], reverse=True)
        return Response(vacancy_data)

@receiver(post_save, sender=Vacancy)
def notify_users_about_new_vacancy(sender, instance, created, **kwargs):
    if created:
        keywords = instance.title.lower().split()
        resumes = Resume.objects.all()

        for resume in resumes:
            resume_text = (resume.skills or '') + ' ' + (resume.experience or '')
            resume_text = resume_text.lower()
            if any(word in resume_text for word in keywords):
                Notification.objects.create(
                    user=resume.user,
                    message=f"New vacancy matches your profile: {instance.title}"
                )

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def recommended_vacancies(request):
    user_resumes = Resume.objects.filter(user=request.user)
    keywords = set()
    for resume in user_resumes:
        if resume.skills:
            keywords.update(resume.skills.lower().split(','))

    matched = Vacancy.objects.filter(description__icontains=list(keywords)[0]) if keywords else []
    return Response(VacancySerializer(matched, many=True).data)



@api_view(['GET'])
@permission_classes([IsAdminUser])  
def analytics_view(request):
    total_resumes = Resume.objects.count()
    total_vacancies = Vacancy.objects.count()
    active_vacancies = Vacancy.objects.filter(is_active=True).count()
    
    User = get_user_model()
    total_users = User.objects.count()
    avg_resumes_per_user = total_resumes / total_users if total_users > 0 else 0

    data = {
        "total_resumes": total_resumes,
        "total_vacancies": total_vacancies,
        "active_vacancies": active_vacancies,
        "average_resumes_per_user": round(avg_resumes_per_user, 2)
    }
    return Response(data)
