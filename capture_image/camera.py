import PySpin
class Camera:
    def __init__(self, camera):
        assert isinstance(camera, PySpin.CameraPtr)
        self.__camera_obj = camera
        # self.__device_tl_node_map = self.__camera_obj.GetTLDeviceNodeMap()
        # self.__node_map = self.__camera_obj.GetNodeMap()

    # def __del__(self):
    #     del self.__camera_obj