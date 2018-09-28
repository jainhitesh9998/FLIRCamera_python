import  PySpin

class FLIRCamera(object):
    def __init__(self):
        self.__system = PySpin.System.GetInstance()
        self.__camera_list = self.__system.GetCameras()
        self.__camera_count = self.__camera_list.GetSize()
        self.__curr_camera_id = None
        self.__cam_list =[]
        self.__cam_params = {
            'cam_pointer': [],
            'cam_nodemap_tldevice': [],
            'cam_nodemap': []
        }
        self.__fill_cam_params()

    def __del__(self):
        for _ in self.__cam_params['cam_pointer']:
            self.__deinit_camera(_)
        self.__camera_list.Clear()
        self.__system.ReleaseInstance()
        # del self.__c1


    def __fill_cam_params(self):
        for i, cam in enumerate(self.__camera_list):
            self.__cam_params['cam_pointer'].append(cam)

            self.__cam_params['cam_nodemap_tldevice'].append(cam.GetTLDeviceNodeMap())
            FLIRCamera.init_camera(cam)
            self.__cam_params['cam_nodemap'].append(cam.GetNodeMap())

    def __initialize(self):
        pass

    def __reinitialize(self):
        pass

    def get_camera_list(self):
        return self.__camera_list

    def get_camera_count(self):
        return self.__camera_count

    @staticmethod
    def init_camera(cam_pointer):
        assert isinstance(cam_pointer, PySpin.CameraPtr)
        cam_pointer.Init()

    def __deinit_camera(self, cam_pointer):
        assert isinstance(cam_pointer, PySpin.CameraPtr)
        cam_pointer.DeInit()

    def acquire_image(self, camera_idx):
        cam_pointer = self.__cam_params['cam_pointer'][camera_idx]
        cam_nodemap = self.__cam_params['cam_nodemap'][camera_idx]
        cam_nodemap_tldevice = self.__cam_params['cam_nodemap_tldevice'][camera_idx]


