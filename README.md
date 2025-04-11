# README

How it works: 

1. Get player input and check for any kind of ange.
2. Use the imput to move the player character and update all the other elements. 
3. Combine all individual images (player images, enemy images, ui, etc).
4. Show the final frame to the player. 

Pygame: 

* Displays graphics and plays sounds. 
* Gets imput (keyboard, mouse, controller, etc).
* Check collisions. 
* Provides additionalk minor tools (repeat timers, image manipulation, show text).

More tools: 

* Expand tools
* Tiled level editor 
* Pymunk physics
* PIL for image manipulation 
* Sockets for multiplayer 
* Perlin-noise for random worlds 

Install: 

```python 
pip install pygame
```

Term | Explanation|--- 
---|---|--- 
Surface | Any graphics. Only visible if on the display surface.| Import img, create imge, create text.  
Display surface | Base for all other images on it. Only one in a game?|--- 
Import image | `pygame.image.load(path)` | Convert for performance 
