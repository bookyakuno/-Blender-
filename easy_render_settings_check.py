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
    "name": "easy render settings check",
    "author": "bookyakuno",
    "version": (1,1),
    "blender": (2, 78, 0),
    'location': 'Properties > Render > Dimensions',
    "description": "& X-Y Resolution Change, Render CycleSlot",
    "category": "Render",
}





import bpy



# class CyclesButtonsPanel:
#     bl_space_type = "PROPERTIES"
#     bl_region_type = "WINDOW"
#     bl_context = "render"
#     COMPAT_ENGINES = {'CYCLES'}
#
#     @classmethod
#     def poll(cls, context):
#         rd = context.scene.render
#         return rd.engine in cls.COMPAT_ENGINES

class render_cycleslots(bpy.types.Operator):
    bl_idname = "object.render_cycleslots"
    bl_label = "render_cycleslots"

    def execute(self, context):


        slots = bpy.data.images['Render Result'].render_slots
        slots.active_index=(slots.active_index+1)%8
        bpy.ops.render.render()

        return {'FINISHED'}


class x_y_change(bpy.types.Operator):
    """Tooltip"""
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



def x_y_change_ui(self, context):

    layout = self.layout

    scene = context.scene
    cscene = scene.cycles
    rd = context.scene.render


    scene = context.scene
    cscene = scene.cycles
    device_type = context.user_preferences.system.compute_device_type


    col = layout.column(align=True)
    row = col.row(align=True)
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

    # draw_samples_info(layout, context)

    row = col.row(align=True)

    row.prop(context.scene, 'save_after_render', text='Auto Save Image', toggle=False)





    snode = context.space_data
    snode_id = snode.id
    layout.prop(snode_id, "use_nodes")






def register():
    bpy.utils.register_class(render_cycleslots)
    bpy.utils.register_class(x_y_change)
    bpy.types.RENDER_PT_dimensions.append(x_y_change_ui)


def unregister():
    bpy.utils.unregister_class(render_cycleslots)
    bpy.utils.unregister_class(x_y_change)
    bpy.types.RENDER_PT_dimensions.remove(x_y_change_ui)


if __name__ == "__main__":
    register()

    # test call
#    bpy.ops.object.x_y_change()
