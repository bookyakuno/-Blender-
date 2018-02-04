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

import sys

from . import w_pie
from . import add_pie
from . import uv_pie
# from . import prefs
from bpy.types import Operator, AddonPreferences

import bpy, os
from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty
import bmesh
from mathutils import *
import math

import sys


bl_info = {
    "name": "w_pie",
    "author": "Bookyakuno & Cédric Lepiller & Jimmy & DavideDozza & Lapineige & Leafar & 0rAngE",
    "version": (0, 2, 6),
    "blender": (2, 79, 0),
    "description": "Extend Right click with pie menu.",
    "category": "3D View",}


def _call_globals(attr_name):
    for m in globals().values():
        if hasattr(m, attr_name):
            getattr(m, attr_name)()


def _flush_modules(pkg_name):
    pkg_name = pkg_name.lower()
    for k in tuple(sys.modules.keys()):
        if k.lower().startswith(pkg_name):
            del sys.modules[k]





# 翻訳辞書
translation_dict = {
    "en_US": {
    },
    "ja_JP": {


        ("*", "This add-on is a compact modified 'wazou pie menu'and added functions."):
    		"このアドオンはWazou Pie Menuをコンパクトにし、さらに機能を追加したものです。",
        ("*", "Extend Right click with pie menu."):
            "右クリックをパイメニューで拡張するものです。",
        ("*", "Only necessary functions - Accessible - Easy to use concept as a concept,"):
            "必要な機能だけ・アクセスしやすく・使いやすいをコンセプトに、",
        ("*", "Key setting with centering on Right click."):
            "パイメニューを右クリックを中心にキー設定をしたものです。",
        ("*", "Other, addition of objects, selection with UV editor, fine addition function, etc."):
            "その他オブジェクト追加やUVエディターでの選択、機能追加などもあります。",
        ("*", "Change the the system setting select button to the LEFT!!"):
            "左選択を前提に作っているので、ユーザー設定のセレクトボタンを「左」に変えてください！！",
		("*", "(SELECTMOUSE is write it as a LEFT)"):
		"(選択マウスは左という前提で記入します)",
		("*", "-shortcut-"):
		"ーショートカットー",
    }
}







class w_pie_Prefs(bpy.types.AddonPreferences):

    bl_idname = __name__

    bpy.types.Scene.Enable_Tab_01 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_02 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_03 = bpy.props.BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, "Enable_Tab_01", text="Info", icon="QUESTION")
        if context.scene.Enable_Tab_01:
            row = layout.row()

            # layout.label(text="It will not be saved if you change it with keymap list of this addon.")
            layout.label(text="Extend Right click with pie menu.")
            layout.label(text="Only necessary functions - Accessible - Easy to use concept as a concept,")
            layout.label(text="Key setting with centering on Right click.")
            layout.label(text="Other, addition of objects, selection with UV editor, fine addition function, etc.")
            layout.label(text="")
            layout.label(text="Change the the system setting select button to the LEFT!!", icon="ERROR")
            input_prefs = context.user_preferences.inputs
            row = layout.row()
            col = row.column()
            sub = col.column()
            row.label(text="User Preferences")
            row.label(text="Select With:")
            row.row().prop(input_prefs, "select_mouse", expand=True)


            layout.label(text="")
            layout.label(text="-shortcut-")
            layout.label(text="(SELECTMOUSE is write it as a LEFT)")

            # このアドオンは、"wazou pie menu" をコンパクトに改造し、さらに機能を追加したものです。
            # >右クリックからの呼び出し
            # >"新規オブジェクト追加 pie"
            # >"UV pie"を追加





            scene = context.scene
            cscene = scene.cycles
            rd = context.scene.render



            col = layout.column(align=True)


            # col = split.column()
            row = col.row(align=True)
            row.label(text="– Object/Edit mode & Vertex/Edge/face >", icon='FACESEL')
            row.label(text="Right mouse")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– add object >", icon='MONKEY')
            row.label(text="Right mouse + shift")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Shading >", icon='MATERIAL')
            row.label(text="Right mouse + shift + alt")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Pivot point   >", icon='ROTATECOLLECTION')
            row.label(text="Right mouse + alt")


            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Views >", icon='NODETREE')
            row.label(text="Ctrl + Q")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Views misc>", icon='NODETREE')
            row.label(text="Ctrl + shift + Q")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Cursor/Origin >", icon='CURSOR')
            row.label(text="Shift + S")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Selections >", icon='BORDER_RECT')
            row.label(text="Shift + G")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– UV >", icon='OUTLINER_OB_LATTICE')
            row.label(text="ctrl D")




        layout.prop(context.scene, "Enable_Tab_03", text="URL's", icon="URL")
        if context.scene.Enable_Tab_03:
            row = layout.row()


            layout.label(text="This add-on is a compact modified 'wazou pie menu'and added functions.")
            layout.label(text="Combined add-ons")
            layout.label(text="> Wazou Pie Menus")
            layout.label(text="> Jimmy_pie_uv")
            layout.label(text="> Add Object Pie Menu")
            row = layout.row()
            row.operator("wm.url_open", text="Pitiwazou.com").url = "http://www.pitiwazou.com/"
            row.operator("wm.url_open", text="Wazou's Ghitub").url = "https://github.com/pitiwazou/Scripts-Blender"
            row.operator("wm.url_open", text="BlenderLounge Forum ").url = "http://blenderlounge.fr/forum/"
            row = layout.row()
            row.operator("wm.url_open", text="bookyakuno github").url = "https://github.com/bookyakuno/-Blender-/blob/master/w_pie.zip"



