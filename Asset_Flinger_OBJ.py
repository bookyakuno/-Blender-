import subprocess, os, bpy
from bpy.types import Operator, AddonPreferences, Panel
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty
from sys import platform as _platform
import bpy.utils.previews

bl_info = {
    'name': 'Asset Flinger OBJ export',
    'description': '"create OBJ for Asset Flinger addon"',
    'author': 'bookyakuno',
    'version': (1,0),
    'blender': (2, 76, 0),
    'warning': "",
    'location': 'View3D > Tool Shelf > Create > Asset Flinger OBJ',
    'category': 'Mesh'
}

#===============================================================

#===============================================================



class assetflinger_objPreferences(AddonPreferences):
    bl_idname = __name__



    temp_folder = StringProperty(
            name="Your Library",
            subtype='FILE_PATH',
            )


    def draw(self, context):
        layout = self.layout

        layout.prop(self, "temp_folder")






#===============================================================

#===============================================================

class assetflinger_obj(bpy.types.Operator):
    bl_idname = "ops.assetflinger_obj"
    bl_label = "instant meshes export"
    bl_options = {'REGISTER', 'UNDO'}
    bl_region_type = "WINDOW"

    operation = bpy.props.StringProperty()

    targetDir = "" # If nothing is specified, the 'home' directory is used

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if len(bpy.context.selected_objects) < 1:
            return {'CANCELLED'}




#===============================================================

#===============================================================

        #  OBJ 保存  =======================================================
        
        self.setUpPaths(context)

        active_object = bpy.context.active_object
        name = active_object.name
        objname = name + ".obj" # The temp object is called the same as the active object you have selected in Blender.
        bpy.ops.view3d.snap_cursor_to_selected() # Set 3D Cursor to the origin of the selected object

        try:
            bpy.ops.export_scene.obj(filepath=objname, use_selection=True, use_materials=False) # Exports the *.obj to your home directory (on Linux, at least) or the directory you specified above under the 'targetDir' variable
        except Exception as e:
            printErrorMessage("Could not create OBJ", e)
            return {'CANCELLED'}

        return {'FINISHED'}


#===============================================================

#===============================================================

        #  セットアップ パス  =======================================================


    def setUpPaths(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences


        self.targetDir = str(addon_prefs.temp_folder) # Set path for temp dir to store objs in


        if self.targetDir != "" and os.path.isdir(self.targetDir):
            os.chdir(self.targetDir)
        else:
            os.chdir(os.path.expanduser("~"))
            



class assetflinger_objPanel(bpy.types.Panel):
    """ """
    bl_label = "'Asset Flinger OBJ"
    bl_idname = "OBJECT_PT_assetflinger_obj"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Create"
    bl_context = "objectmode"



    def draw(self, context):

        layout = self.layout
        obj = context.object
        wm = context.window_manager
        row = layout.row()
        layout.operator("ops.assetflinger_obj", text="OBJ export", icon="PLAY").operation = "cmd"
        layout.operator("object.all_cmp", text="Thumbnail export", icon="PLAY").operation = "cmd"





#===============================================================

#===============================================================


# Utility functions
def printErrorMessage(msg, e):
    print("-- Error ---- !")
    print(msg, "\n", str(e))
    print("------\n\n")


def register():

    bpy.utils.register_class(assetflinger_obj)
    bpy.utils.register_class(assetflinger_objPanel)
    bpy.utils.register_class(assetflinger_objPreferences)



def unregister():
    bpy.utils.unregister_class(assetflinger_obj)
    bpy.utils.unregister_class(assetflinger_objPanel)
    bpy.utils.unregister_class(assetflinger_objPreferences)



if __name__ == "__main__":
    register()
