from ursina import *

# def update():
#     firstCube.rotation_y += 20 * time.dt

# app = Ursina()

# firstCube = Entity(model = 'cube',
#                    color = color.rgb(0,0,255),
#                    texture = 'brick',
#                    position = (0,0,0),
#                    rotation = (0,0,0),
#                    )

# firstFloor =  Entity(model=Plane(subdivisions=(3,6)), color = color.rgb(0,0,0), texture='brick', position = (0,0,0))

# app.run()

# urisna coordinate system 
# https://www.ursinaengine.org/coordinate_system.html

#             y (up)
#             |
#             |
# (forward) z |
#           \ |
#            \|
#             *---------- x (right)

# ─────────────────────────────────────
# 📌 Ursina Vec3 Reference Card from chatgpt 🧱
# ─────────────────────────────────────

# 🎯 Create a vector
v = Vec3(1, 2, 3)

# 📍 Access components
v.x, v.y, v.z

# 🛠 Modify components
v.y = 10

# 🎲 Unpack
x, y, z = v

# ➕ Math
v + Vec3(1,0,0)
v * 2
-v

# 🔍 Vector ops
v.length()
v.normalized()
v.distance_to(Vec3(0,0,0))
v.dot(Vec3(1,0,0))
v.cross(Vec3(0,1,0))

# 📦 Clone
v.copy()

# 🧭 Built-in directions
Vec3.forward() = (0,0,1)
Vec3.back()    = (0,0,-1)
Vec3.right()   = (1,0,0)
Vec3.left()    = (-1,0,0)
Vec3.up()      = (0,1,0)
Vec3.down()    = (0,-1,0)

# 🔄 Convert from list/tuple
v = Vec3(*[1,2,3]) or Vec3(*(1,2,3))

# 🌀 Rotate around axis
v.rotate_around(axis=Vec3.up(), angle=90)

# 🧠 Note: Don’t compare full Vec3 to a float
# ❌ if v >= 5
# ✅ if v.x >= 5

# 🧱 Use with entity
cube = Entity(position=Vec3(0,1,0))
cube.position += Vec3.up()

# 📦 Equality check with tolerance
v.approx(Vec3(1,2,3), tolerance=0.1)

# ─────────────────────────────────────
