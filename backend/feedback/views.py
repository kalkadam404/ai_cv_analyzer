
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from resumes.models import Resume
class ResumeFeedbackView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):
        try:
            resume = Resume.objects.get(id=resume_id, user=request.user)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found"}, status=404)
        text = resume.extracted_text.lower()

        recommended_skills = {"python", "django", "javascript", "react", "vue", "rest api"}
        resume_skills = set(s.strip().lower() for s in resume.skills.split(",") if s.strip())
        missing_skills = list(recommended_skills - resume_skills)
        words_count = len(text.split())
        formatting_feedback = "Good formatting." if words_count >= 100 else "Your resume appears short. Consider adding more details."
        common_ats_keywords = {"ci/cd", "agile", "git", "docker", "aws"}
        missing_keywords = list(common_ats_keywords - resume_skills)
        
        feedback = {
            "missing_skills": missing_skills,
            "formatting_feedback": formatting_feedback,
            "ats_keywords_suggestion": missing_keywords,
        }
        return Response(feedback)
