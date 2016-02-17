

bl_info = {
    "name": "Resolution X-Y Change",
    "author": "bookyakuno",
    "version": (1.0),
    "blender": (2, 76, 0),
    'location': 'Properties > Render > Dimensions > X - Y',
    "description": "Change Resolution X and Y ",
    "category": "Render",
}





import bpy




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

    rd = context.scene.render
    layout = self.layout

    col = layout.column(align=True)
    row = col.row(align=True)
    row.operator("object.x_y_change", icon="FILE_REFRESH")



def register():
    bpy.utils.register_class(x_y_change)
    bpy.types.RENDER_PT_dimensions.append(x_y_change_ui)


def unregister():
    bpy.utils.unregister_class(x_y_change)
    bpy.types.RENDER_PT_dimensions.remove(x_y_change_ui)


if __name__ == "__main__":
    register()

    # test call
#    bpy.ops.object.x_y_change()
