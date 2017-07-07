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

bl_info = {
	"name": "Repeat local view",
	"author": "Saidenka,bookyakuno",
	"version": (1, 0, 0),
	"blender": (2, 78),
	"location": "3D View",
	"description": "Repeat local view as long as there are selected objects & Non zoom",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "3D View",
}
import bpy, mathutils
import os, csv
import collections




class LocalViewEx_z(bpy.types.Operator):
	bl_idname = "view3d.local_view_ex_z"
	bl_label = "Global / local view (non-zoom)"
	bl_description = "Repeat local view as long as there are selected objects & Non zoom"
	bl_options = {'REGISTER'}

	def execute(self, context):



		if (context.space_data.local_view):

			ff = bpy.context.selected_objects
			bpy.ops.object.select_all(action='SELECT')
			ww = len (context.selected_objects )

			bpy.ops.object.select_all(action='DESELECT')
			for obj in ff:
				obj.select = True


			aax = len (context.selected_objects )

			if  len (context.selected_objects ) == 0:
				bpy.ops.view3d.local_view_ex_ops()
				self.report(type={'INFO'}, message="0")

			elif  ww == 1:

				self.report(type={'INFO'}, message="1")

				bpy.ops.view3d.local_view_ex_ops()
			elif  len (context.selected_objects ) == ww:


				self.report(type={'INFO'}, message="1")

				bpy.ops.view3d.local_view_ex_ops()

			# elif  len (context.selected_objects ) == aax:
			# 	# if  len (context.selected_objects ) == aax:
			#
			# 	self.report(type={'INFO'}, message="==")
			# 	bpy.ops.view3d.local_view_ex_ops()




			# else:
			elif  len (context.selected_objects ) < ww:


				if context.mode =='EDIT_MESH':
					self.report(type={'INFO'}, message="EDIT")

					bpy.ops.object.editmode_toggle()

					bpy.ops.view3d.local_view_ex_ops()
					bpy.ops.object.editmode_toggle()
				else:
					self.report(type={'INFO'}, message="Repeat")

					aa = bpy.context.selected_objects


					bpy.ops.view3d.local_view_ex_ops()
					bpy.ops.object.select_all(action='DESELECT')
					for obj in aa:
						obj.select = True
					bpy.ops.view3d.local_view_ex_ops()

		else:

			if context.mode =='EDIT_MESH':
				bpy.ops.object.editmode_toggle()

				bpy.ops.view3d.local_view_ex_ops()
				bpy.ops.object.editmode_toggle()

			else:
				bpy.ops.view3d.local_view_ex_ops()





		return {'FINISHED'}


	# =====================================================

	# =====================================================




class LocalViewEx_ops(bpy.types.Operator):
	bl_idname = "view3d.local_view_ex_ops"
	bl_label = "Global / local view (non-zoom)"
	bl_description = "Displays only selected objects and centered point of view doesn\'t (zoom)"
	# bl_options = {'REGISTER'}

	def execute(self, context):


		pre_smooth_view = context.user_preferences.view.smooth_view
		context.user_preferences.view.smooth_view = 0
		pre_view_distance = context.region_data.view_distance
		pre_view_location = context.region_data.view_location.copy()
		pre_view_rotation = context.region_data.view_rotation.copy()
		pre_cursor_location = context.space_data.cursor_location.copy()
		bpy.ops.view3d.localview()
		# if (context.space_data.local_view):
		# 	# self.report(type={'INFO'}, message="Local")
		# else:
			# self.report(type={'INFO'}, message="Global")
		context.space_data.cursor_location = pre_cursor_location
		context.region_data.view_distance = pre_view_distance
		context.region_data.view_location = pre_view_location
		context.region_data.view_rotation = pre_view_rotation
		context.user_preferences.view.smooth_view = pre_smooth_view
		return {'FINISHED'}

	# =====================================================

	# =====================================================




#
# # register the class
# def register():
# 	 bpy.utils.register_module(__name__)
#
# 	 pass
#
# def unregister():
# 	 bpy.utils.unregister_module(__name__)
#
# 	 pass
#
# if __name__ == "__main__":
# 	 register()










		# store keymaps here to access after registration
addon_keymaps = []
def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager



	km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
	kmi = km.keymap_items.new(LocalViewEx_z.bl_idname, 'Q', 'PRESS')
	addon_keymaps.append((km, kmi))








def unregister():
	bpy.utils.unregister_module(__name__)
	# handle the keymap
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()
