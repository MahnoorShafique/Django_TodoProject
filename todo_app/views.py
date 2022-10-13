from unicodedata import name
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Todo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
import json
from dateutil import parser
@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    
    def post(self, request):
        data_dict=json.loads(request.body)
        date_data = data_dict["due_date"]
        if (isinstance(date_data, str)):
            converted_date = parser.parse(date_data)
            data_str = str(converted_date)
            if len(data_str) > 10:
                    data_str = data_str[0:10]
            data_dict.update({'due_date':data_str})
        try:
            task_obj=Todo(task_name=data_dict['task_name'],due_date=data_dict['due_date'],
            description=data_dict['description'],status=data_dict['status']

            )

            task_obj.save()
            return_data={
                "msg":"Data Added successfully",
                "status":True
            }
            return JsonResponse(return_data)
        except Exception as e:
            response={
                "msg":"an error occured",
                'status':False
            }
            return JsonResponse(response)


        
        
    def get(self,request):
        id_=request.query_param('id')