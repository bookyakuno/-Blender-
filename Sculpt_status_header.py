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

import bpy

# アドオン情報
bl_info = {
	"name" : "Sculpt status header",
	"author" : "bookyakuno",
	"version" : (0, 2),
	"blender" : (2, 77),
	"location" : "Sculpt Mode > 3DView > header > Left",
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


#	obj = context.active_object
#	if obj:
#			obj_type = obj.type

#			if obj_type in {'ARMATURE'}:

#				arm = context.active_object.data
#				self.layout.prop(arm, "use_mirror_x",text="",icon="MOD_MIRROR")


#	if mode_string == 'EDIT_ARMATURE':
#    
#		arm = context.active_object.data
#		self.layout.prop(arm, "use_mirror_x")

#	if ob.type == 'ARMATURE' and ob.mode in {'EDIT', 'POSE'}:

#		arm = context.active_object.data
#		self.layout.prop(arm, "use_mirror_x")


	if context.sculpt_object:

		col = layout.column(align=True)
		row = col.row(align=True)
		# シンメトリー
		sculpt = context.tool_settings.sculpt
		row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
		row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
		row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)




# 		toolsettings = context.tool_settings
# 		settings = self.paint_settings(context)
# 		brush = settings.brush
#
#
# 		col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)



		# Dynatopo
		row.separator()
		if context.sculpt_object.use_dynamic_topology_sculpting:
			row.operator("sculpt.dynamic_topology_toggle", icon='CANCEL', text="")
		else:
			row.operator("sculpt.dynamic_topology_toggle", icon='MOD_REMESH', text="")



################################################################

#		row.prop(brush, "stroke_method", text="")

		row.prop(sculpt, "detail_size", text="")


def texture_import(self, context):

	layout = self.layout


	layout.separator()
	layout.operator('texture.load_brushes')
	layout.operator('texture.load_single_brush')







	# アドオンを有効にしたときの処理
def register():
	# オペレーターなどを登録
# 	bpy.utils.register_module(__name__)
	# ヘッダーメニューに項目追加
	bpy.types.VIEW3D_HT_header.prepend(sculpt_header)
	bpy.types.VIEW3D_PT_tools_brush_texture.append(texture_import)

# アドオンを無効にしたときの処理
def unregister():
	# オペレーターなどを解除
# 	bpy.utils.unregister_module(__name__)
	# ヘッダーメニューの項目解除
	bpy.types.VIEW3D_HT_header.remove(sculpt_header)
	bpy.types.VIEW3D_PT_tools_brush_texture.remove(texture_import)



# このスクリプトを単独で実行した時に実行
if __name__ == '__main__':
	register()
