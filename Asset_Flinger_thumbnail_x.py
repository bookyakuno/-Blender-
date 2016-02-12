bl_info = {
    "name": "Asset Flinger thumbnail_x",
    "author": "bookyakuno",
    "version": (1, 0),
    "blender": (2, 76, 0),
    "location": "D + shift + ctrl + cmd or 『 object.all_cmp 』",
    "description": "create thumbnail for Asset Flinger addon ",
    "warning": "",
    "category": "Render"}
    
    

    
import bpy
from bpy.props import BoolProperty, EnumProperty
from bpy.app.handlers import persistent
from os.path import dirname, exists, join
from bpy.path import basename
from os import mkdir, listdir
from re import findall


import subprocess, os, bpy
from bpy.types import Operator, AddonPreferences, Panel
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty
from sys import platform as _platform
import bpy.utils.previews



class ExampleAddonPreferences(AddonPreferences):
    bl_idname = __name__

    filepath_x = StringProperty(
            name="File Path",
            subtype='FILE_PATH',
            )

    def draw(self, context):
        layout = self.layout
#        layout.label(text="This is a preferences view for our addon")
        layout.prop(self, "filepath_x")



class OBJECT_OT_addon_prefs_example(Operator):
    """Display example preferences"""
    bl_idname = "object.addon_prefs_example"
    bl_label = "Addon Preferences Example"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        info = ("Path: %s, Number: %d, Boolean %r" %
                (addon_prefs.filepath, addon_prefs.number, addon_prefs.boolean))

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}


# Registration
def register():
    bpy.utils.register_class(OBJECT_OT_addon_prefs_example)
    bpy.utils.register_class(ExampleAddonPreferences)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_addon_prefs_example)
    bpy.utils.unregister_class(ExampleAddonPreferences)    
    
    
    

# ===============================================================

# ===============================================================


# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================



# ===============================================================

# ===============================================================


    

