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
	"name": "render check list + misc",
	"author": "bookyakuno",
	"version": (1, 0, 2),
	"blender": (2, 78),
	"location": "Dimensions",
	"description": "render check list + misc",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Render",
}

import bpy

from bpy.props import (BoolProperty,
					   FloatProperty,
					   FloatVectorProperty,
					   StringProperty,
					   PointerProperty)

from bpy.props import *




class set_f(bpy.types.Operator):
   bl_idname = "object.set_f"
   bl_label = "set_f"
   bl_description = "Change the number of sheets"
   def execute(self, context):

	   scn = context.scene

	   set_f = scn.frame_start + scn.floatSample
	   scn.frame_end = set_f

	   return {'FINISHED'}

class now_f(bpy.types.Operator):
   bl_idname = "object.now_f"
   bl_label = "now_f"
   bl_description = "Current number of sheets"

   def execute(self, context):

	   scn = context.scene

	   scn.floatSample = scn.frame_end - scn.frame_start


	   return {'FINISHED'}




# class SampleProperties(bpy.types.PropertyGroup):
# 	# boolSample = BoolProperty()
# 	floatSample = IntProperty(name="FloatPropSample",min=-1, max=10000, default=0)
# 	# floatVectorSample = FloatVectorProperty(name="Vector")
	# stringSample=StringProperty(name="text")


class SampleUI_PT_object(bpy.types.Panel):
	bl_label = "UI For Sample Prop"
	bl_context = "object"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"

	def draw(self, context):
		# self.layout.prop(context.object.sample_props,"boolSample")
		self.layout.prop(context.object.sample_props,"floatSample")
		# self.layout.prop(context.object.sample_props,"floatVectorSample")
		# self.layout.prop(context.object.sample_props,"stringSample")

		layout = self.layout
		row = layout.row(align=True)
		row.operator("object.fff", text="fff")



class render_cycleslots(bpy.types.Operator):
	bl_idname = "object.render_cycleslots"
	bl_label = "render_cycleslots"
	bl_options = {'REGISTER', 'UNDO'}
	bl_description = "Slots change every time rendering"

	def execute(self, context):


		slots = bpy.data.images['Render Result'].render_slots
		slots.active_index=(slots.active_index+1)%8
		#bpy.ops.render.render('EXECUTION_CONTEXT')
		bpy.ops.render.render('INVOKE_DEFAULT')
		return {'FINISHED'}


class x_y_change(bpy.types.Operator):
	bl_idname = "object.x_y_change"
	bl_label = "X-Y"

	def execute(self, context):
#        main(context)
		old_x = bpy.context.scene.render.resolution_x
		old_y = bpy.context.scene.render.resolution_y
		mainScreen = bpy.context.screen
		scene = mainScreen.scene
		scene.render.resolution_x = old_y
		scene.render.resolution_y = old_x

		return {'FINISHED'}












def render_final_resolution_ui_z(self, context):




	rd = context.scene.render
	layout = self.layout

	final_res_x = (rd.resolution_x * rd.resolution_percentage) / 100
	final_res_y = (rd.resolution_y * rd.resolution_percentage) / 100

	if rd.use_border:
		final_res_x_border = round(
			(final_res_x * (rd.border_max_x - rd.border_min_x)))
		final_res_y_border = round(
			(final_res_y * (rd.border_max_y - rd.border_min_y)))
		layout.label(text="Reso: {} x {} [Border: {} x {}]".format(
					 str(final_res_x)[:-2], str(final_res_y)[:-2],
					 str(final_res_x_border), str(final_res_y_border)))
	else:
		layout.label(text="Reso: {} x {}".format(
					 str(final_res_x)[:-2], str(final_res_y)[:-2]))





	layout = self.layout
	scene = context.scene
	cscene = scene.cycles
	rd = context.scene.render



	col = layout.column(align=True)
	row = col.row(align=True)


	row.operator_context = 'EXEC_DEFAULT'
	row.operator("render.render", text="Render", icon='RENDER_STILL')
	row.operator("object.render_cycleslots", icon="RENDER_REGION")
	row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
	row.prop(rd, "use_lock_interface", icon_only=True)
	row = col.row(align=True)



	row.operator("object.x_y_change", icon="FILE_REFRESH")



	# col = split.column()
	row = col.row(align=True)

	row.prop(cscene, "film_transparent", text="BG Alpha", icon="WORLD")
	row.prop(rd, "use_overwrite", icon="ORTHO")

	split = layout.split()
	row = col.row(align=True)
	row.prop(rd, "use_stamp", icon="OUTLINER_DATA_FONT")
	row.prop(cscene, "use_square_samples", icon="IPO_QUAD")




	row = col.row(align=True)
	row.prop(rd, "use_persistent_data", text="Persistent Images")
	row.prop(cscene, "samples", text="samples")
	row = col.row(align=True)

	row.prop(scene, "frame_current")
	row.prop(cscene, "preview_samples", text="Preview")


	# draw_samples_info(layout, context)

	row = col.row(align=True)

	row.prop(context.scene, 'save_after_render', text='Auto Save Image', toggle=False)


# =====================================================
# set flame
	layout = self.layout
	# row = layout.row(align=True)
	row = col.row(align=True)
	row.operator("object.now_f", text="now_f",icon="EYEDROPPER")
	row.operator("object.set_f", text="set_f",icon="FILE_TICK")
	row.prop(scene, "floatSample", text="")



















def register():
	bpy.utils.register_module(__name__)

	bpy.types.RENDER_PT_dimensions.append(render_final_resolution_ui_z)
	# bpy.types.Object.sample_props=PointerProperty(type=SampleProperties)



	bpy.types.Scene.floatSample = IntProperty(name="FloatPropSample", description="Number of sheets to be rendered", min=0, default=0)

	# floatSample = IntProperty(name="FloatPropSample",min=-1, max=10000, default=0)


def unregister():
	bpy.types.RENDER_PT_dimensions.remove(render_final_resolution_ui_z)
	# del bpy.types.Object.sample_props




if __name__ == "__main__":
	register()
