import json
import urllib2


def recognize(image_paths, database):
    """Returns a list of ids of the students that were present in image_paths.
    Args:
        image_paths: Paths to images from segmentation.
        database: A list of all possible students (Student Model).
    """
    return recognizeMicrosoftFaceAPI(image_paths, database)


def recognizeMicrosoftFaceAPI(image_paths, database):
    super_secret_key = '79f6c1631a2a41ddac1deb21783dee22'
    result = set()

    for img in image_paths:
        # Call DetectFace
        with open(img, 'rb') as f:
            data = f.read()
            req = urllib2.Request('https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true')
            req.add_header('Content-Type', 'application/octet-stream')
            req.add_header('Ocp-Apim-Subscription-Key', super_secret_key)
            try:
                response = urllib2.urlopen(req, data)
            except urllib2.HTTPError, e:
                print e.read()
            resp = response.read()
            print resp

            face_id = json.loads(resp)[0]['faceId']
            # X-Call Verify on all from      database
            face_ids = [(student.msFaceId, student.pk) for student in database]

            for (id, sid) in face_ids:
                # Verify call
                req = urllib2.Request('https://api.projectoxford.ai/face/v1.0/verify')
                req.add_header('Content-Type', 'application/json')
                req.add_header('Ocp-Apim-Subscription-Key', super_secret_key)
                try:
                    dict = {'faceId1' : face_id, 'faceId2' : id}
                    print dict
                    response = urllib2.urlopen(req, json.dumps(dict))
                except urllib2.HTTPError, e:
                    print e.read()
                resp = response.read()
                print resp
                resp_parsed = json.loads(resp)

                if resp_parsed['isIdentical']:
                    print 'MATCH'
                    result.add(sid)
                    face_ids.remove((id, sid))
                    break

    print list(result)
    return list(result)