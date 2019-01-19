bl_info = {
    "name": "Mask Tools",
    "author": "Stanislav Blinov,Yigit Savtur,Bookyakuno (2.8Update)",
    "version": (0, 36,0),
    "blender": (2, 80,0),
    "location": "3d View > Properties shelf (N) > Sculpt",
    "description": "Tools for Converting Sculpt Masks to Vertex groups",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Sculpting"}



import bpy

from .maskToVGroup import *
from .vgroupToMask import *
from .maskFromCavity import *




from mathutils import Vector

import bmesh
import bpy
import collections
import mathutils
import math
from bpy_extras import view3d_utils
from bpy.types import (
        Operator,
        Menu,
        Panel,
        PropertyGroup,
        AddonPreferences,
        )
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        )











# import maskToVGroup
# import vgroupToMask
# import maskFromCavity

# maskToVGroup.register()
# vgroupToMask.register()
# maskFromCavity.register()

class MaskToolsPanel(Panel):
    """Creates a Mask Tool Box in the Viewport Tool Panel"""
    bl_category = "Sculpt"
    bl_idname = "MESH_OT_masktools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Mask Tools"



    def draw(self, context):
        layout = self.layout

        ###############################################################
        row = layout.row(align = True)
        row.label(text = "Vertex Group :", icon = 'GROUP_VERTEX')
        row = layout.row(align = True)
        row.label(text = "Save Mask to VGroup")

        row = layout.row()
        row.scale_y = 1.3
        row.operator("mesh.masktovgroup", text = "Create VGroup", icon = 'GROUP_VERTEX')
        row = layout.row(align = True)
        row.operator("mesh.masktovgroup_append", text = "Add VGroup", icon = 'EXPORT')
        row.operator("mesh.masktovgroup_remove", text = "Difference VGroup", icon = 'UNLINKED')

        space = layout.row()

        ###############################################################
        row = layout.row(align = True)
        row.label(text = "Mask :", icon = 'MOD_MASK')
        row = layout.row(align = True)
        row.label(text = "Import VGroup to Mask ")



        row = layout.row(align = True)
        row.scale_y = 1.3
        row.operator("mesh.vgrouptomask_append", text = "Add", icon = 'IMPORT')
        row.operator("mesh.vgrouptomask_remove", text = "Difference", icon = 'UNLINKED')
        row = layout.row()
        row.operator("mesh.vgrouptomask", text = "New Mask", icon='NONE')

        space = layout.row()

        row = layout.row(align = True)
        row.label(text = "Mask Smooth/Sharp :", icon = 'MOD_SMOOTH')

        row = layout.row(align = True)
        # row.label(text = "Mask Smooth", icon = 'MOD_MASK')
        row.scale_y = 1.3
        row.operator("mesh.mask_smooth_all", text = "Smooth", icon = 'MOD_SMOOTH')
        row.operator("mesh.mask_sharp", text = "Sharp", icon = 'IMAGE_ALPHA')

        row = layout.row(align = False)
        row.prop(bpy.context.scene,"mask_smooth_strength", text = "Mask Smooth Strength", icon='MOD_MASK',slider = True)


        space = layout.row()



        ###############################################################
        row = layout.row(align = True)
        row.label(text = "Mask Fat/Less :", icon = 'ONIONSKIN_ON')
        row = layout.row(align = True)
        row.scale_y = 1.3
        row.operator("mesh.mask_fat", text = "Mask Fat", icon = 'KEY_HLT')
        row.operator("mesh.mask_less", text = "Mask Less", icon = 'KEY_DEHLT')

        row = layout.row(align = True)
        row.prop(bpy.context.scene,"mask_fat_repeat", text = "Mask Fat Repeat", icon='MOD_MASK',slider = True)
        row.prop(bpy.context.scene,"mask_less_repeat", text = "Mask Less Repeat", icon='MOD_MASK',slider = True)

        space = layout.row()

        ###############################################################
        row = layout.row(align = True)
        row.label(text = "Mask Edge/Cavity :", icon = 'EDGESEL')


        row = layout.row(align = True)
        # row.label(text = "Mask by Edges :", icon = 'MOD_MASK')
        row.scale_y = 1.3
        row.operator("mesh.mask_from_edges", text = "Mask by Edges", icon = 'EDGESEL')

        row = layout.row(align = True)
        row.prop(bpy.context.scene,"mask_edge_angle", text = "Edge Angle",icon='MOD_MASK',slider = True)
        row.prop(bpy.context.scene,"mask_edge_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)

        space = layout.row()
        space = layout.row()

        row = layout.row(align = True)
        # row.label(text = "Mask by Cavity:", icon = 'MOD_MASK')
        row.scale_y = 1.3
        row.operator("mesh.mask_from_cavity", text = "Mask by Cavity", icon = 'STYLUS_PRESSURE')

        row = layout.row(align = True)
        row.prop(bpy.context.scene,"mask_cavity_angle", text = "Cavity Angle",icon='MOD_MASK',slider = True)
        row.prop(bpy.context.scene,"mask_cavity_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)

        space = layout.row()
        space = layout.row()



        ###############################################################
        # row = layout.row(align = True)
        # row.label(text = "Mask Misc :", icon = 'FORCE_VORTEX')
        #
        # space = layout.row()
        # row = layout.row(align = True)
        # row.operator("mesh.mask_sharp_thick", text = "Mask Sharp (Thick)", icon = 'NONE')
        # row = layout.row(align = True)
        # maskCavity = layout.row(align = False)
        # maskCavity.prop(bpy.context.scene,"mask_sharp_thick", text = "Mask Sharp Thick Strength", icon='MOD_MASK',slider = True)
        #
        # space = layout.row()
        # row = layout.row(align = True)
        # row.operator("mesh.duplicate", text = "Mask Duplicate")








classes = {
MaskToolsPanel,


MaskToVertexGroup,
MaskToVertexGroupAppend,
MaskToVertexGroupRemove,

VertexGroupToMask,
VertexGroupToMaskAppend,
VertexGroupToMaskRemove,

MaskFromCavity,
MaskFromEdges,
MaskSmoothAll,
MaskFat,
MaskLess,
MaskSharp,
MaskSharpThick,
MaskDuplicate,
}


def register():

	for cls in classes:
		bpy.utils.register_class(cls)

def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)


	if __name__ == "__main__":
		register()


#
#
# def register():
#
#     bpy.utils.register_module(__name__)
#
#
#
# def unregister():
#     bpy.utils.unregister_module(__name__)
#
#
# if __name__ == "__main__" :
# 	register()
