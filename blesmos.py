import bpy
import math

def func(x):
    return math.sin(x)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

rad = 8
res = 8

res *= rad

bpy.ops.mesh.primitive_grid_add(x_subdivisions=res, y_subdivisions=res, size=rad, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

for object in bpy.data.objects:
    for vert in object.data.vertices:
        x = vert.co[0]
        y = vert.co[1]
        vert.co[2] = func(x) + func(y)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.delete(type='ONLY_FACE')
bpy.ops.object.editmode_toggle()
bpy.ops.object.shade_smooth(use_auto_smooth=True)


"""bpy.ops.object.editmode_toggle()
bpy.ops.object.modifier_add(type='SKIN')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.object.skin_root_mark()
bpy.ops.transform.skin_resize(value=(0.139442, 0.139442, 0.139442), orient_type='GLOBAL')
bpy.ops.object.editmode_toggle()"""
