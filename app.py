import time
import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)
cap = cv2.VideoCapture(0)
@app.route('/',methods=['GET'])
def index():
    """Video streaming home page. """
    return render_template('index.html')


def gen():
    """Video streaming generator function."""

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        """Write Code to make changes to image"""
        if ret == True:
            img = cv2.resize(img, (0,0), fx=1, fy=1)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break


@app.route('/video_feed',methods=['GET'])
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
