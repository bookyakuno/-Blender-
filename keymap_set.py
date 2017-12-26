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
	"name": "Keymap Set",
	"author": "bookyakuno",
	"version": (0, 4),
	"blender": (2, 79, 0),
	"description": "Rational Keymap Set",
	"location": "This addon Setting",
	"warning": "",
	"category": "UI"}

# 	このアドオンのkeymapリストによって変更しても保存されません。 "入力"タブの所で検索して変更してください。
# チェックボックスによってkeymap を有功/無効にできます。それには再起動が必要です。
#
import bpy, os
from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty
import bmesh
from mathutils import *
import math
import rna_keymap_ui



import bpy
from bpy.app.translations import pgettext_iface as iface_
from bpy.app.translations import contexts as i18n_contexts


class DeleteBySelectMode_x(bpy.types.Operator):
	bl_idname = "mesh.delete_by_select_mode_x"
	bl_label = "delete by mode"
	bl_description = "delete by select mode"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		mode = context.tool_settings.mesh_select_mode[:]
		if (mode[0]):
			bpy.ops.mesh.delete(type="VERT")
		elif (mode[1]):
			bpy.ops.mesh.delete(type="EDGE")
		elif (mode[2]):
			bpy.ops.mesh.delete(type="FACE")
		return {'FINISHED'}


class KeymapSetMenuPrefs(bpy.types.AddonPreferences):
	bl_idname = __name__





	use_scene_refresh_z = bpy.props.BoolProperty(
		name="Refresh Scene",
		description="Specials Menu [W], or hit F5",
		default=False,
	)
	boolean = BoolProperty(
			name="Example Boolean",
			default=False,
			)
	select_border = BoolProperty(
			name="select_border",
			default=True,
			)

	select_link = BoolProperty(
			name="select link",
			default=True,
			)

	mode_set = BoolProperty(
			name="Mode Set",
			default=True,
			)

	view_numpad = BoolProperty(
			name="View Numpad",
			default=True,
			)

	etc = BoolProperty(
			name="Etc",
			default=True,
			)
######################################################
######################################################

	bpy.types.Scene.select_border_tab = bpy.props.BoolProperty(default=False)

	bpy.types.Scene.select_linked_tab = bpy.props.BoolProperty(default=False)

	bpy.types.Scene.view_numpad_tab = bpy.props.BoolProperty(default=False)

	bpy.types.Scene.mode_set_tab = bpy.props.BoolProperty(default=False)


	bpy.types.Scene.select_border_tab_02 = bpy.props.BoolProperty(default=False)




	def draw(self, context):
		layout = self.layout
		user_preferences = context.user_preferences
		addon_prefs = user_preferences.addons[__name__].preferences

		#######################################################
		#######################################################


		# layout.prop(self, "boolean")
		# # layout.prop(self, "select_border")
        #
		# if addon_prefs.boolean == True:
		# 	layout.label(
		# 	text="Here you can enable or disable specific tools, "
		# 	"in case they interfere with others or are just plain annoying")



		layout.label(
		text="It will not be saved if you change it with keymap list of this addon."
		)
		layout.label(
		text="Please search and change at the 'input' tab. "
		)
		layout.label(
		text=		"")
		layout.label(
		text=		"A checkbox enables you to enable / disable keymap.")
		layout.label(
		text=		"It requires a reboot.", icon='FILE_REFRESH')



#######################################################
#######################################################
#  Select Border
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(self, "select_border")
		row.prop(context.scene, "select_border_tab", text="Select Border >> Mouse Drag", icon="URL")


		if context.scene.select_border_tab:
			col = layout.column()
			kc = bpy.context.window_manager.keyconfigs.addon
			for km, kmi in select_border_keymap:
				km = km.active()
				col.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)


#######################################################
#######################################################
#  Select Linked
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(self, "select_link")
		row.prop(context.scene, "select_linked_tab", text="Select Linked >> Double Click", icon="URL")

		if context.scene.select_linked_tab:
			col = layout.column()
			kc = bpy.context.window_manager.keyconfigs.addon
			for km, kmi in select_linked_keymap:
				km = km.active()
				col.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)



#######################################################
#######################################################
#  view numpad
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(self, "view_numpad")
		row.prop(context.scene, "view_numpad_tab", text="view numpad  >> 1,2,3,4,5", icon="URL")



		if context.scene.view_numpad_tab:
			col = layout.column()
			kc = bpy.context.window_manager.keyconfigs.addon
			for km, kmi in view_numpad_keymap:
				km = km.active()
				col.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)


