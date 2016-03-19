import json
import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

    detect_faces(filename)

    return JsonResponse(
        {'present': ['Jan Kowalski', 'Dupa Wolowa', 'Anna Kowalska'],
         'absent': ['Twoja Stara', 'John Smith']})
