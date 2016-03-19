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
    print "Request started. Segmenting..."
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

    image = cv2.imread('files/' + filename)
    for ((xb, yb, xe, ye), _) in matched_crop_tuples:
        cv2.rectangle(image, (xb,yb), (xe, ye), (213, 72, 211), 7)

    for ((xb, yb, xe, _), sid) in matched_crop_tuples:
        xc = (xb + xe) / 2
        text = next(stud.name for stud in students if stud.pk == sid)
        fontSize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, thickness=5)
        print fontSize
        print xc
        offset = fontSize[0][0] / 2
        cv2.putText(image, text, (max(0, xc - offset), yb), cv2.FONT_HERSHEY_DUPLEX, 2, (171, 15, 169), 5)

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
