import json
import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from models import Student
from recognition.recognizer import recognize
from segmentation.segment import detect_faces

@csrf_exempt
def check(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    data = body['photo']

    currtime = int(time.time())
    filename = 'tempimages/' + str(currtime) + '.png'
    fh = open(filename, 'wb')
    fh.write(data.decode('base64'))
    fh.close()

    _, _, _, faces_paths = detect_faces(filename)
    students = Student.objects.all()
    ids = recognize(faces_paths, students)
    present_students = [students[id].name for id in ids]
    absent_students = [student.name for student in students if student.pk not in ids]
    for student in students:
        print student.pk

    return JsonResponse({'present': present_students, 'absent': absent_students})
