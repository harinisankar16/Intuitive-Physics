# code creates basic towers using the cube entity and you can stack as many cubes as specified by num_blocks
# each cube's x and z positions are jittered randomly 


from ursina import *
import random

def check_cog(entity_b, entity_t):
    top_cog = entity_t.world_position

    bottom_cog = entity_b.world_position
    bottom_dim = entity_b.scale

    x_min = bottom_cog.x - bottom_dim.x / 2
    x_max = bottom_cog.x + bottom_dim.x / 2
    z_min = bottom_cog.z - bottom_dim.z / 2
    z_max = bottom_cog.z + bottom_dim.z / 2

    return (top_cog.x >= x_min and top_cog.x <= x_max) and (top_cog.z >= z_min and top_cog.z <=z_max)
      

app = Ursina()

EditorCamera()


# Create a ground/base
ground = Entity(model="cube", color=color.gray, scale=(6, 0.1, 6), position=(0, 0, 0))

# Define block dimensions
block_width = 2
block_height = 1
block_depth = 3

# Number of blocks in the tower
num_blocks = 6

tower = []

# Build the tower
for i in range(num_blocks):
    if i == 0:
        block = Entity(
            model="cube",
            color=color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            scale=(block_width, block_height, block_depth),
            texture="brick",
            position=(0, block_height / 2, 0),
            rotation=(0, 0, 0),
            collider="box",
        )
        tower.append(block)
    else:
        while True:
            x_jitter = random.uniform(-block_width / 2, block_width / 2)  # randomly jitter the x position for each cube
            z_jitter = random.uniform(-block_depth / 2, block_depth / 2)  # randomly jitter the z position for each cube

            new_x = tower[-1].position.x + x_jitter
            new_z = tower[-1].position.z + z_jitter
            new_y = block_height / 2 + i * block_height

            block = Entity(
                model="cube",
                color=color.rgb(
                    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                ),
                scale=(block_width, block_height, block_depth),
                texture="brick",
                position=(new_x, new_y, new_z),
                rotation=(0, 0, 0),
                Collider="box",
            )

            if check_cog(tower[-1], block):
                tower.append(block)
                break
            else: 
                destroy(block)


    print(f"cog of block{i} is within cog of block{i-1}: {check_cog(tower[-1],tower[i])}")
    
        
# print(blocks)
# #have it rotate
# def update():
#     for block in blocks:
#         block.rotation_y += 20 * time.dt


app.run()
