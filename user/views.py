from urllib import request
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import *
from .models import *

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': user.phone_number
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class RegisterTasksView(generics.CreateAPIView): 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterTasksUserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = serializer.save()  

        return Response({
            'message': 'تسک با موفقیت ثبت شد!',
            'task': {
                'Title': task.title,
                'descriptions': task.descriptions,
                'Category': task.category.name if task.category else None,
                'due_date': task.due_date
            }
        }, status=status.HTTP_201_CREATED)

class CompletedTasksView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompletedTasksSerializers
    lookup_field = "user_task_id"

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)

class DeleteTasksView(generics.DestroyAPIView):
    serializer_class = TasksSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)  

    def delete(self, request, *args, **kwargs):
        user_task_id = self.kwargs.get('user_task_id') 
        task = self.get_queryset().filter(user_task_id=user_task_id).first()  

        if not task:
            return Response({'error': 'این تسک وجود ندارد !'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'message': 'تسک با موفقیت حذف شد.'}, status=status.HTTP_200_OK)
class UpdateTaskView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TasksSerializers
    lookup_field = "user_task_id" 

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)  