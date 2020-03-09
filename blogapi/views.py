from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import GetArticlesSerializer,CreateArticleSerializer, CreateUser
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from blogapp.models import Article

@api_view(['GET'])
def testview(request):
    data = {"message":"hello world"}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getarticles(request):
    print(request.user)
    articles = Article.objects.all().order_by('-posted_on')
    serializer = GetArticlesSerializer(articles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createarticle(request):
    serializer = CreateArticleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(request.data.get('title'))
    print(request.data.get('content'))
    a = Article.objects.create(title=request.data.get('title'), content=request.data.get('content'), posted_by=request.user)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def createuserview(request):
    serializer = CreateUser(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return Response(data={"token":token}, status=status.HTTP_201_CREATED)
    
