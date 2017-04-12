#0.0

import bpy
import os
import re

from mathutils import Vector
C = bpy.context
D = bpy.data
scn = C.scene

'''
#guess_select
recomp = re.compile(r'')
'''

def no_ext(base, obn):
    '''check without '.L' extention, loose'''
    if base.rsplit('.', 1)[0] in obn.rsplit('.', 1)[0]:
        return(obn.rsplit('.', 1)[0])


def check(fn, base, pool):
    print ('comparing with base:', fn(base,base))

    if bpy.context.mode in ('POSE'):
        #recreatelist from pose to edit
        #pool = [C.object.data.bones[b.name] for b in pool]
        for ob in pool:
            bpy.ops.object.mode_set(mode='EDIT')
            if fn(base, ob.name):
                ob.select_head = True
                ob.select_tail= True
                ob.select = True
            bpy.ops.object.mode_set(mode='POSE')

    elif bpy.context.mode in ('EDIT_ARMATURE'):
        for ob in pool:
            if fn(base, ob.name):
                ob.select_head = True
                ob.select_tail= True
                ob.select = True

    elif bpy.context.mode in ('OBJECT'):
        for ob in pool:
            if fn(base, ob.name):
                ob.select = True


pool = False

if bpy.context.mode in ('POSE'):
    act = C.active_pose_bone
    pool = [o for o in C.object.data.pose.bones[:]]#[o for o in C.selected_pose_bones]

elif bpy.context.mode in ('EDIT_ARMATURE'):
    act = C.active_bone
    pool = [o for o in C.object.data.edit_bones[:]]#[o for o in C.selected_bones]

elif bpy.context.mode in ('OBJECT'):
    act = C.active_object
    pool = [o for o in C.selectable_objects]#[o for o in C.selected_objects]
else:
    pass

#get name
base = act.name

if pool:
    check(no_ext, base, pool)

else:
    print('no selection')
