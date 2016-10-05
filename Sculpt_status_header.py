# ##### BEGIN GPL LICENSE BLOCK #####
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 2
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

# アドオン情報
bl_info = {
	"name" : "Sculpt status header",
	"author" : "bookyakuno",
	"version" : (0, 2),
	"blender" : (2, 78),
	"location" : "Sculpt Mode > 3DView > header > Left, duplicate/separate mask > shfit + alt + D/F",
	"description" : "Sculpt smart status",
	"warning" : "",
	"wiki_url" : "",
	"tracker_url" : "",
	"category" : "UI"
}


def prop_unified_size_x(self, context):
	ups = context.tool_settings.unified_paint_settings
	ptr = ups if ups.use_unified_size else brush
	parent.prop(ptr, prop_name, icon=icon, text=text, slider=slider)



# ヘッダーに項目追加
def sculpt_header(self, context):

	layout = self.layout


	if context.image_paint_object:

		col = layout.column(align=True)
		row = col.row(align=True)
		# シンメトリー

		toolsettings = context.tool_settings
		ipaint = toolsettings.image_paint
		row.prop(ipaint, "use_symmetry_x", text="X", toggle=True)
		row.prop(ipaint, "use_symmetry_y", text="Y", toggle=True)
		row.prop(ipaint, "use_symmetry_z", text="Z", toggle=True)



		settings = self.paint_settings(context)
		brush = settings.brush

		col = layout.column()

		col.label(text="Stroke Method:")

		col.prop(brush, "stroke_method", text="")








	obj = context.active_object
	mode_string = context.mode
	edit_object = context.edit_object
	gp_edit = context.gpencil_data and context.gpencil_data.use_stroke_edit_mode
	mode = obj.mode
	if (mode == 'EDIT' and obj.type == 'MESH' or mode == 'EDIT' and 'ARMATURE'):

		arm = context.active_object.data
		self.layout.prop(arm, "use_mirror_x",text="",icon="MOD_MIRROR")


#   obj = context.active_object
#   if obj:
#   		obj_type = obj.type

#   		if obj_type in {'ARMATURE'}:

#   			arm = context.active_object.data
#   			self.layout.prop(arm, "use_mirror_x",text="",icon="MOD_MIRROR")


#   if mode_string == 'EDIT_ARMATURE':
#
#   	arm = context.active_object.data
#   	self.layout.prop(arm, "use_mirror_x")

#   if ob.type == 'ARMATURE' and ob.mode in {'EDIT', 'POSE'}:

#   	arm = context.active_object.data
#   	self.layout.prop(arm, "use_mirror_x")


	if context.sculpt_object:

		col = layout.column(align=True)
		row = col.row(align=True)
		# シンメトリー
		sculpt = context.tool_settings.sculpt
		row.scale_x = 0.5
		row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
		row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
		row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)




#   	 toolsettings = context.tool_settings
#   	 settings = self.paint_settings(context)
#   	 brush = settings.brush
#
#
#   	 col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)



		# Dynatopo
# row.separator()
# if context.sculpt_object.use_dynamic_topology_sculpting:
#	 row.operator("sculpt.dynamic_topology_toggle", icon='CANCEL', text="")
# else:
#	 row.operator("sculpt.dynamic_topology_toggle", icon='MOD_REMESH', text="")
# row.prop(sculpt, "detail_size", text="")



		#booleans_sculpt_v_0_0_2.py

		WM = context.window_manager
		toolsettings = context.tool_settings
		sculpt = toolsettings.sculpt

		if len(context.selected_objects) >= 1 :
				#Detail Size
				row.separator()
				row = layout.row(align=True)
				row.operator("object.update_dyntopo", text=" ", icon='FILE_TICK')
				row.scale_x = 0.5
				row.prop(WM, "detail_size", text="")
#   			row.scale_x = 1.2
				row.separator()
				if context.sculpt_object.use_dynamic_topology_sculpting:
					row.operator("sculpt.dynamic_topology_toggle", icon='CANCEL', text="")
				else:
					row.operator("sculpt.dynamic_topology_toggle", icon='MOD_REMESH', text="")

				row.separator()

				if not bpy.context.object.mode == 'SCULPT':
						layout.prop(WM, "subdivide_mesh", text="Subdivide")
						if WM.subdivide_mesh:
								layout.prop(WM, "use_sharps", text="Sharp Edges")
				layout.prop(WM, "smooth_mesh", text="", icon='MOD_SMOOTH')
				layout.prop(WM, "update_detail_flood_fill", text="", icon='MOD_DECIM')


