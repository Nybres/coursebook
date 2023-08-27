from rest_framework.generics import RetrieveUpdateAPIView
from ..models import Instructor
from ..serializers import InstructorSerializer


class EditInstructorView(RetrieveUpdateAPIView):
    serializer_class = InstructorSerializer

    queryset = Instructor.objects.all()
    # def get_queryset(self):
    #     return Instructor.objects.filter(app_user=self.request.user)
