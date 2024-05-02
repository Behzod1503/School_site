from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import jwt
from datetime import datetime, timedelta

from .serializers import UserSerializer, UserRegSerializer, UsersListSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = get_user_model().objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Bunday foydalanuvchi topilmadi')

        if not user.check_password(password):
            raise AuthenticationFailed('Login yoki parol xato, iltimos tekshirib qaytadan kiriting')

        payload = {
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes=10),
            'iat': datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.data = {
            'token': token,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }

        return response


class UserDetailView(APIView):
    # serializer_class = UserSerializer
    def get(self, request):
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise AuthenticationFailed('Send token, please')

        if not token:
            raise AuthenticationFailed('Invalid token, login again, please')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired, login again, please')
        except:
            raise AuthenticationFailed('Invalid token, login again, please')

        user = get_user_model().objects.filter(username=payload['username'], is_active=True).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UsersListView(ListAPIView):
    serializer_class = UsersListSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_TOKEN']
        except:
            raise AuthenticationFailed('Send token, please')

        if not token:
            raise AuthenticationFailed('Invalid token, login again, please')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired, login again, please')
        except:
            raise AuthenticationFailed('Invalid token, login again, please')

        queryset = get_user_model().objects.all()

        if len(self.request.GET):
            if 'name' in self.request.GET:
                queryset = queryset.filter(first_name__icontains=self.request.GET['name']) | queryset.filter(
                    last_name__icontains=self.request.GET['name'])

        return queryset


def getUserId(request):
    try:
        token = request.META['HTTP_TOKEN']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['username']
    except:
        return False


# class UserDeleteView(APIView):
#     def post(self, request):
#         try:
#             token = request.META['HTTP_TOKEN']
#         except:
#             raise AuthenticationFailed('Send token, please')
#
#         if not token:
#             raise AuthenticationFailed('Invalid token, login again, please')
#
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Token expired, login again, please')
#         except:
#             raise AuthenticationFailed('Invalid token, login again, please')
#
#         try:
#             u_id = request.data['username']
#         except:
#             return Response({'detail': 'Send username please'})
#
#         try:
#             get_user_model().objects.filter(username=u_id).update(is_active=False)
#             return Response({'detail': 'User deleted'})
#         except:
#             return Response({'detail': 'Internal server error, please try again'})