#######################################################
#######################################################
#  Mode Set
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(self, "mode_set")
		row.prop(context.scene, "mode_set_tab", text="Mode Set >> Tab", icon="URL")


		if context.scene.mode_set_tab:
			col = layout.column()
			kc = bpy.context.window_manager.keyconfigs.addon
			for km, kmi in mode_set_keymap:
				km = km.active()
				col.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)



#######################################################
#######################################################
#  etc
		col = layout.column(align=True)
		row = col.row(align=True)
		row.prop(self, "etc")
		row.prop(context.scene, "select_border_tab_02", text="etc...", icon="URL")


		if context.scene.select_border_tab_02:
			col = layout.column()
			kc = bpy.context.window_manager.keyconfigs.addon
			for km, kmi in ccc:
				km = km.active()
				col.context_pointer_set("keymap", km)
				rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)




select_border_keymap = []

select_linked_keymap = []

view_numpad_keymap = []

mode_set_keymap = []

ccc = []
################################################################
# # # # # # # # プロパティの指定に必要なもの
def kmi_props_setattr(kmi_props, attr, value):
	try:
		setattr(kmi_props, attr, value)
	except AttributeError:
		print("Warning: property '%s' not found in keymap item '%s'" %
			  (attr, kmi_props.__class__.__name__))
	except Exception as e:
		print("Warning: %r" % e)

# # # # # # # #
################################################################
#------------------- REGISTER ------------------------------

def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager
	if wm.keyconfigs.addon:
#
#  ################################################################
#
		user_preferences = bpy.context.user_preferences
		addon_prefs = user_preferences.addons[__name__].preferences

		######################################################
		######################################################
		#boader select
		# 矩形選択
		if addon_prefs.select_border == True:

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY')
			kmi_props_setattr(kmi.properties, 'extend', False)
			kmi.active = True
			select_border_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
			kmi.active = True
			select_border_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.manipulator', 'SELECTMOUSE', 'PRESS', any=True)
			kmi_props_setattr(kmi.properties, 'release_confirm', True)
			kmi.active = True
			select_border_keymap.append((km, kmi))



			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.select_all', 'A', 'PRESS', oskey=True)
			kmi.active = True
			select_border_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('mesh.select_all', 'A', 'PRESS', oskey=True)
			kmi.active = True
			select_border_keymap.append((km, kmi))





		######################################################
		######################################################
		#Select Linked
		if addon_prefs.select_link == True:

			km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK')
			kmi_props_setattr(kmi.properties, 'limit', True)
			kmi_props_setattr(kmi.properties, 'deselect', False)
			kmi.active = True
			select_linked_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
			kmi_props_setattr(kmi.properties, 'limit', True)
			kmi_props_setattr(kmi.properties, 'deselect', False)
			kmi.active = True
			select_linked_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', ctrl=True)
			kmi_props_setattr(kmi.properties, 'limit', True)
			kmi_props_setattr(kmi.properties, 'deselect', True)
			kmi.active = False
			select_linked_keymap.append((km, kmi))




			#UV Select Linked
			km = wm.keyconfigs.addon.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('uv.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK')
			kmi.active = True
			select_linked_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('uv.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
			kmi_props_setattr(kmi.properties, 'extend', True)
			kmi.active = True
			select_linked_keymap.append((km, kmi))









 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- Delete >> BACK SPACE  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #




		km = wm.keyconfigs.addon.keymaps.new('Object Mode', space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('object.delete', 'BACK_SPACE', 'PRESS')
		kmi.active = True
		ccc.append((km, kmi))



		km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('mesh.delete_by_select_mode_x', 'BACK_SPACE', 'PRESS')
		kmi.active = True
		ccc.append((km, kmi))



		km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('mesh.dissolve_mode', 'BACK_SPACE', 'PRESS', alt=True)
		kmi.active = True
		ccc.append((km, kmi))










		######################################################
		######################################################
		# 視点変更
		#------------3d View
		# 1,2,3
		if addon_prefs.view_numpad == True:

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS')
			kmi_props_setattr(kmi.properties, 'type', 'FRONT')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS')
			kmi_props_setattr(kmi.properties, 'type', 'RIGHT')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS')
			kmi_props_setattr(kmi.properties, 'type', 'TOP')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))


			# 1,2,3 + Ctrl
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'type', 'BACK')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'type', 'LEFT')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'type', 'BOTTOM')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))

			# align_active …… 1,2,3 + Alt

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'ONE', 'PRESS', alt=True)
			kmi_props_setattr(kmi.properties, 'type', 'TOP')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'TWO', 'PRESS', alt=True)
			kmi_props_setattr(kmi.properties, 'type', 'RIGHT')
			kmi_props_setattr(kmi.properties, 'align_active', True)
			kmi.active = True
			view_numpad_keymap.append((km, kmi))


			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

			kmi = km.keymap_items.new('view3d.viewnumpad', 'THREE', 'PRESS', alt=True)
			kmi_props_setattr(kmi.properties, 'type', 'FRONT')
			kmi_props_setattr(kmi.properties, 'align_active', True)
			kmi.active = True
			view_numpad_keymap.append((km, kmi))



