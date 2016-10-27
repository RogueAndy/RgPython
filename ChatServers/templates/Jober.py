import datetime
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

def showJobers(request):
    list = [{id: 1, 'name': '求职者1', 'age': '23'},
            {id: 2, 'name': '求职者2', 'age': '23'},
            ]

    return render_to_response('jober.html', {'jobers': list})

@csrf_exempt
def returnforios2(request):
    print('-----调用了 returnforios 方法')
    message = ''
    if request.method == 'POST':
        print('------request method: ' + request.method)
        message = request.POST["message"]
    response_data = {
        'status': '1',
        'name': '钟灵杰',
        'qq': [111, 222],
        'message': message,
    }

    print('IOS user send a new message: ' + message)
    list = [{'content': message, 'sender': 'zlj'}]
    # return render_to_response('ChatWeb.html', {'messages': list})
    return HttpResponse(json.dumps(response_data), content_type='application/json')