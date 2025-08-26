from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserFilterView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'fullname',
                openapi.IN_QUERY,
                description="Filtra usuários pelo nome.",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description="Filtra usuários por e-mail.",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'adress',
                openapi.IN_QUERY,
                description="Filtra usuários por endereço.",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'phone',
                openapi.IN_QUERY,
                description="Filtra usuários por telefone.",
                type=openapi.TYPE_STRING
            ),
        ],
        responses={200: UserSerializer(many=True)}
    )

    def get(self, request):
        fullname = request.query_params.get("fullname", None)
        email = request.query_params.get("email", None)
        adress = request.query_params.get("adress", None)
        phone = request.query_params.get("phone", None)

        users = User.objects.all()

        if fullname:
            users = users.filter(fullname__icontains=fullname)
        if email:
            users = users.filter(email__icontains=email)
        if adress:
            users = users.filter(adress__icontains=adress)
        if phone:
            users = users.filter(phone__icontains=phone)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)