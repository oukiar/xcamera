#!/usr/bin/env python
from kivy.app import App
from kivy.lang import Builder

kv = """
#:import XCamera kivy_garden.xcamera.XCamera

FloatLayout:
    orientation: 'vertical'

    XCamera:
        id: xcamera
        on_picture_taken: app.picture_taken(*args)
        play: True
    BoxLayout:
        orientation: "vertical"
        size_hint: 1, None
        height: sp(100)
        spacing: sp(5)
        ToggleButton:
            text: "Flash"
            on_release: xcamera.set_flashlight(self.state != "normal")
        
        BoxLayout:
            orientation: 'horizontal'

            Button:
                text: 'Set landscape'
                on_release: xcamera.force_landscape()

            Button:
                text: 'Restore orientation'
                on_release: xcamera.restore_orientation()
"""


class CameraApp(App):
    def build(self):
        return Builder.load_string(kv)

    def picture_taken(self, obj, filename):
        print('Picture taken and saved to {}'.format(filename))


def main():
    CameraApp().run()


if __name__ == '__main__':
    main()