addon_keymaps = []

def register():
    bpy.utils.register_class(w_pie_Prefs)
    bpy.utils.register_module(__name__)
    bpy.app.translations.register(__name__, translation_dict)   # 辞書の登録


# Keympa Config

    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        #Select Mode
        km = wm.keyconfigs.addon.keymaps.new('Object Non-modal', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('wm.call_menu_pie', 'ACTIONMOUSE', 'PRESS')
        kmi.properties.name = "pie.objecteditmode"

        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'ACTIONMOUSE', 'PRESS')
        kmi.properties.name = "pie.objecteditmode"

        #Views
        km = wm.keyconfigs.addon.keymaps.new(name='Window')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', ctrl=True)
        kmi.properties.name = "pie.areaviews"
        #Views
        km = wm.keyconfigs.addon.keymaps.new(name='Window')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', ctrl=True, shift=True)
        kmi.properties.name = "pie.view_misc"

        #Origin/Pivot
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'ACTIONMOUSE', 'PRESS', alt=True)
        kmi.properties.name = "pie.pivotpoint"

        # cursor
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', shift=True)
        kmi.properties.name = "pie.originpivot"
        km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', shift=True)
        kmi.properties.name = "pie.originpivot"

        #Shading
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'ACTIONMOUSE', 'PRESS', alt=True, shift=True)
        kmi.properties.name = "pie.shadingview"

        # #Object shading
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'Z', 'PRESS', shift=True)
        # kmi.properties.name = "pie.objectshading"

        #Selection Object Mode
        km = wm.keyconfigs.addon.keymaps.new(name = 'Object Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'G', 'PRESS', shift=True)
        kmi.properties.name = "pie.selectionsom"

        #Selection Edit Mode
        km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'G', 'PRESS', shift=True)
        kmi.properties.name = "pie.selectionsem"

        #uv_pie
        km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS', ctrl=True)
        kmi.properties.name = "pie.uv_pie"

        #uv_pie
        km = wm.keyconfigs.addon.keymaps.new(name = 'Image', space_type='IMAGE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS', ctrl=True)
        kmi.properties.name = "pie.uv_pie"



############################################
############################################
# add pie menu

        # object mode
        km = wm.keyconfigs.addon.keymaps.new(name="Object Mode")
        kmi = km.keymap_items.new("wm.call_menu_pie", "ACTIONMOUSE", "PRESS", shift=True)
        kmi.properties.name="add.menu"
        addon_keymaps.append(km)
        print(kmi.properties.name)

        #mesh edit mode
        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        # km = wm.keyconfigs.addon.keymaps.new(name="Mesh")
        kmi = km.keymap_items.new("wm.call_menu_pie", "ACTIONMOUSE", "PRESS", shift=True)
        kmi.properties.name="add.mesh"
        addon_keymaps.append(km)
        print(kmi.properties.name)

        #curve edit mode
        km = wm.keyconfigs.addon.keymaps.new(name="Curve")
        kmi = km.keymap_items.new("wm.call_menu_pie", "ACTIONMOUSE", "PRESS", shift=True)
        kmi.properties.name="add.curve"
        addon_keymaps.append(km)
        print(kmi.properties.name)

        #mataball edit mode
        km = wm.keyconfigs.addon.keymaps.new(name="Metaball")
        kmi = km.keymap_items.new("wm.call_menu_pie", "ACTIONMOUSE", "PRESS", shift=True)
        kmi.properties.name="add.metaball"
        addon_keymaps.append(km)

        print(kmi.properties.name)



        #Node Editor
        km = wm.keyconfigs.addon.keymaps.new(name = "Node Editor", space_type = "NODE_EDITOR")
        kmi = km.keymap_items.new("wm.call_menu_pie", "ACTIONMOUSE", "PRESS", shift=True)
        kmi.properties.name="pie.add_node"
        addon_keymaps.append(km)

        ############################################
        ############################################
        # UV pie select mode
        km = wm.keyconfigs.addon.keymaps.new(name='Image',
                                             space_type='IMAGE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'ACTIONMOUSE', 'PRESS')
        kmi.properties.name = "pie.uv_select_mode"

        addon_keymaps.append(km)









# Register / Unregister Classes
def unregister():
    bpy.utils.unregister_class(w_pie_Prefs)
    bpy.utils.unregister_module(__name__)
    bpy.app.translations.unregister(__name__)   # 辞書の削除

if __name__ == "__main__":
    register()
