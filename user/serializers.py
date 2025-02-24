from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from .models import *
from datetime import datetime


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        username = validated_data['phone_number']
        
        user = CustomUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=username,  
            phone_number=validated_data['phone_number']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Error! Incorrect credentials')
        
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        
        now = datetime.now()
        user.last_login = now
        user.save(update_fields=["last_login"]) 
        
        return {
            'refresh': str(refresh),
            'access': str(access),
            'user': f"{user.first_name} {user.last_name}",
            }
    

class RegisterTasksUserSerializers(serializers.ModelSerializer) : 
    category = serializers.CharField(write_only=True) 
    category_name = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = Tasks
        fields = ['title', 'descriptions', 'category', 'category_name','due_date']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None  

    def create(self, validated_data):
        category_name = validated_data.pop('category', None)
        category = None

        if category_name:
            category, _ = Category.objects.get_or_create(name=category_name)  

        user = self.context['request'].user
        task = Tasks.objects.create(user=user, category=category, **validated_data)
        return task
    
class CompletedTasksSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model = Tasks
        fields =['completed']    

    def update(self,instance, validated_data):
        instance.completed = True
        instance.save(update_fields=["completed"])
        return instance
    
class TasksSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model = Tasks
        fields = [ 'user_task_id' , 'title' , 'user' , 'descriptions' , 'completed' , 'created_at' , 'due_date' , 'category']    
class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'descriptions', 'completed', 'due_date', 'category'] 
        extra_kwargs = {
            'title': {'required': False},  
            'descriptions': {'required': False},
            'completed': {'required': False},
            'due_date': {'required': False},
            'category': {'required': False},
        }
