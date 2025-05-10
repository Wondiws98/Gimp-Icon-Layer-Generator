# Gimp-Icon-Layer-Generator
A Gimp (GNU Image Manipulation Program) Python script for helping in making .ico image files for Windows applications.

Upon executing the script, it will copy the currently selected layer and scale it to all the following resolutions: 256, 96, 80, 72, 64, 60, 48, 40, 36, 32, 30, 24, 20, 16.

It will then delete the original layer, leaving you with an image containing all layers, scaled to resolutions needed for a proper Windows icon.

You can then export the image as a .ico file.

# Installation
Copy "icon-later-generator.py" into your Gimp plug-ins folder, located at "Program Files/GIMP 2/lib/gimp/2.0/plug-ins".

Make sure to restart Gimp after intalling the script.

# Using
You can find the "Generate Icon Layers" option in the "Layer" tab under "Generate".
