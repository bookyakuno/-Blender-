# 3D Navigation_x TOOLBAR v1.2 - 3Dview Addon - Blender 2.5x
#
# THIS SCRIPT IS LICENSED UNDER GPL, 
# please read the license block.
#
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
    "name": "PLAY & HIDE",
    "author": "bookyakuno",
    "version": (1),
    "location": "Please setting HotKey object.play_hide ",
    "description": "Animation play & Rendering Only",
    "warning": "",
    "category": "3D View"}

# import the basic library
import bpy




class play_hide(bpy.types.Operator):
    bl_idname = "object.play_hide"
    bl_label = "PLAY & HIDE"



    def execute(self, context):

        

        if (bpy.context.screen.is_animation_playing == False):
            	bpy.context.space_data.show_only_render = True
            	bpy.ops.screen.animation_play(reverse=False, sync=False)
        
        else:
            	bpy.context.space_data.show_only_render = False
            	bpy.ops.screen.animation_play(reverse=False, sync=False)

        

        return {'FINISHED'}





# register the class
def register():
    bpy.utils.register_module(__name__)
 
    pass 

def unregister():
    bpy.utils.unregister_module(__name__)
 
    pass 

if __name__ == "__main__": 
    register()
