def recognize(image_paths, database):
    """Returns a list of ids of the students that were present in image_paths.
    Args:
        image_paths: Paths to images from segmentation.
        database: A list of all possible students (Student Model).
    """
    return recognizeMicrosoftFaceAPI(image_paths, database)


def recognizeMicrosoftFaceAPI(image_paths, database):
    return [1]