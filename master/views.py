from rest_framework import generics , mixins
from master.models import Master
from .serializers import MasterSerializer

class MasterApi(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field            = 'pk'
    serializer_class        = MasterSerializer

    def get_queryset(self):
        return Master.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request ,*args ,**kwargs)

class MasterRud(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MasterSerializer


    def get_queryset(self):
        return Master.objects.all()
    

