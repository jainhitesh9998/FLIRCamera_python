from time import sleep
import  PySpin

from capture_image.flir_camera import FLIRCamera
from capture_image.camera import Camera
#
# cam = FLIRCamera()
#
# print(cam.get_camera_count())
# print(cam.get_camera_list())

# del cam
#cam_ins = Camera(1)

system = PySpin.System.GetInstance()
cam_list = system.GetCameras()
cam = cam_list.GetByIndex(0)
cam.Init()
cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)
count = 0
cam.BeginAcquisition()
try:
    while True:
        image_primary = cam.GetNextImage()
        image_array = image_primary.GetData()
        image_primary.Save('prime{}.jpg'.format(count))
        count += 1
        sleep(0.1)
except KeyboardInterrupt:
    cam.EndAcquisition()
    cam.DeInit()
    del image_primary
    del cam
    del cam_list
    print("graceful_exit")