class InstantMesher(bpy.types.Operator):
    bl_idname = "ops.instantmesher"
    bl_label = "instant meshes export"
    bl_options = {'REGISTER', 'UNDO'}
    bl_region_type = "WINDOW"

    operation = bpy.props.StringProperty()

    # custom variables
    # Defined in the Blender addon preferences
    instantmeshesPath = "" # Path to the "instant Meshes"-executable
    sketchretopPath = "" # Path to the "Sketch-Retopo"-executable
    targetDir = "" # If nothing is specified, the 'home' directory is used

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if len(bpy.context.selected_objects) < 1:
            return {'CANCELLED'}


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

        if self.operation == "cmd":
            self.cmd(objname, context)

        elif self.operation == "regular":
            self.regular(objname, context)

        elif self.operation == "sketch":
            self.sketch(objname, context)

        try:
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR') # Set object origin to 3D Cursor
        except:
            bpy.ops.object.ogtc()


        self.operation = "regular"

        return {'FINISHED'}



    def setUpPaths(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        self.instantmeshesPath = str(addon_prefs.instant_path) # Set path for instant meshes
        self.sketchretopPath = str(addon_prefs.sketch_path) # Set path for Sketch-Retopo
        self.targetDir = str(addon_prefs.temp_folder) # Set path for temp dir to store objs in

        info = ("Path: %s" % (addon_prefs.instant_path))

        if self.instantmeshesPath == "":
            print("Path to 'instant Meshes' not specified. Terminating...")
            return {'CANCELLED'}

        if self.targetDir != "" and os.path.isdir(self.targetDir):
            os.chdir(self.targetDir)
        else:
            os.chdir(os.path.expanduser("~"))
            


    def cmd(self, objname, context):
        wm = context.window_manager
        creationTime = os.path.getmtime(objname) # Get creation time of obj for later comparison

        smoothingIts = str(wm.instantMesherSmoothingInt)
        allQuads = bool(wm.instantMesherQuadsBool)
        vertsAmount = wm.instantMesherVertexCountInt

        print("VERTSAMOUNT", str(vertsAmount))

        # try:
        if allQuads:
            vertsAmount = str(int(vertsAmount/4))
            subprocess.call([self.instantmeshesPath,  "-o", objname, "-S", str(smoothingIts), "-v", vertsAmount, objname]) # Calls Instant Meshes and appends the temporary *.obj to it
        else:
            subprocess.call([self.instantmeshesPath,  "-o", objname, "-S", str(smoothingIts), "-v", str(vertsAmount), "-D", objname]) # Calls Instant Meshes and appends the temporary *.obj to it

        # except Exception as e:
        #     printErrorMessage("Could not execute Instant Meshes", e)

        if(os.path.getmtime(objname) != creationTime):
            try:
                bpy.ops.import_scene.obj(filepath=objname) # Imports remeshed obj into Blender
            except Exception as e:
                printErrorMessage("Could not import OBJ", e)
                return {'CANCELLED'}
        else:
            print("Object has not changed. Skipping import...")
            pass

        try:
            os.remove(objname) # Removes temporary obj
        except Exception as e:
            printErrorMessage("Could not remove OBJ", e)





#===============================================================

#===============================================================

#===============================================================

#===============================================================

#===============================================================


#===============================================================

#===============================================================

#===============================================================

#===============================================================

#===============================================================



#===============================================================

#===============================================================

#===============================================================

#===============================================================

#===============================================================











class InstantMesherPanel(bpy.types.Panel):
    """ """
    bl_label = "OBJ EXPORT"
    bl_idname = "OBJECT_PT_instantmesher"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
#    bl_category = "Retopology"
    bl_context = "objectmode"



    def draw(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        instantmeshesPath = str(addon_prefs.instant_path)
        sketchPath = str(addon_prefs.sketch_path)
        layout = self.layout
        obj = context.object
        wm = context.window_manager
        row = layout.row()
        layout.operator("ops.instantmesher", text="OBJ export", icon="PLAY").operation = "cmd"



bl_idname = 'VIEW3D_PT_name'
bl_space_type = 'VIEW_3D'
bl_label = 'Name'
bl_region_type = 'TOOLS'
bl_options = {'HIDE_HEADER'}
bl_category = 'Name'

def register():

    bpy.utils.register_class(InstantMesher)
    bpy.utils.register_class(InstantMesherPanel)






def unregister():
    bpy.utils.unregister_class(InstantMesher)
    bpy.utils.unregister_class(InstantMesherPanel)




if __name__ == "__main__":
    register()
    
    
    
    
    
    

# ===============================================================

# ===============================================================


# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================
# ===============================================================



# ===============================================================

# ===============================================================


    
    
# 
# 
# class InstantMesherPreferences(AddonPreferences):
#     bl_idname = __name__
# 
#     instant_path = StringProperty(
#             name="Instant Meshes-executable path",
#             subtype='FILE_PATH',
#             )
# 
#     temp_folder = StringProperty(
#             name="folder to store temp objs",
#             subtype='DIR_PATH',
#             )
# 
#     sketch_path = StringProperty(
#             name="Sketch-Retopo-executable path",
#             subtype='FILE_PATH',
#             )
# 
    







# Auto Save Render
# game engine - How to take pictures from the GE? - Blender Stack Exchange
#http://blender.stackexchange.com/questions/27253/how-to-take-pictures-from-the-ge

def main(context):
    for ob in context.scene.objects:
        print(ob)


class save_thumbnail(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.save_thumbnail"
    bl_label = "save thumbnail"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        
        
        


        # # # # # # # #
        ################################################################

        ################################################################
        old_path = bpy.context.scene.render.filepath
        old_fileformat = bpy.context.scene.render.image_settings.file_format
        old_extension = bpy.context.scene.render.use_file_extension
        old_x = bpy.context.scene.render.resolution_x
        old_y = bpy.context.scene.render.resolution_y
        old_percentage = bpy.context.scene.render.resolution_percentage
        old_aspect_x = bpy.context.scene.render.pixel_aspect_x
        old_aspect_y = bpy.context.scene.render.pixel_aspect_y


        # # # # # # # #
        ################################################################

        ################################################################
        # path to the folder
        file_path = bpy.data.filepath
        file_name = bpy.path.display_name_from_filepath(file_path)
        file_ext = '.blend'
        file_dir = file_path.replace(file_name+file_ext, '')

        mainScreen = bpy.context.screen

        #current scene
        scene = mainScreen.scene 
        #set render settings
        scene.render.resolution_x = 128
        scene.render.resolution_y = 128
        scene.render.resolution_percentage = 100



        #render from view (set view_context = False for the camera render)
        bpy.ops.render.opengl(view_context = True)





        # # # # # # # #
        ################################################################

        ################################################################
        rndr = scene.render
        original_format = rndr.image_settings.file_format

        format = rndr.image_settings.file_format = scene.auto_save_format
        if format == 'OPEN_EXR_MULTILAYER': extension = '.exr'
        if format == 'JPEG': extension = '.jpg'
        if format == 'PNG': extension = '.png'  
        blendname = basename(bpy.data.filepath).rpartition('.')[0]


#         self.filepath_z = str(addon_prefs.filepath_x) # Set path for instant meshes
# 
#         if self.filepath_z == "":
#             print("Path to 'instant Meshes' not specified. Terminating...")
#             return {'CANCELLED'}

#        else:
#        filepath = dirname(bpy.data.filepath) + str(addon_prefs.filepath) #'/auto_saves'
#        filepath = os.path.basename(context.user_preferences.addons["save_thumbnail"].preferences.filepath_x)

        addon_preferences = bpy.context.user_preferences.addons[__name__].preferences
        filepath = dirname(bpy.data.filepath) + addon_preferences.filepath_x



            

#         user_preferences = context.user_preferences
#         addon_prefs = user_preferences.addons[__name__].preferences
# 
#         self.filepath_x = str(addon_prefs.filepath_x) # Set path for instant meshes
# 
#         info = ("Path: %s" % (addon_prefs.filepath_x))
# 
#         if self.filepath_x == "":
#             print("Path to 'instant Meshes' not specified. Terminating...")
#             return {'CANCELLED'}





        if not exists(filepath):
            mkdir(filepath)

        if scene.auto_save_subfolders:
            filepath = join(filepath, blendname)
        if not exists(filepath):
            mkdir(filepath)


        # # # # # # # #
        ################################################################

        ################################################################


        #imagefiles starting with the blendname
        files = [f for f in listdir(filepath) \
                if f.startswith(blendname) \
                and f.lower().endswith(('.png', '.jpg', '.jpeg', '.exr'))]
        
        highest = 0
        if files:
            for f in files:
                #find last numbers in the filename after the blendname
                suffix = findall('\d+', f.split(blendname)[-1])
                if suffix:
                    if int(suffix[-1]) > highest:
                        highest = int(suffix[-1])
        

            ###############################################################

        ################################################################
        # # # # # # # #


        active_object = bpy.context.active_object
        name = active_object.name

        #save and load the render (you can't keep the render result)
        #save_name = name + ".png"
#        save_name = join(filepath, blendname) + '_' + str(highest+1).zfill(3) + extension
        #save_name = scene.name+".png"

#改良前        save_name = join(filepath, blendname) + name + ".png"
#        save_name = join(filepath) + name + ".png"
        save_name = join(filepath) + name + ".png"


        image = bpy.data.images['Render Result']
        if not image:
            print('Auto Save: Render Result not found. Image not saved')
            return
        
        print('Auto_Save:', save_name)
        image.save_render(save_name, scene=None)

        rndr.image_settings.file_format = original_format



        # # # # # # # #
        ################################################################



        # restore old settings
        bpy.context.scene.render.filepath = old_path
        bpy.context.scene.render.image_settings.file_format = old_fileformat
        bpy.context.scene.render.use_file_extension = old_extension
        bpy.context.scene.render.resolution_x = old_x
        bpy.context.scene.render.resolution_y = old_y
        bpy.context.scene.render.resolution_percentage = old_percentage
        bpy.context.scene.render.pixel_aspect_x = old_aspect_x
        bpy.context.scene.render.pixel_aspect_y = old_aspect_y


        ################################################################
        # # # # # # # #
       
        
        
        return {'FINISHED'}



        # # # # # # # #
        ################################################################

        ################################################################
        # # # # # # # #



class all_cmp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.all_cmp"
    bl_label = "all_cmp"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)

#        old_shadingvariable = bpy.context.scene.object.shadingvariable
        #ソリッド表示にします
        bpy.ops.object.shadingvariable(variable="SOLID")

        #matcapを赤いものに設定     好きに設定して下さい
        bpy.context.space_data.matcap_icon = '12'
        
        #レンダリングするもののみ表示     これを消すとアウトライン付きになります
        bpy.context.space_data.show_only_render = True

        #平行投影/透視投影      平行投影にする
        bpy.ops.view3d.view_persportho()
        
        #サムネイル作成を実行する
        bpy.ops.object.save_thumbnail()


        #平行投影/透視投影      透視投影に戻す
        bpy.ops.view3d.view_persportho()

        #レンダリングするもののみ表示     表示を戻す
        bpy.context.space_data.show_only_render = False

        #instantmesher
        #bpy.ops.instantmesher
        #matcapを設定      よく使う元のmatcapに戻す
        bpy.context.space_data.matcap_icon = '06'
  
        
#xx        bpy.context.scene.object.shadingvariable = old_shadingvariable




        
        return {'FINISHED'}





        

        # store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)
    # handle the keymap
#addon_keymaps = [] #put on out of register()
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = '3D View', space_type = 'VIEW_3D')

    kmi = km.keymap_items.new(all_cmp.bl_idname, 'D', 'PRESS', shift=True, ctrl=True, oskey=True)
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
# 
# 
# def register():
#     bpy.utils.register_class(save_thumbnail)
#     bpy.utils.register_class(all_cmp)
#     bpy.utils.register_class(InstantMesherPreferences)
# 
# 
# def unregister():
#     bpy.utils.unregister_class(save_thumbnail)
#     bpy.utils.unregister_class(all_cmp)
#     bpy.utils.unregister_class(InstantMesherPreferences)
# 
# 
# if __name__ == "__main__":
#     register()
# 
#     # test call
#     bpy.ops.object.save_thumbnail()

