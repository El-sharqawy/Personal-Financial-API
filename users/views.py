from .models import CustomUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserBalanceView(APIView):
    queryset = CustomUser.objects.all()

    def get(self, request):
        try:
            username = request.user.username
            balance = request.user.current_balance
        except:
           username = "No User Selected, Please Login"
           balance = 0
        return Response({"username": username,"balance": balance})
