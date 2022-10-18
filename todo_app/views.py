from django.core import serializers
from dateutil import parser
import json
import logging
from unicodedata import name

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Todo

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    """Creating todo model"""

    def post(self, request):
        data_dict = json.loads(request.body)
        date_data = data_dict["due_date"]
        if (isinstance(date_data, str)):

            converted_date = parser.parse(date_data)
            data_str = str(converted_date)
            if len(data_str) > 10:
                data_str = data_str[0:10]
            data_dict.update({'due_date': data_str})
        try:

            task_obj = Todo.objects.create(**data_dict)
            return_data = {
                "msg": f'Data added against {task_obj.task_id}',
                "status": True
            }
            return JsonResponse(return_data)
        except Exception as e:
            logger.error(str(e))
            response = {
                "msg": "an error occured",
                'status': False
            }

            return JsonResponse(response)

    def get(self, request):
        """ Fetching all records or single records"""
        id_ = request.GET.get('id')
        try:
            if id_ is not None:
                obj = Todo.objects.filter(task_id=id_)
            else:
                obj = Todo.objects.all()
            qs_json = serializers.serialize('json', obj)
            return HttpResponse(qs_json, content_type='application/json')
        except Exception as e:
            logger.error(str(e))
            response = {
                "msg": str(e),
                "status": True
            }
            return JsonResponse(response)

    def patch(self, request):
        """Updating some records"""
        id_ = request.GET.get('id')
        data_dict = json.loads(request.body)
        date_data = data_dict.get("due_date", 0)
        try:
            if (isinstance(date_data, str)):
                converted_date = parser.parse(date_data)
                data_str = str(converted_date)
                if len(data_str) > 10:
                    data_str = data_str[0:10]
                data_dict.update({'due_date': data_str})
            if id_ is not None:
                model_obj = Todo.objects.get(task_id=id_)
                for attr, value in data_dict.items():
                    setattr(model_obj, attr, value)
                model_obj.save()
                return_data = {
                    "msg": f'Data updated against {model_obj.task_name}',
                    "status": True
                }
                return JsonResponse(return_data)
        except Exception as e:
            logger.error(str(e))
            return {}

    def delete(self, request):
        """"Deleting rocord based on its id. """
        id_ = request.GET.get('id')
        try:
            obj = Todo.objects.get(task_id=id_)
            if obj:
                obj.delete()
                response = {
                    "msg": "Data with id :{} deleted successfully".format(obj.task_id)
                }
            else:
                response = {
                    "msg": "NO id found in db"
                }
            return HttpResponse(response, content_type='application/json')
        except Exception as e:
            logger.error(str(e))
            response = {
                "msg": "Id does not exists in db"
            }
            return JsonResponse(response)
