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
	"name": "group_layer",
	"author": "bookyakuno",
	"version": (1,0),
	"location": "Outliner header",
	"description": "like Layer Outliner Group.",
	"warning": "",
	"category": "outliner"}


# import the basic library
import bpy

class root_group_z(bpy.types.Operator):
	bl_idname = "object.root_group_z"
	bl_label = "root_group_z"
	bl_description = "Create/add _root group."

	def execute(self, context):
#		bpy.context.scene.objects.select = True #all select


		for ob in bpy.context.scene.objects:
			# if ob.type == 'MESH':
				ob.select = True

		for group in bpy.data.groups:
			for object in group.objects:
		#        print(object.name)
		#        o = bpy.data.objects
		#        o.select = True
				ee = object
				ee.select = False

		#bpy.ops.group.create(name="_root")
		bpy.ops.object.group_link(group='_root')
		bpy.ops.group.objects_add_active(group='_root')

		return {'FINISHED'}


class new_group_z(bpy.types.Operator):
	bl_idname = "object.new_group_z"
	bl_label = "new_group_z"
	bl_description = "all remeve and Create new group."

	def execute(self, context):
		bpy.ops.group.objects_remove_all()
		# bpy.ops.group.objects_add_active(group='z_')
		bpy.ops.group.create(name="z_")

		return {'FINISHED'}


class add_group_z(bpy.types.Operator):
	bl_idname = "object.add_group_z"
	bl_label = "add_group_z"

	def execute(self, context):
		bpy.ops.group.objects_remove_all()
		bpy.ops.object.group_link()

		return {'FINISHED'}







def group_layer_menu(self, context):

	space = context.space_data
	layout = self.layout
	# layout.menu("OUTLINER_MT_view", text="",icon="COLLAPSEMENU")
	# layout.menu("OUTLINER_MT_search", text="",icon="FILTER")


	if bpy.context.space_data.display_mode == 'GROUPS':
		row = layout.row()
		row = layout.row(align=True)

		row.operator("group.objects_remove", text="", icon='X')
		row.operator("group.objects_remove_all", text="", icon='CANCEL')
		row.operator("object.group_link", text="", icon='ZOOMIN')
		row.operator("object.new_group_z", text="", icon='NEW')

	if space.display_mode == 'DATABLOCKS':
		layout.menu("OUTLINER_MT_edit_datablocks")










def register():
	bpy.utils.register_class(root_group_z)
	bpy.utils.register_class(new_group_z)
	bpy.utils.register_class(add_group_z)

	bpy.utils.register_module(__name__)
	bpy.types.OUTLINER_HT_header.prepend(group_layer_menu)


def unregister():
	bpy.utils.unregister_class(root_group_z)
	bpy.utils.unregister_class(new_group_z)
	bpy.utils.unregister_class(add_group_z)


	bpy.utils.unregister_module(__name__)

	bpy.types.INFO_HT_header.remove(group_layer_menu)


if __name__ == '__main__':
	register()
