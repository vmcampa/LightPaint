# LightPaint 
**Light painting in the Pimoroni´s unicornhat with a USB-SNES controller**<br/>  This is my first project ever other than following tutorials.<br/>

<h2> Requisitos.<br/> 
    
**Hardware:**<br/>
UnicornHat<br/>
![unicornhat](/jpgs/unicornhat.jpg)
Raspberry Pi 3<br/>
![RPi3B](/jpgs/Raspberry_Pi3.jpg)
USB SNES Controller<br/>
![SNES](/jpgs/USB_SNES_controller.jpg)

**Dependencies:**<br/>  
* Unicornhat library<br/>
    _sudo pip3 install unicornhat_<br/>
* Pygame library<br/>
    _sudo pip3 install pygame_<br/>
**Other libraries used:**<br/>
glob, json, datetime, sys<br/>

<h2> Usage:<br/> 
    
run with sudo<br/>      
_sudo python3 paint.py_<br/> 

Use **arrowkeys** to move the pencil and buttons to add a colour (**X**: blue, **Y**: green, **A**: red, **B**:yellow, **Right_Shoulder**: Black, **Left_shoulder**: white).
**Mode** to change mode between drawing and slideshow.
Whithin slideshow use **Right/Left_shoulder** to save image as json file and **start** to start/stop the slideshow.

vmc
