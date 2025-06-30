from ursina import *


# function to flip if block is vertical or horizontal



# function to find center of gravity of a cube or cube-like object
# if cog of top block is within the size of the bottom block, returns true/false

def check_cog(entity_b, entity_t):
    top_cog = entity_t.world_position #why world position instead of position

    bottom_cog = entity_b.world_position
    bottom_dim = entity_b.scale

    x_min = bottom_cog.x - bottom_dim.x / 2 #min x value possible based on bottom cube location and cog
    x_max = bottom_cog.x + bottom_dim.x / 2 #max x value possible based on bottom cube location and cog
    z_min = bottom_cog.z - bottom_dim.z / 2
    z_max = bottom_cog.z + bottom_dim.z / 2

    return (top_cog.x >= x_min and top_cog.x <= x_max) and (top_cog.z >=z_min and top_cog.z <=z_max)
      


