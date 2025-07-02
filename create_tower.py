# code creates basic towers using the cube entity and you can stack as many cubes as specified by num_blocks
# each cube's x and z positions are jittered randomly 


from ursina import *
import random

# TODO: need to make sure check_cog works for rotated blocks 

def check_cog(entity_b, entity_t): #b = bottom, t = top
    top_cog = entity_t.world_position

    bottom_cog = entity_b.world_position
    bottom_dim = entity_b.scale

    x_min = bottom_cog.x - bottom_dim.x / 2
    x_max = bottom_cog.x + bottom_dim.x / 2
    # z_min = bottom_cog.z - bottom_dim.z / 2
    # z_max = bottom_cog.z + bottom_dim.z / 2

    return top_cog.x >= x_min and top_cog.x <= x_max 
      
app = Ursina()

EditorCamera()


# Create a ground/base
ground = Entity(model="cube", color=color.gray, scale=(6, 0.1, 6), position=(0, -4, 0))

# Define block dimensions
block_width = 2
block_height = 1
block_depth = 1


# Number of blocks in the tower
num_blocks = 6

tower = []



# Build the tower
for i in range(num_blocks):
    
    #randomly determine if the current block should be vertical 

    is_vertical = random.random() < 0.3
    if is_vertical:
        rotation = Vec3(0, 90, 0)  
        curr_scale = Vec3(block_height, block_width, block_depth)  
    else:
        rotation = Vec3(0,0,0)
        curr_scale = Vec3(block_width,block_height,block_depth)

    if i == 0:
        block = Entity(
            model="cube",
            color=color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            scale=curr_scale,
            position=(0, ground.position.y + curr_scale.y / 2, 0),
            rotation= rotation,
            collider="box",
        )
        tower.append(block)
    else:
        while True:
            x_jitter = random.uniform(-curr_scale.x / 2, curr_scale.x / 2)  # randomly jitter the x position for each cube
            # z_jitter = random.uniform(-curr_scale.z / 2, curr_scale.z / 2)  # randomly jitter the z position for each cube

            new_x = tower[-1].position.x + x_jitter
            new_z = tower[-1].position.z 
            new_y = tower[-1].position.y + (tower[-1].scale.y / 2) + (curr_scale.y / 2)

            block = Entity(
                model="cube",
                color=color.rgb(
                    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                ),
                scale=curr_scale,
                position=(new_x, new_y, new_z),
                rotation= rotation,
                collider="box",
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
