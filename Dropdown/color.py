from kivy.uix.colorpicker import ColorPicker

clr_picker = ColorPicker()
add_widget(clr_picker)
    
def on_color():
    print "RGBA = ", str(value)
    print "HSV = ", str(instance.hsv)
    print "HEX = ", str(instance.hex_color)
        
clr_picker.bind(color=on_color)
