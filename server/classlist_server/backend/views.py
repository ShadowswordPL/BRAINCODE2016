import json
import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from models import Lesson, Student
from recognition.recognizer import recognize
from segmentation.segment import detect_faces
import cv2
@csrf_exempt
def check(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    data = body['photo']

    currtime = int(time.time())
    filename = 'files/' + str(currtime) + '.png'
    fh = open('files/' + filename, 'wb')
    fh.write(data.decode('base64'))
    fh.close()

    _, _, _, faces_paths, crop_tuples = detect_faces('files/' + filename)
    students = Student.objects.all()
    ids, matched_crop_tuples = recognize(faces_paths, crop_tuples, students)

    present_students = [student.name for student in students if student.pk in ids]
    absent_students = [student.name for student in students if student.pk not in ids]
    for student in students:
        print student.pk

    image = cv2.imread('files/' + filename)
    for ((xb, yb, xe, ye), _) in matched_crop_tuples:
        cv2.rectangle(image, (xb,yb), (xe, ye), (255, 0, 255), 7)

    for ((xb, yb, _, _), sid) in matched_crop_tuples:
        cv2.putText(image, next(stud.name for stud in students if stud.pk == sid), (xb, yb), cv2.FONT_HERSHEY_SIMPLEX, 2, 3400, 5)

    cv2.imwrite('files/' + filename, image)
    lesson = Lesson()
    lesson.name = "Mathematics"
    lesson.img = filename
    lesson.save()
    for student in students:
        if student.pk in ids:
            lesson.students.add(student)
    lesson.save()

    return JsonResponse({'present': present_students, 'absent': absent_students})