#	def prop_unified_strength(parent, context, brush, prop_name, icon='NONE', text="", slider=False):
#		ups = context.tool_settings.unified_paint_settings
#		ptr = ups if ups.use_unified_strength else brush
#		parent.prop(ptr, prop_name, icon=icon, text=text, slider=slider)






################################################################

#   	row.prop(brush, "stroke_method", text="")

		row.prop(sculpt, "detail_size", text="")


def texture_import(self, context):

	layout = self.layout


	layout.separator()
	layout.operator('texture.load_brushes')
	layout.operator('texture.load_single_brush')










# class sculptmode_off_persp(bpy.types.Operator):
# 	bl_idname = "object.sculptmode_off_persp"
# 	bl_label = "sculptmode_off_persp"
#
#
# 	def execute(self, context):
# 		# v = bpy.context.user_preferences.view
# 		bpy.ops.sculpt.sculptmode_toggle()
# 		bpy.context.user_preferences.view.use_auto_perspective = False
#
# 		if bpy.context.object.mode == 'SCULPT':
#
# 			bpy.ops.sculpt.sculptmode_toggle()
# 			bpy.context.user_preferences.view.use_auto_perspective = True
#
# 		return {'FINISHED'}



class duplicate_mask(bpy.types.Operator):
	bl_idname = "object.duplicate_mask"
	bl_label = "duplicate_mask"


	def execute(self, context):
		bpy.ops.paint.hide_show(action='HIDE', area='MASKED') # マスク部分を非表示
		bpy.ops.sculpt.sculptmode_toggle() # オブジェクトモードに戻す
		bpy.ops.object.select_all(action='DESELECT') #全選択解除で最後に選択するものを複製したものだけにする
		bpy.ops.object.editmode_toggle() # 編集モード
		bpy.ops.mesh.select_all(action='DESELECT') #全選択解除
		bpy.ops.mesh.reveal() # 隠しているものを表示
		bpy.ops.mesh.duplicate_move() # 選択部分を複製
		bpy.ops.mesh.edge_face_add() # 閉じたオブジェクトにする(F2)
		bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY') # 閉じた面を三角形化
		bpy.ops.mesh.separate(type='SELECTED') # 選択部分を分離
		bpy.ops.object.editmode_toggle() # オブジェクトモード
		bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') #重心に原点を配置して、回転しやすいように

		return {'FINISHED'}



class separate_mask(bpy.types.Operator):
	bl_idname = "object.separate_mask"
	bl_label = "separate_mask"


	def execute(self, context):
		bpy.ops.paint.hide_show(action='HIDE', area='MASKED') # マスク部分を非表示
		bpy.ops.sculpt.sculptmode_toggle() # オブジェクトモードに戻す
		bpy.ops.object.select_all(action='DESELECT') #全選択解除で最後に選択するものを複製したものだけにする
		bpy.ops.object.editmode_toggle() # 編集モード
		bpy.ops.mesh.select_all(action='DESELECT') #全選択解除
		bpy.ops.mesh.reveal() # 隠しているものを表示
		# bpy.ops.mesh.duplicate_move() # 選択部分を複製
		bpy.ops.mesh.split()
		bpy.ops.mesh.edge_face_add() # 閉じたオブジェクトにする(F2)
		bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY') # 閉じた面を三角形化
		bpy.ops.mesh.separate(type='SELECTED') # 選択部分を分離
		bpy.ops.object.editmode_toggle() # オブジェクトモード
		bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') #重心に原点を配置して、回転しやすいように

		return {'FINISHED'}




addon_keymaps = []
def register():
	bpy.utils.register_module(__name__)

	bpy.types.VIEW3D_HT_header.prepend(sculpt_header)
	bpy.types.VIEW3D_PT_tools_brush_texture.append(texture_import)

	# bpy.utils.register_class(separate_mask)



	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps.new(name='Sculpt', space_type='EMPTY')
	kmi = km.keymap_items.new(duplicate_mask.bl_idname, 'D', 'PRESS',  alt=True, shift=True)
	addon_keymaps.append((km, kmi))
	kmi = km.keymap_items.new(separate_mask.bl_idname, 'F', 'PRESS',  alt=True, shift=True)
	addon_keymaps.append((km, kmi))









def unregister():
	bpy.types.VIEW3D_HT_header.remove(sculpt_header)
	bpy.types.VIEW3D_PT_tools_brush_texture.remove(texture_import)

	# bpy.utils.unregister_class(separate_mask)



# このスクリプトを単独で実行した時に実行
if __name__ == '__main__':
	register()
