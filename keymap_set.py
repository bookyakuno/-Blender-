# -*- coding: utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
 
bl_info = {
    "name": "Keymap Set",
    "author": "bookyakuno",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "description": "Rational Keymap Set",
    'location': 'This addon Setting',
    "category": "UI"}
 
import bpy, os
from bpy.types import Menu, Header   
from bpy.props import IntProperty, FloatProperty, BoolProperty
import bmesh
from mathutils import *
import math
import rna_keymap_ui

 
 

class DeleteBySelectMode_x(bpy.types.Operator):
    bl_idname = "mesh.delete_by_select_mode_x"
    bl_label = "delete by mode"
    bl_description = "delete by select mode"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        mode = context.tool_settings.mesh_select_mode[:]
        if (mode[0]):
            bpy.ops.mesh.delete(type="VERT")
        elif (mode[1]):
            bpy.ops.mesh.delete(type="EDGE")
        elif (mode[2]):
            bpy.ops.mesh.delete(type="FACE")
        return {'FINISHED'}

 
 
 
 
 
 
class WazouPieMenuPrefs(bpy.types.AddonPreferences):
    """Creates the tools in a Panel, in the scene context of the properties editor"""
    bl_idname = __name__
 

    bpy.types.Scene.Enable_Tab = bpy.props.BoolProperty(default=False)

 
    def draw(self, context):
        layout = self.layout
 

        layout.prop(context.scene, "Enable_Tab", text="Keymap", icon="URL")   
        if context.scene.Enable_Tab:
            #Add the keymap in the prefs
            col = layout.column()
            kc = bpy.context.window_manager.keyconfigs.addon
            for km, kmi in addon_keymaps:
                km = km.active()
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)


addon_keymaps = []

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)
        
#------------------- REGISTER ------------------------------     

def register():
    bpy.utils.register_module(__name__)
 
 
# Keympa Config   
 
    wm = bpy.context.window_manager
 
    if wm.keyconfigs.addon:
 
 
 
 
 
 



 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Select Border >> Mouse Drag --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        

        
        #boader select        
        # 矩形選択
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY')
        kmi_props_setattr(kmi.properties, 'extend', False)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
 
        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D') 
        kmi = km.keymap_items.new('view3d.manipulator', 'SELECTMOUSE', 'PRESS', any=True)
        kmi_props_setattr(kmi.properties, 'release_confirm', True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
  
 
 
 
 
        
        #boader select  -- Gesture
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('CANCEL', 'ESC', 'PRESS', any=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        
        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('BEGIN', 'LEFTMOUSE', 'PRESS')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        
        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        
        
        
        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE', shift=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        
        
        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('DESELECT', 'LEFTMOUSE', 'RELEASE', ctrl=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))



        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.select_all', 'A', 'PRESS', oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.select_all', 'A', 'PRESS', oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))



 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Select Linked >> Double Click --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        

        
        
    	#Select Linked
        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK')
        kmi_props_setattr(kmi.properties, 'limit', True)
        kmi_props_setattr(kmi.properties, 'deselect', False)
        kmi.active = True
        addon_keymaps.append((km, kmi))


        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
        kmi_props_setattr(kmi.properties, 'limit', True)
        kmi_props_setattr(kmi.properties, 'deselect', False)
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', ctrl=True)
        kmi_props_setattr(kmi.properties, 'limit', True)
        kmi_props_setattr(kmi.properties, 'deselect', True)
        kmi.active = False
        addon_keymaps.append((km, kmi))

 
 
 
     	#UV Select Linked
        km = wm.keyconfigs.addon.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('uv.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK')
        kmi.active = True
        addon_keymaps.append((km, kmi))


        km = wm.keyconfigs.addon.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('uv.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
        kmi_props_setattr(kmi.properties, 'extend', True)
        kmi.active = True
        addon_keymaps.append((km, kmi))

 
 
 
 




 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Delete >> BACK SPACE  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        



        km = wm.keyconfigs.addon.keymaps.new('Object Mode', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('object.delete', 'BACK_SPACE', 'PRESS')        
        kmi.active = True
        addon_keymaps.append((km, kmi))

 

        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.delete_by_select_mode_x', 'BACK_SPACE', 'PRESS')
        kmi.active = True
        addon_keymaps.append((km, kmi))



        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.dissolve_mode', 'BACK_SPACE', 'PRESS', alt=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))

 






 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################ ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- View >> 1,2,3 --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
                

 
        
        
        
        # 視点変更
        
        #------------3d View

        # 1,2,3
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS')
        kmi_props_setattr(kmi.properties, 'type', 'FRONT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS')
        kmi_props_setattr(kmi.properties, 'type', 'RIGHT')
        kmi.active = True
        addon_keymaps.append((km, kmi))


        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS')
        kmi_props_setattr(kmi.properties, 'type', 'TOP')
        kmi.active = True
        addon_keymaps.append((km, kmi))


        # 1,2,3 + Ctrl
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'type', 'BACK')
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'type', 'LEFT')
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'type', 'BOTTOM')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        # align_active …… 1,2,3 + Alt 

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS', alt=True)
        kmi_props_setattr(kmi.properties, 'type', 'TOP')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS', alt=True)
        kmi_props_setattr(kmi.properties, 'type', 'RIGHT')
        kmi_props_setattr(kmi.properties, 'align_active', True)
        kmi.active = True
        addon_keymaps.append((km, kmi))

        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

        kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS', alt=True)
        kmi_props_setattr(kmi.properties, 'type', 'FRONT')
        kmi_props_setattr(kmi.properties, 'align_active', True)
        kmi.active = True
        addon_keymaps.append((km, kmi))









 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Camera  >> 4  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.viewnumpad', 'FOUR', 'PRESS')
        kmi_props_setattr(kmi.properties, 'type', 'CAMERA')
        kmi.active = True
        addon_keymaps.append((km, kmi))




        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.context_toggle', 'FOUR', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'data_path', 'space_data.lock_camera')
        kmi.active = True
        addon_keymaps.append((km, kmi))








 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Render  >> 5  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        
        
        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('render.render', 'FIVE', 'PRESS')
        kmi_props_setattr(kmi.properties, 'animation', False)
        kmi_props_setattr(kmi.properties, 'use_viewport', True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        










 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Mesh Tool --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
                





        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.knife_tool', 'Z', 'PRESS', ctrl=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))



        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('mesh.inset', 'S', 'PRESS', shift=True,alt=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))



 
 
 
 



 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Transform AXIS-Y >> C --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        





        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Transform Modal Map', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('AXIS_Y', 'C', 'PRESS', any=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        

        
        km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Transform Modal Map', space_type='EMPTY', region_type='WINDOW', modal=True)
        kmi = km.keymap_items.new_modal('PLANE_Y', 'C', 'PRESS', shift=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))
        







 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- View Rotate/move --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        

        

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D') 
        kmi = km.keymap_items.new('view3d.rotate', 'SELECTMOUSE', 'PRESS', oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))





        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.move', 'MIDDLEMOUSE', 'PRESS', oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))



 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- view all / selected  >>   --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        
        

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.view_all', 'A', 'PRESS', ctrl=True, oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('view3d.view_selected', 'A', 'PRESS', shift=True, oskey=True)
        kmi.active = True
        addon_keymaps.append((km, kmi))




 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Mode Set >> Tab  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        
        
       
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
        kmi_props_setattr(kmi.properties, 'mode', 'POSE')
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new('Pose', space_type='EMPTY', region_type='WINDOW', modal=False) 
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
        kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
 
        
