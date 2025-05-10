from gimpfu import *
from array import array

#!/usr/bin/env python

def generate_icon_layers(image, layer) :
    ''' Creates copies of the selected layer, scales them to all 14 Windows icon sizes (256 to 16) and adds it to the current image.
    
    Parameters:
    image : image The current image.
    layer : layer The layer of the image that is selected.
    '''
    
    resolutions = [
        256,
        96,
        80,
        72,
        64,
        60,
        48,
        40,
        36,
        32,
        30,
        24,
        20,
        16
    ]
    
    for i in resolutions:
        new_layer = layer.copy()
        new_layer.name = str(i) + "px"
        image.add_layer(new_layer, 0)
        new_layer.scale(i, i, 1)
        
    image.remove_layer(layer)
    
register(
    "python_fu_generate_icon_layers",
    "Generate Icon Layers",
    "Generate all layers needed for a proper Windows icon based on the currently selected layer",
    "Windows98",
    "Open Source",
    "2025",
    "<Image>/Layer/Generate/Generate Icon Layers",
    "*",
    [],
    [],
    generate_icon_layers)

main()