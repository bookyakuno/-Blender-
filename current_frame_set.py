bl_info = {
"name": "current frame set _x3",
"author": "bookyakuno",
"version": (1.0),
"blender": (2, 76),
"location": " Shift + 3",
"description": "current frame set.",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "3D View"}


import bpy




class C_frame_set(bpy.types.Operator):
    bl_idname = "object.c_frame_set"
    bl_label = "Current frame set"
    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'UI'


    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout

        scene = context.scene


        layout.prop(scene, "frame_current", text="")



        return {'FINISHED'}








        # store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)
    # handle the keymap
#addon_keymaps = [] #put on out of register()
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = 'Window', space_type = 'EMPTY')

    kmi = km.keymap_items.new(C_frame_set.bl_idname, 'THREE', 'PRESS', shift=True)
    addon_keymaps.append((km, kmi))



def unregister():
    bpy.utils.unregister_module(__name__)
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
        
        

















        
# 
# 
# def register():
#     bpy.utils.register_class(C_frame_set)
# 
# def unregister():
#     bpy.utils.unregister_class(C_frame_set)
# 
# if __name__ == "__main__":
#     register()
# 