#Sculpt mode        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
        kmi_props_setattr(kmi.properties, 'mode', 'SCULPT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new('Sculpt', space_type='EMPTY', region_type='WINDOW', modal=False) 
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
        kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
         
 
 
#Weight paint
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', alt=True)
        kmi_props_setattr(kmi.properties, 'mode', 'WEIGHT_PAINT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new('Weight Paint', space_type='EMPTY', region_type='WINDOW', modal=False) 
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', alt=True)
        kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
         

 
 
 
 #Texture paint        
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'mode', 'TEXTURE_PAINT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new('Image Paint', space_type='EMPTY', region_type='WINDOW', modal=False) 
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True)
        kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
         
 
#Vertex paint         
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True, alt=True)
        kmi_props_setattr(kmi.properties, 'mode', 'VERTEX_PAINT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new('Vertex Paint', space_type='EMPTY', region_type='WINDOW', modal=False) 
        kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True, alt=True)
        kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
        kmi.active = True
        addon_keymaps.append((km, kmi))
         
 
 
 
 


 # # # # # # # #
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 ################################################################  
        km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)        
        kmi = km.keymap_items.new('-- Modifier Add --', 'MINUS', 'PRESS')
        kmi.active = False
        addon_keymaps.append((km, kmi)) 
 ################################################################
 # # # # # # # #
        

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.modifier_add', 'FOUR', 'PRESS', ctrl=True, oskey=True)
        kmi_props_setattr(kmi.properties, 'type', 'MIRROR')
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.subdivision_set', 'ONE', 'PRESS', oskey=True)
        kmi_props_setattr(kmi.properties, 'level', 0)
        kmi.active = True
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('object.subdivision_set', 'THREE', 'PRESS', oskey=True)
        kmi_props_setattr(kmi.properties, 'level', 2)
        kmi.active = True
        addon_keymaps.append((km, kmi))



 
 
 
 
 # # # # # # # #
 ################################################################
 
 
 ################################################################
 # # # # # # # #





def unregister():
    bpy.utils.unregister_module(__name__)
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
        

    # clear the list
    del addon_keymaps[:]
 
if __name__ == "__main__":
    register()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
