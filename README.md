# LightPaint 
**Light painting in the Pimoroni´s unicornhat with a USB-SNES controller**  
This is my first project ever other than following tutorials.  

**Requisitos.**
    
**Hardware:**  
UnicornHat  
![unicornhat](/jpgs/unicornhat.jpg)
Raspberry Pi 3  
![RPi3B](/jpgs/Raspberry_Pi3.jpg)
USB SNES Controller  
![SNES](/jpgs/USB_SNES_controller.jpg)

**Dependencies:**  
* Unicornhat library  
    _sudo pip3 install unicornhat_  
* Pygame library  
    _sudo pip3 install pygame_  
**Other libraries used:**  
glob, json, datetime, sys  

**Usage:**   
run with sudo        
**_sudo python3 paint.py_**   

Use **arrowkeys** to move the pencil and buttons to add a colour (**X**: blue, **Y**: green, **A**: red, **B**:yellow, **Right_Shoulder**: Black, **Left_shoulder**: white).
**Mode** to change mode between drawing and slideshow.
Whithin slideshow use **Right/Left_shoulder** to save image as json file and **start** to start/stop the slideshow.  

vmc 
