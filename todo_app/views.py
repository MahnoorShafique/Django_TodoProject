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
from django.core import serializers
@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    
    def post(self, request):
        data_dict=json.loads(request.body)
        date_data = data_dict["due_date"]
        keys=[*data_dict]
        # if set(keys) in {"task_name","description","due_date"}:
        if (isinstance(date_data, str)):
            converted_date = parser.parse(date_data)
            data_str = str(converted_date)
            if len(data_str) > 10:
                    data_str = data_str[0:10]
            data_dict.update({'due_date':data_str})
        try:

            task_obj = Todo.objects.create(**data_dict)
    
            # task_obj=Todo(task_name=data_dict['task_name'],due_date=data_dict['due_date'],
            # description=data_dict['description'],status=data_dict.get('status'))

            # task_obj.save()
            return_data={
                "msg":f'Data added against {task_obj.task_id}',
                "status":True
            }
            return JsonResponse(return_data)
        except Exception as e:
            response={
                "msg":"an error occured",
                'status':False
            }
            return JsonResponse(response)
        # else:
        #      response={
        #             "msg":"Params missing",
        #             'status':False
        #         }
        #      return JsonResponse(response)


        
        
    def get(self,request):
        id_=request.GET.get('id')
        if id_ is not None:
            obj=Todo.objects.filter(task_id=id_)       
        else:
            obj=Todo.objects.all()
        qs_json = serializers.serialize('json', obj)
        return HttpResponse(qs_json, content_type='application/json')
    def patch(self,request):
        id_=request.GET.get('id')
        data_dict=json.loads(request.body)
        date_data = data_dict.get("due_date",0)
        try:
            if (isinstance(date_data, str)):
                converted_date = parser.parse(date_data)
                data_str = str(converted_date)
                if len(data_str) > 10:
                        data_str = data_str[0:10]
                data_dict.update({'due_date':data_str})
            if id_ is not None:
                model_obj=Todo.objects.get(task_id=id_)
                for attr, value in data_dict.items():
                        setattr(model_obj, attr, value)
                model_obj.save()
                return_data={
                    "msg":f'Data updated against {model_obj.task_name}',
                    "status":True
                }
                return JsonResponse(return_data)
        except Exception as e:
            return {}
    def delete(self,request):
        id_=request.GET.get('id')
        try:
            obj=Todo.objects.get(task_id=id_)
            if obj:
                obj.delete()
                response={
                    "msg":"Data with id :{} deleted successfully".format(obj.task_id)
                }
            else:
                response={
                    "msg":"NO id found in db"
                }
            return HttpResponse(response, content_type='application/json')      
        except Exception as e:
              response={
                    "msg":"Id does not exists in db"
                }
              return JsonResponse(response)
       
              
        
        

