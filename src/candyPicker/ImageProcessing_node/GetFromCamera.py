#!/usr/bin/env python
class GetFromCamera():
    def get_from_webcam(self):
        """
        Fetches an image from the webcam
        """
        print "try fetch from webcam..."
        stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
        bytes=''
        bytes+=stream.read(64500)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
    
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
            return i
        else:
            print "did not receive image, try increasing the buffer size in line 13:"
        