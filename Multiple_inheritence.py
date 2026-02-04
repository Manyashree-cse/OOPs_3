class Camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality
    def display_camera_details(self):
        print("the quality of camera:",self.camera_quality)

class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality
    def display_music_details(self):
        print("the music details are:",self.sound_quality)

class SmartPhone(Camera,MusicPlayer):
    def __init__(self,brand,camera_quality,sound_quality):
        self.brand=brand
        Camera.__init__(self, camera_quality)    #Inheritance order (MRO)
        MusicPlayer.__init__(self, sound_quality)  #super() only calls the first parent class in the inheritance order.

    def display_smartphone_details(self):
        print("the brand is:",self.brand)
        print("the quality of camera:",self.camera_quality)
        print("the music details are:",self.sound_quality)

obj_smart_phone=SmartPhone("manya","avg","good")
obj_smart_phone.display_smartphone_details()
obj_smart_phone1=SmartPhone("manya","avg","good")
obj_smart_phone1.display_music_details()
obj_smart_phone1.display_camera_details()