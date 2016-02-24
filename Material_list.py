bl_info = {
        "name": "material List",
    'description': '"material List from Hard Ops addon."',
    'author': 'bookyakuno',
    'version': (1,0),
    'blender': (2, 76, 0),
    'warning': "",
    'location': 'View3D > Ctrl + Shift + F',
    'category': 'Material'
}









import bpy


class material_list_menu_x(bpy.types.Menu):
    bl_label = 'material List'
    bl_idname = 'object.material_list_menu_x'

    def draw(self, context):
        layout = self.layout


        layout.menu("object.material_list_menu", icon='MATERIAL_DATA') #編集




def register():
    bpy.utils.register_module(__name__)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'F', 'PRESS', ctrl = True, shift = True)
        kmi.properties.name = "view3d.mymenu"

def unregister():
    bpy.utils.unregister_module(__name__)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['3D View']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu':
                if kmi.properties.name == "object.material_list_menu_x":
                    km.keymap_items.remove(kmi)
                    break

if __name__ == "__main__":
    register()

