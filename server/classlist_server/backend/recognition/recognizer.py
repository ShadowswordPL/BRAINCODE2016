import json
import time
import urllib2


def recognize(image_paths, crop_tuples, database):
    """Returns a list of ids of the students that were present in image_paths.
    Args:
        image_paths: Paths to images from segmentation.
        database: A list of all possible students (Student Model).
    """
    return recognizeMicrosoftFaceAPI(image_paths, crop_tuples,  database)


def rate_limit_wait():
    time.sleep(61.0)


def recognizeMicrosoftFaceAPI(image_paths, crop_tuples, database):
    super_secret_key = '79f6c1631a2a41ddac1deb21783dee22'

    success = False
    while not success:
        mapping = dict(zip(image_paths, crop_tuples))
        result = set()
        matched_crop_tuples = set()
        try:
            for img in image_paths:
                # Call DetectFace
                with open(img, 'rb') as f:
                    # Nie wydzielaj nic z kodu stary, 'WYBUCHNIEEEEE'
                    data = f.read()
                    req = urllib2.Request('https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true')
                    req.add_header('Content-Type', 'application/octet-stream')
                    req.add_header('Ocp-Apim-Subscription-Key', super_secret_key)
                    try:
                        response = urllib2.urlopen(req, data)
                    except urllib2.HTTPError, e:
                        print e.read()
                        rate_limit_wait()
                        response = urllib2.urlopen(req, data)
                    resp = response.read()
                    print resp

                    resp_parsed = json.loads(resp)
                    if not resp_parsed:
                        continue  # false positive

                    face_id = json.loads(resp)[0]['faceId']
                    # X-Call Verify on all from      database
                    face_ids = [(student.msFaceId, student.pk) for student in database]

                    for (id, sid) in face_ids:
                        # Verify call
                        req = urllib2.Request('https://api.projectoxford.ai/face/v1.0/verify')
                        req.add_header('Content-Type', 'application/json')
                        req.add_header('Ocp-Apim-Subscription-Key', super_secret_key)
                        d = {'faceId1' : face_id, 'faceId2' : id}
                        print d
                        try:
                            response = urllib2.urlopen(req, json.dumps(d))
                        except urllib2.HTTPError, e:
                            print e.read()
                            rate_limit_wait()
                            response = urllib2.urlopen(req, json.dumps(d))

                        resp = response.read()
                        print resp
                        resp_parsed = json.loads(resp)

                        if resp_parsed['isIdentical'] or resp_parsed['confidence'] >= 0.42:
                            print 'MATCH'
                            result.add(sid)
                            matched_crop_tuples.add((mapping[img], sid))
                            face_ids.remove((id, sid))
                            break

            success = True
        except Exception, e:
            pass

    print list(result), list(matched_crop_tuples)
    return list(result), list(matched_crop_tuples)