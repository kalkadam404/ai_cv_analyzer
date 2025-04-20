import spacy
import fitz  # PyMuPDF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.generics import ListAPIView

nlp = spacy.load("en_core_web_sm")
class ResumeUploadView(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        resume = Resume.objects.create(user=request.user, file=file)
        text = self.extract_text_from_pdf(resume.file.path)
        resume.extracted_text = text

        parsed_data = self.extract_resume_data(text)

        resume.skills = parsed_data.get("skills", "")
        resume.education = parsed_data.get("education", "")
        resume.experience = parsed_data.get("experience", "")
        resume.save()

        return Response({
            'message': 'Resume uploaded and parsed successfully',
            'resume': ResumeSerializer(resume).data
        })

    def extract_text_from_pdf(self, path):
        text = ''
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    def extract_resume_data(self, text):
        lines = text.splitlines()
        skills = []
        education = []
        experience = []

        current_section = None

        for line in lines:
            lower = line.lower()
            if "skill" in lower:
                current_section = "skills"
                continue
            elif "education" in lower:
                current_section = "education"
                continue
            elif "experience" in lower or "employment" in lower:
                current_section = "experience"
                continue

            if current_section == "skills":
                skills.append(line.strip())
            elif current_section == "education":
                education.append(line.strip())
            elif current_section == "experience":
                experience.append(line.strip())

        return {
            "skills": ', '.join(skills).strip(),
            "education": '\n'.join(education).strip(),
            "experience": '\n'.join(experience).strip(),
        }

class ResumeListView(ListAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class ResumeDetailView(APIView):
    def get(self, request, pk):
        try:
            resume = Resume.objects.get(pk=pk)
            serializer = ResumeSerializer(resume)
            return Response(serializer.data)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found"}, status=404)