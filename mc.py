from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
block_chosen = 1
chosenblockhp = 1
def update():
    global block_chosen
    if held_keys['1']: block_chosen = 1
    if held_keys['2']:
        block_chosen = 2
    if held_keys['3']: block_chosen = 3
    if held_keys['4']: block_chosen = 4
class Voxel(Button):
    def __init__(self,chosentexture = grass_texture,blockhp = 1,position = (0,0,0)):
        self.blockhp = blockhp

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
                    chosenblockhp = 3
                elif block_chosen == 2:
                    mytexture = dirt_texture
                    chosenblockhp = 4
                elif block_chosen == 3:
                    mytexture = stone_texture
                    chosenblockhp = 6
                elif block_chosen == 4:
                    mytexture = brick_texture
                    chosenblockhp = 5

                voxel = Voxel(mytexture, blockhp = chosenblockhp,position = self.position + mouse.normal) 
            if key == 'right mouse down':
                self.blockhp-=1
            if self.blockhp==0:
                destroy(self)
for z in range(20):
    for x in range(20):
        voxel = Voxel(blockhp = 30,position = (x,0,z))
player = FirstPersonController()
app.run()