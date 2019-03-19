import logging
import json
from datetime import datetime

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView

from api.models import TestModel
from api.serializers import TestSerializer

logger = logging.getLogger(__name__)


class ListTestEntries(APIView):
	permission_classes = (permissions.AllowAny,)

	def get(self, request, tenant_name,format=None):
		all_test_instances = TestModel.objects.all()
		# Simply writing a json instead of a serializer since it's for testing
		data = {}
		for item in all_test_instances:
			data[str(item.id)] = [item.title,str(item.updated_at)]
		return Response({'message':'success','data':data})


	def post(self, request, tenant_name,format=None):
		message = 'fail'
		logger.info(str(request.method))
		if request.method == "POST":
			if request.data:
				serializer = TestSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
					message = 'success'
		return Response({'message':message})


# Signals
# Simply to test whether its saving in the correct database or not
@receiver(post_save, sender=TestModel)
def save_updated_at(sender, instance,created, **kwargs):
	if created:
		current_time = datetime.now()
		instance.updated_at=current_time
		instance.save()