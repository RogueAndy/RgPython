import datetime
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

def showTeachers(request):
    list = [{id: 1, 'name': '教师1', 'age': '23'},
            {id: 2, 'name': '教师2', 'age': '23'},
            ]

    return render_to_response('teacher.html', {'teachers': list})

@csrf_exempt
def returnforios(request):
    print('-----调用了 returnforios 方法')
    if request.method == 'POST':
        print('------request method: ' + request.method)

    response_data = {'status': '1'}
    # response_data = {
    #     'status': '1',
    #     'm': 'fail',
    #     'd': []
    # }
    # response_data = {'status': '1'}
    return HttpResponse(json.dumps(response_data), content_type='application/json')
    # return JsonResponse({"status": "1"})