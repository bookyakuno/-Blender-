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
	"version" : (0, 1),
	"blender" : (2, 77),
	"location" : "Sculpt Mode > 3DView > header > Left",
	"description" : "Sculpt smart status",
	"warning" : "",
	"wiki_url" : "",
	"tracker_url" : "",
	"category" : "UI"
}



# ヘッダーに項目追加
def sculpt_header(self, context):

	layout = self.layout
	
	if context.sculpt_object:
	
		sculpt = context.tool_settings.sculpt
		
		col = layout.column(align=True)
		row = col.row(align=True)
		# シンメトリー
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





	# アドオンを有効にしたときの処理
def register():
	# オペレーターなどを登録
# 	bpy.utils.register_module(__name__)
	# ヘッダーメニューに項目追加
	bpy.types.VIEW3D_HT_header.prepend(sculpt_header)

# アドオンを無効にしたときの処理
def unregister():
	# オペレーターなどを解除
# 	bpy.utils.unregister_module(__name__)
	# ヘッダーメニューの項目解除
	bpy.types.VIEW3D_HT_header.remove(sculpt_header)



# このスクリプトを単独で実行した時に実行
if __name__ == '__main__':
	register()
