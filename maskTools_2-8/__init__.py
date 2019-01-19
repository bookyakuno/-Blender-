bl_info = {
    "name": "Mask Tools",
    "author": "Stanislav Blinov,Yigit Savtur,Bookyakuno (2.8Update)",
    "version": (0, 35,1),
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

        vgroupHeader = layout.row(align = True)
        vgroupHeader.label(text = "Vertex Group :", icon = 'GROUP_VERTEX')

        vGroupButtons = layout.row()
        vGroupButtons.operator("mesh.masktovgroup", text = "Create VGroup", icon = 'NONE')
        vGroupButtons.operator("mesh.masktovgroup_append", text = "Add", icon = 'DISCLOSURE_TRI_RIGHT')
        vGroupButtons.operator("mesh.masktovgroup_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')

        space = layout.row()

        maskHeader = layout.row(align = True)
        maskHeader.label(text = "Mask :", icon = 'MOD_MASK')

        maskButtons = layout.row()
        maskButtons.operator("mesh.vgrouptomask", text = "Create Mask", icon='NONE')
        maskButtons.operator("mesh.vgrouptomask_append", text = "Add", icon = 'DISCLOSURE_TRI_RIGHT')
        maskButtons.operator("mesh.vgrouptomask_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')

        space = layout.row()
        space = layout.row()

        maskEdgesHeader = layout.row(align = True)
        maskEdgesHeader.label(text = "Mask by Edges :", icon = 'MOD_MASK')
        maskEdgesHeader.operator("mesh.mask_from_edges", text = "Create", icon = 'NONE')

        maskEdges = layout.row(align = True)
        maskEdges.prop(bpy.context.scene,"mask_edge_angle", text = "Edge Angle",icon='MOD_MASK',slider = True)
        maskEdges.prop(bpy.context.scene,"mask_edge_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)

        space = layout.row()
        space = layout.row()

        maskCavityHeader = layout.row(align = True)
        maskCavityHeader.label(text = "Mask by Cavity:", icon = 'MOD_MASK')
        maskCavityHeader.operator("mesh.mask_from_cavity", text = "Create", icon = 'NONE')

        maskCavity = layout.row(align = True)
        maskCavity.prop(bpy.context.scene,"mask_cavity_angle", text = "Cavity Angle",icon='MOD_MASK',slider = True)
        maskCavity.prop(bpy.context.scene,"mask_cavity_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)

        space = layout.row()
        space = layout.row()

        maskCavityHeader = layout.row(align = True)
        maskCavityHeader.label(text = "Mask Smooth", icon = 'MOD_MASK')
        maskCavityHeader.operator("mesh.mask_smooth_all", text = "Smooth", icon = 'NONE')

        maskCavity = layout.row(align = False)
        maskCavity.prop(bpy.context.scene,"mask_smooth_strength", text = "Mask Smooth Strength", icon='MOD_MASK',slider = True)









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
