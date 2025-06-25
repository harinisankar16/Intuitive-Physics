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

    return (top_cog >= x_min and top_cog <= x_max) and (top_cog>=z_min and top_cog <=z_max)
      

app = Ursina()

EditorCamera()


# Create a ground/base
ground = Entity(model="cube", color=color.gray, scale=(6, 0.1, 6), position=(0, 0, 0))

# Define block dimensions
block_width = 2
block_height = 1
block_depth = 3

# Number of blocks in the tower
num_blocks = 3

blocks = []

# Build the tower
for i in range(num_blocks):

    x_jitter = random.uniform(-block_width / 2, block_width / 2)  # randomly jitter the x position for each cube
    z_jitter = random.uniform(-block_depth / 2, block_depth / 2)  # randomly jitter the z position for each cube

    block = Entity(
        model="cube",
        color=color.rgb(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        ),
        scale=(block_width, block_height, block_depth),
        texture="brick",
        position=(x_jitter, block_height / 2 + i * block_height, z_jitter),
        rotation=(0, 0, 0),
        Collider="box",
    )

    blocks.append(block)

    print(f"cog of block{i} is within cog of block{i-1}: {check_cog(blocks[i-1],blocks[i])}")
    
        # x_jitter = random.uniform(-block_width / 2, block_width / 2)  # randomly jitter the x position for each cube
        # z_jitter = random.uniform(-block_depth / 2, block_depth / 2)  # randomly jitter the z position for each cube

print(blocks)
# #have it rotate
# def update():
#     for block in blocks:
#         block.rotation_y += 20 * time.dt


app.run()
