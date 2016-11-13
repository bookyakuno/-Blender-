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
	"name": "undo_and_global_undo",
	"author": "bookyakuno",
	"version": (1,0),
	"location": "ctrl + alt + Y or object.undo_and_global_undo",
	"description": "undo_and_global_undo",
	"warning": "",
	"category": "Window"}

import bpy


class undo_and_global_undo(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "object.undo_and_global_undo"
	bl_label = "undo_and_global_undo"
	bl_options = {'REGISTER', 'UNDO'}
	def execute(self, context):
		if bpy.context.user_preferences.edit.use_global_undo == False:
			bpy.context.user_preferences.edit.use_global_undo = True
			bpy.ops.ed.undo()
		else:
			bpy.ops.ed.undo()
		return {'FINISHED'}



addon_keymaps = []
def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager

	km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY')
	kmi = km.keymap_items.new(undo_and_global_undo.bl_idname, 'Y', 'PRESS', alt=True, ctrl=True)
	addon_keymaps.append((km, kmi))

def unregister():
	bpy.utils.unregister_module(__name__)
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()
