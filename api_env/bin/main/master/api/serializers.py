from rest_framework import serializers
from master.models import Master

class MasterSerializer(serializers.ModelSerializer):
	class Meta():
		model = Master
		fields = '__all__'


