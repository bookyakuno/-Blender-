
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






import bpy, codecs, os.path

import bpy
import mathutils
import os.path
import os, sys
import subprocess
import fnmatch


# アドオン情報
bl_info = {
	"name" : "info_header_useful",
	"author" : "bookyakuno",
	"version" : (0, 2),
	"blender" : (2, 7),
	"location" : "info header",
	"description" : "info header useful",
	"warning" : "",
	"wiki_url" : "",
	"tracker_url" : "",
	"category" : "UI"
}





class RecoverLatestAutoSave_x(bpy.types.Operator):
	bl_idname = "wm.recover_latest_auto_save_x"
	bl_label = "最新の自動保存の読み込み"
	bl_description = "復元するために自動的に保存したファイルの最新ファイルを開きます"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		tempPath = context.user_preferences.filepaths.temporary_directory
		lastFile = None
		for fileName in fnmatch.filter(os.listdir(tempPath), "*.blend"):
			path = os.path.join(tempPath, fileName)
			if (lastFile):
				mtime = os.stat(path).st_mtime
				if (lastTime < mtime and fileName != "quit.blend"):
					lastFile = path
					lastTime = mtime
			else:
				lastFile = path
				lastTime = os.stat(path).st_mtime
		bpy.ops.wm.recover_auto_save(filepath=lastFile)
		self.report(type={"INFO"}, message="最新の自動保存ファイルを読み込みました")
		return {'FINISHED'}








class INFO_HT_header_recent_files_x(bpy.types.Menu):
	bl_idname = 'yyyt'
	bl_label = "Recent Files"

	def draw(self, context):

		recent_files = os.path.join(bpy.utils.user_resource('CONFIG'), "recent-files.txt")
		file = codecs.open(recent_files, 'r', 'utf-8-sig')

		for index, blend_path in enumerate(file.readlines()):
			if not blend_path: continue
			blend_path = blend_path.rstrip("\r\n")
			base_name = os.path.splitext( os.path.basename(blend_path) )[0]
			row = self.layout.row()
			row.operator_context = 'EXEC_DEFAULT'
			row.operator('wm.open_mainfile', icon='FILE_BLEND', text=base_name).filepath = blend_path

			if index == 0:
				self.layout.separator()
		self.layout.separator()
		row = self.layout.row()
		row.operator('wm.recover_latest_auto_save_x' , icon='PREVIEW_RANGE')

		file.close()



# ヘッダーに項目追加
def func_x_x(self, context):

	layout = self.layout

	window = context.window
	scene = context.scene
	rd = scene.render

	layout.prop(scene, "frame_current", text="")


	toolsettings = context.tool_settings
	screen = context.screen
	userprefs = context.user_preferences

	row = layout.row(align=True)
	row.prop(toolsettings, "use_keyframe_insert_auto", text="", toggle=True)
	if toolsettings.use_keyframe_insert_auto:
		row.prop(toolsettings, "use_keyframe_insert_keyingset", text="", toggle=True)

	if screen.is_animation_playing and not userprefs.edit.use_keyframe_insert_available:
		subsub = row.row(align=True)
		subsub.prop(toolsettings, "use_record_with_nla", toggle=True)

	# 最近使ったファイル
#	self.layout.menu('INFO_MT_file_open_recent', icon='OPEN_RECENT', text="")
#				 layout.menu("INFO_MT_file_open_recent", icon='OPEN_RECENT', text="")


	self.layout.menu('yyyt', icon='OPEN_RECENT', text="")

	### アイテム








	layout = self.layout
	col = layout.column(align=True)
	view = context.space_data
	scene = context.scene
	obj = context.object
	#				obj_type = obj.type

	ob = context.active_object

	row = layout.row()
	row.template_ID(context.scene.objects, "active")
#	 row.label(text="", icon='OBJECT_DATA')
#	 row.prop(ob, "name", text="")

	if ob.type == 'ARMATURE' and ob.mode in {'EDIT', 'POSE'}:
		bone = context.active_bone
		row = layout.row()
		row.label(text="", icon='BONE_DATA')
		row.prop(bone, "name", text="")

	# 連番リネーム
	#				row.prop(context.scene,"rno_str_new_name",text="")
	#				layout.operator("object.rno_setname",text="",icon='GREASEPENCIL')





	obj = context.object

	obj_name = obj.name
	for group in bpy.data.groups:
			group_objects = group.objects
			if obj_name in group.objects and obj in group_objects[:]:
					col = layout.column(align=True)

					col.context_pointer_set("group", group)


					row.menu("GROUP_MT_specials", icon='META_CUBE', text="")
#					row.prop(group, "name", text="")

#					row.operator("object.group_remove", text="", icon='X', emboss=False)







#class GROUP_MT_specials_x(Menu):
#    bl_label = "Group Specials"

#    def draw(self, context):
#        layout = self.layout

#        layout.operator("object.group_unlink", icon='X')
#        layout.operator("object.grouped_select")
#        layout.operator("object.dupli_offset_from_cursor")
#        layout.operator("object.group_remove", icon='X', emboss=False)
#
#
#        obj = context.object

#        obj_name = obj.name
#        for group in bpy.data.groups:
#                group_objects = group.objects
#                if obj_name in group.objects and obj in group_objects[:]:
#                        col = layout.column(align=True)
#                        layout.prop(group, "name", text="")








	# アドオンを有効にしたときの処理
def register():
	# オペレーターなどを登録
	bpy.utils.register_module(__name__)
	# ヘッダーメニューに項目追加
	bpy.types.INFO_HT_header.prepend(func_x_x)
#	 bpy.types.INFO_MT_file_open_recent.append(menu_draw_testx)

# アドオンを無効にしたときの処理
def unregister():
	# オペレーターなどを解除
	bpy.utils.unregister_module(__name__)
	# ヘッダーメニューの項目解除
	bpy.types.INFO_HT_header.remove(func_x_x)
#	 bpy.types.INFO_MT_file_open_recent.remove(menu_draw_testx)


# このスクリプトを単独で実行した時に実行
if __name__ == '__main__':
	register()