# Camera

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('view3d.viewnumpad', 'FOUR', 'PRESS')
			kmi_props_setattr(kmi.properties, 'type', 'CAMERA')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))




			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('wm.context_toggle', 'FOUR', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'data_path', 'space_data.lock_camera')
			kmi.active = True
			view_numpad_keymap.append((km, kmi))



# Render

			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('render.render', 'FIVE', 'PRESS')
			kmi_props_setattr(kmi.properties, 'animation', False)
			kmi_props_setattr(kmi.properties, 'use_viewport', True)
			kmi.active = True
			view_numpad_keymap.append((km, kmi))











 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- Mesh Tool --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #






		km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('mesh.knife_tool', 'Z', 'PRESS', ctrl=True)
		kmi.active = True
		ccc.append((km, kmi))



		km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('mesh.inset', 'S', 'PRESS', shift=True,alt=True)
		kmi.active = True
		ccc.append((km, kmi))










 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- Transform AXIS-Y >> C --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #













 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- View Rotate/move --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #




		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('view3d.rotate', 'SELECTMOUSE', 'PRESS', oskey=True)
		kmi.active = True
		ccc.append((km, kmi))





		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('view3d.move', 'MIDDLEMOUSE', 'PRESS', oskey=True)
		kmi.active = True
		ccc.append((km, kmi))



 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- view all / selected  >>   --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #



		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('view3d.view_all', 'A', 'PRESS', ctrl=True, oskey=True)
		kmi.active = True
		ccc.append((km, kmi))

		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('view3d.view_selected', 'A', 'PRESS', shift=True, oskey=True)
		kmi.active = True
		ccc.append((km, kmi))


#
		######################################################
		######################################################
		# mose set
		if addon_prefs.mode_set == True:


			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
			kmi_props_setattr(kmi.properties, 'mode', 'POSE')
			kmi.active = True
			mode_set_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Pose', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
			kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))



	#Sculpt mode
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
			kmi_props_setattr(kmi.properties, 'mode', 'SCULPT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Sculpt', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', shift=True)
			kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))



	#Weight paint
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', alt=True)
			kmi_props_setattr(kmi.properties, 'mode', 'WEIGHT_PAINT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Weight Paint', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', alt=True)
			kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))





	 #Texture paint
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'mode', 'TEXTURE_PAINT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Image Paint', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True)
			kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))


	#Vertex paint
			km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True, alt=True)
			kmi_props_setattr(kmi.properties, 'mode', 'VERTEX_PAINT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))

			km = wm.keyconfigs.addon.keymaps.new('Vertex Paint', space_type='EMPTY', region_type='WINDOW', modal=False)
			kmi = km.keymap_items.new('object.mode_set', 'TAB', 'PRESS', ctrl=True, alt=True)
			kmi_props_setattr(kmi.properties, 'mode', 'OBJECT')
			kmi.active = True
			mode_set_keymap.append((km, kmi))







 # # # # # # # #
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('--  --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 ################################################################
		km = wm.keyconfigs.addon.keymaps.new('Info',space_type='EMPTY', region_type='WINDOW', modal=False)
		kmi = km.keymap_items.new('-- Modifier Add --', 'MINUS', 'PRESS')
		kmi.active = False
		ccc.append((km, kmi))
 ################################################################
 # # # # # # # #


		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('object.modifier_add', 'FOUR', 'PRESS', ctrl=True, oskey=True)
		kmi_props_setattr(kmi.properties, 'type', 'MIRROR')
		kmi.active = True
		ccc.append((km, kmi))

		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('object.subdivision_set', 'ONE', 'PRESS', oskey=True)
		kmi_props_setattr(kmi.properties, 'level', 0)
		kmi.active = True
		ccc.append((km, kmi))

		km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')
		kmi = km.keymap_items.new('object.subdivision_set', 'THREE', 'PRESS', oskey=True)
		kmi_props_setattr(kmi.properties, 'level', 2)
		kmi.active = True
		ccc.append((km, kmi))






 # # # # # # # #
 ################################################################


 ################################################################
 # # # # # # # #





def unregister():
	bpy.utils.unregister_module(__name__)
	# handle the keymap
	for km, kmi in ccc:
		km.keymap_items.remove(kmi)
	ccc.clear()


	# clear the list
	del ccc[:]
