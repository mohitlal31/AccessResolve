from accommodation.models import AccommodationRequest
from accommodation.serializers import (
    AccommodationRequestSerializer,
    UserLoginSerializer,
    UserSerializer,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class AccommodationList(generics.ListCreateAPIView):
    serializer_class = AccommodationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return AccommodationRequest.objects.filter(user=self.request.user)


class AccommmodationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccommodationRequestSerializer
    queryset = AccommodationRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserLogin(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        print("Login called in django")
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            username = request.data["username"]
            password = request.data["password"]
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("User not found")

            print("django login function to be called")
            login(request, user)
            return Response("Login Successful", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserRegister(APIView):
    def post(self, request):
        print(f"request details = {request.data}")
        print(f"request user = {request.user}")
        username = request.data["username"]
        password = request.data["password"]

        # Check if the provided username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError("User already exists")

        user_obj = User.objects.create_user(username=username, password=password)
        user_obj.save()
        return Response(status=status.HTTP_200_OK)


# @method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        print("GetCSRFToken was called and it returned a success 200")
        return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "accommodations": reverse(
                "accommodations-list", request=request, format=format
            ),
            "login": reverse("user-login", request=request),
            "logout": reverse("user-logout", request=request),
            "register": reverse("user-register", request=request),
        }
    )
