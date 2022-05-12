from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from agora_key.RtcTokenBuilder import RtcTokenBuilder
import requests
import json






class agora(APIView):
    def post(self, request, format=None):
        appId = '5b05a737da4e48ef97f7ef24f46d63ad'
        appCertificate ='75e6e14bdfd142db8786ccd7ec3979ea'
        channelname = 'testing'
        uid = request.data.get('123')
        role = 'host'
        privilegeExpiredTs = 40
        data = RtcTokenBuilder.buildTokenWithAccount(appId, appCertificate, channelname, uid, role, privilegeExpiredTs )
        token = {
            'data': data
        }
        return Response(token)

class imagedetect(APIView):

    def post(self, request, *args, **kwargs):
        params = {
            'models': 'nudity,wad',
            'api_user': '1101636910',
            'api_secret': 'nqapUNqQvxQn5pgCLG3s'
        }
        image = request.FILES['image']
        img = image.read()
        r = requests.post('https://api.sightengine.com/1.0/check.json', files={'media': img}, data=params)
        output = json.loads(r.text)
        print(r.text)
        if output["status"] == 'success' and output['weapon'] <=0.8 and output['nudity']['raw'] <= 0.9:
            user = Todo.objects.create(title='test', description='kdkkdkk', deadline='2022-04-05 05:45', isCompleted='True', image=image)
            user.save()
            return Response(output)
        else:
            return Response("Image contain sensitive content..!")

class TodoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Todo.objects.get(id=id)
            serializer = TodoSerializer(stu)
            return Response(serializer.data)

        stu = Todo.objects.all()
        serializer = TodoSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({
            'message':'Data created'}, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        id=pk
        stu = Todo.objects.get(pk=id)
        serializer = TodoSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message':'Updated'})

    def patch(self, request, pk, format=None):
        id = pk
        stu = Todo.objects.get(pk=id)
        serializer = TodoSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'message': 'Updated'})

    def delete(self, request, pk, format=None):
        id=pk
        stu = Todo.objects.get(pk=id)
        stu.delete()
        return Response({'message': 'Deleted'})







# class ToDoViewSet(viewsets.ViewSet):
#     def list(self, request):
#         users = Todo.objects.all()
#         serializer = TodoSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': 'Created Successfully'})
#
#     def retrieve(self, request, pk=None):
#         id =pk
#         if id is not None:
#             stu = Todo.objects.get(id=id)
#             serializer = TodoSerializer(stu)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         id=pk
#         us = Todo.objects.get(pk=id)
#         serializer = TodoSerializer(us, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': 'Updated Successfully'})
#
#     def partial_update(self, request, pk=None):
#         id = pk
#         us = Todo.objects.get(pk=id)
#         serializer = TodoSerializer(us, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': ' Partial Updated Successfully'})
#
#     def destroy(self, request, pk=None):
#         id=pk
#         us =Todo.objects.get(pk=id)
#         us.delete()
#         return Response({'message': 'Successfully Deleted'})
