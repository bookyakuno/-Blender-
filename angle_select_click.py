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
	"name": "angle select Click",
	"author": "bookyakuno",
	"version": (1,1),
	"location": "Mesh Dispkay Panel. alt + Y or ctrl + ACTIONMOUSE",
	"description": "shift + alt + Y or ctrl + shift + ACTIONMOUSE = select multiple",
	"warning": "This add-on uses hide. Hide information will be lost.",
	"category": "Mesh"}

import bpy
import bmesh



bpy.types.Scene.angle_select_click_threshold = bpy.props.FloatProperty(default= 0.14, min= 0.01, max= 1.00, description="Angle")

class angle_select_click(bpy.types.Operator):
	bl_idname = "object.angle_select_click"
	bl_label = "angle_select_click"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		obj = context.object
		bm = bmesh.from_edit_mesh(obj.data)


		bpy.ops.view3d.select('INVOKE_DEFAULT')
		bpy.ops.mesh.select_similar(type='NORMAL', compare='EQUAL', threshold=bpy.context.scene.angle_select_click_threshold)
		# threshold= bpy.context.scene.angle_select_click_threshold
		bpy.ops.mesh.hide(unselected=True) #選択以外非表示
		bpy.ops.mesh.select_all(action='DESELECT') #選択解除
		bpy.ops.view3d.select('INVOKE_DEFAULT') #マウス下選択
		bpy.ops.mesh.select_linked(delimit={'NORMAL'}) #リンク選択
		bpy.ops.mesh.select_all(action='INVERT')
		# bpy.ops.mesh.reveal()
		bpy.ops.mesh.reveal()


		# selected_faces = [f for f in bm.faces if f.select]
        #
		# for f in selected_faces :
		# 		if selected_faces:
		# 			f.select=True
        #
		# del(selected_faces[:])
		bpy.ops.mesh.select_all(action='INVERT')

		return {'FINISHED'}

class angle_select_click_extend(bpy.types.Operator):
	bl_idname = "object.angle_select_click_extend"
	bl_label = "angle_select_click_extend"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		obj = context.object
		bm = bmesh.from_edit_mesh(obj.data)

		bpy.ops.object.vertex_group_assign_new()
		bpy.ops.mesh.hide() #選択非表示
		bpy.ops.view3d.select('INVOKE_DEFAULT',extend=True)
		bpy.ops.mesh.select_similar(type='NORMAL', compare='EQUAL', threshold=bpy.context.scene.angle_select_click_threshold)

		bpy.ops.mesh.hide(unselected=True) #選択以外非表示
		bpy.ops.mesh.select_all(action='DESELECT') #選択解除
		bpy.ops.view3d.select('INVOKE_DEFAULT',extend=True) #マウス下選択
		bpy.ops.mesh.select_linked(delimit={'NORMAL'}) #リンク選択
		bpy.ops.mesh.select_all(action='INVERT')
		bpy.ops.mesh.reveal()
		bpy.ops.mesh.select_all(action='INVERT')


		selected_faces = [f for f in bm.faces if f.select]

		for f in selected_faces :
				if selected_faces:
					f.select=True

		del(selected_faces[:])

		# bpy.ops.object.vertex_group_deselect()
		bpy.ops.object.vertex_group_select()
		bpy.ops.object.vertex_group_remove()

		return {'FINISHED'}


# ヘッダーに項目追加
def angle_select_click_threshold_menu(self, context):

	layout = self.layout
	scene = context.scene

	# row = layout.row(align=True)
	layout.label(text="angle select click:", icon='LAMP_HEMI')
	layout.prop(context.scene, "angle_select_click_threshold", text="Threshold")



addon_keymaps = []
def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager

	km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
	kmi = km.keymap_items.new(angle_select_click.bl_idname, 'Y', 'PRESS', alt=True)
	addon_keymaps.append((km, kmi))

	kmi = km.keymap_items.new(angle_select_click_extend.bl_idname, 'Y', 'PRESS', alt=True,shift=True)
	addon_keymaps.append((km, kmi))

	kmi = km.keymap_items.new(angle_select_click.bl_idname, 'ACTIONMOUSE', 'PRESS', ctrl=True)
	addon_keymaps.append((km, kmi))

	kmi = km.keymap_items.new(angle_select_click_extend.bl_idname, 'ACTIONMOUSE', 'PRESS', ctrl=True,shift=True)
	addon_keymaps.append((km, kmi))



	# メニューに項目追加
	bpy.types.VIEW3D_PT_view3d_meshdisplay.append(angle_select_click_threshold_menu)


def unregister():
	bpy.utils.unregister_module(__name__)
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()


	bpy.types.VIEW3D_PT_view3d_meshdisplay.remove(angle_select_click_threshold_menu)


if __name__ == '__main__':
	register()
