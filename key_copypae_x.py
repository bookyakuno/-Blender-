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
    "name": "key_copypae_x",
    "author": "bookyakuno",
    "version": (1,3),
    "location": "shift + ctrl/cmd + X/C/V ,key_del = BACK_SPACE(Other Anime Editor Window)",
    "description": "current key frame CUT, COPY, PASTE, DELETE in Timeline",
    "warning": "",
    "category": "timeline"}

# import the basic library
import bpy




class key_cut_x(bpy.types.Operator):
    bl_idname = "object.key_cut_x"
    bl_label = "key_cut_x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Message
        if (context.active_object):
            self.report(type={"INFO"}, message="key_cut_x")


        bpy.ops.object.view_menu(variable="DOPESHEET_EDITOR")	    # ドープシートへ移動
        # 選択を確実に解除
        bpy.ops.action.select_leftright(mode='RIGHT', extend=False)	 # 右側を選択
        bpy.ops.action.select_all_toggle(invert=False)				# 選択解除

        bpy.ops.action.select_column(mode='CFRA')				    # 現在のフレームのキーをすべて選択
        bpy.ops.action.copy()									    # キーフレームをコピー
        bpy.ops.action.delete()                                     # キーフレームをカット
        bpy.ops.object.view_menu(variable="TIMELINE")				# タイムラインへ戻る

        return {'FINISHED'}


class key_copy_x(bpy.types.Operator):
    bl_idname = "object.key_copy_x"
    bl_label = "key_copy_x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Message
        if (context.active_object):
            self.report(type={"INFO"}, message="key_copy_x")


        bpy.ops.object.view_menu(variable="DOPESHEET_EDITOR")	#ドープシートへ移動
        # 選択を確実に解除
        bpy.ops.action.select_leftright(mode='RIGHT', extend=False)	 # 右側を選択
        bpy.ops.action.select_all_toggle(invert=False)				# 選択解除

        bpy.ops.action.select_column(mode='CFRA')				# 現在のフレームのキーをすべて選択
        bpy.ops.action.copy()									# キーフレームをコピー
        bpy.ops.object.view_menu(variable="TIMELINE")				# タイムラインへ戻る

        return {'FINISHED'}





class key_paste_x(bpy.types.Operator):
    bl_idname = "object.key_paste_x"
    bl_label = "key_paste_x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if (context.active_object):
            self.report(type={"INFO"}, message="key_paste_x")			# Message


        bpy.ops.object.view_menu(variable="DOPESHEET_EDITOR")
        bpy.ops.action.paste()
        bpy.ops.object.view_menu(variable="TIMELINE")


        return {'FINISHED'}



class key_move_current_x(bpy.types.Operator):
    bl_idname = "object.key_move_current_x"
    bl_label = "key_move_current_x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # if (context.active_object):
        self.report(type={"INFO"}, message="key_move_current_x")			# Message

        bpy.ops.action.copy()
        bpy.ops.action.delete()
        bpy.ops.action.paste()


        return {'FINISHED'}










class key_del_x(bpy.types.Operator):
	bl_idname = "object.key_del_x"
	bl_label = "key_del_x"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if (context.active_object):
		    self.report(type={"INFO"}, message="key_del_x")			# Message
		bpy.ops.anim.keyframe_delete_v3d() #これが実際に削除するやつ。普通にAlt + Iから実行する方は、『警告 + この文』を実行しているので、この文だけを実行させる
		return {'FINISHED'}


class key_del_graph_x(bpy.types.Operator):
	bl_idname = "graph.key_del_graph_x"
	bl_label = "silent_graph_Key_Del"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if (context.active_object):
		    self.report(type={"INFO"}, message="key_del_graph_x")			# Message
		bpy.ops.graph.delete()
		 #これが実際に削除するやつ。普通にAlt + Iから実行する方は、『警告 + この文』を実行しているので、この文だけを実行させる
		return {'FINISHED'}












        # store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)
    # handle the keymap
#addon_keymaps = [] #put on out of register()
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = 'Timeline', space_type = 'TIMELINE')

    # key_cut_x
    kmi = km.keymap_items.new(key_cut_x.bl_idname, 'X', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(key_cut_x.bl_idname, 'X', 'PRESS', shift=True, oskey=True)
    addon_keymaps.append((km, kmi))

    # key_copy_x
    kmi = km.keymap_items.new(key_copy_x.bl_idname, 'C', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(key_copy_x.bl_idname, 'C', 'PRESS', shift=True, oskey=True)
    addon_keymaps.append((km, kmi))

    # key_paste_x
    kmi = km.keymap_items.new(key_paste_x.bl_idname, 'V', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(key_paste_x.bl_idname, 'V', 'PRESS', shift=True, oskey=True)
    addon_keymaps.append((km, kmi))

    # key_move_current_x
    kmi = km.keymap_items.new(key_move_current_x.bl_idname, 'X', 'PRESS',  oskey=True)
    addon_keymaps.append((km, kmi))

    # key_del_x
    kmi = km.keymap_items.new(key_del_x.bl_idname, 'BACK_SPACE', 'PRESS')
    addon_keymaps.append((km, kmi))

    km = wm.keyconfigs.addon.keymaps.new(name = 'Graph Editor Generic', space_type = 'GRAPH_EDITOR')
    kmi = km.keymap_items.new(key_del_graph_x.bl_idname, 'BACK_SPACE', 'PRESS')
    addon_keymaps.append((km, kmi))
    # km = wm.keyconfigs.addon.keymaps.new(name = 'Dopesheet', space_type = 'DOPESHEET_EDITOR')
    # kmi = km.keymap_items.new(key_del_x.bl_idname, 'BACK_SPACE', 'PRESS')
    # addon_keymaps.append((km, kmi))
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(key_del_x.bl_idname, 'BACK_SPACE', 'PRESS',  alt=True)
    addon_keymaps.append((km, kmi))
    km = wm.keyconfigs.addon.keymaps.new(name='Pose Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(key_del_x.bl_idname, 'BACK_SPACE', 'PRESS',  alt=True)
    addon_keymaps.append((km, kmi))



def unregister():
    bpy.utils.unregister_module(__name__)
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()








#
#
#
# # register the class
# def register():
#     bpy.utils.register_module(__name__)
#
#     pass
#
# def unregister():
#     bpy.utils.unregister_module(__name__)
#
#     pass
#
# if __name__ == "__main__":
#     register()
