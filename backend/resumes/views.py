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
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        resume = Resume.objects.create(user=request.user, file=file)

        text = self.extract_text_from_pdf(resume.file.path)
        resume.extracted_text = text

        doc = nlp(text)
        resume.skills = ', '.join([token.text for token in doc if token.pos_ == 'NOUN'])
        resume.save()

        return Response({'message': 'Resume uploaded and parsed successfully'})

    def extract_text_from_pdf(self, path):
        text = ''
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
        return text


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