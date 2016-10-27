import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response

def sayHello(request):
    s = "hello world"
    current_time = datetime.datetime.now()
    html = "<html><head></head><body><h1> %s </h1><p> %s </p></body></html>" % (s, current_time)
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def showStudents(request):
    list = [{id: 1, 'name': '钟灵杰', 'age': '23'},
            {id: 2, 'name': '打完', 'age': '23'},
            {id: 3, 'name': '打的', 'age': '42'}
            ]

    return render_to_response('student.html', {'students': list})