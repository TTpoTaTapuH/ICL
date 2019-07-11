from rest_framework import viewsets

from catalog.api.serializers import TaskSerializer
from catalog.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows news to be viewed or edited.
    """
    queryset = Task.objects.all()

    def get_serializer_class(self):
        return TaskSerializer
