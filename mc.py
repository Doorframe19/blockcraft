from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
block_chosen = 1
def update():
    global block_chosen
    if held_keys['1']: block_chosen = 1
    if held_keys['2']:
        block_chosen = 2
    if held_keys['3']: block_chosen = 3
    if held_keys['4']: block_chosen = 4
class Voxel(Button):
    def __init__(self,chosentexture = grass_texture, position = (0,0,0)):


        super().__init__(

            parent = scene,
            position = position,
        
            model = 'assets/block',
            origin_y =0.5,
            texture = chosentexture,
            color = color.white,
            
            scale = 0.49999999999999999999999999


        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_chosen == 1:
                    mytexture = grass_texture
                elif block_chosen == 2:
                    mytexture = dirt_texture
                elif block_chosen == 3:
                    mytexture = stone_texture
                elif block_chosen == 4:
                    mytexture = brick_texture

                voxel = Voxel(mytexture,position = self.position + mouse.normal) 
            if key == 'right mouse down':
                destroy(self)             

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
app.run()