# Pie buttons order for a quick reference
# 4 - LEFT
# 6 - RIGHT
# 2 - BOTTOM
# 8 - TOP
# 7 - TOP - LEFT
# 9 - TOP - RIGHT
# 1 - BOTTOM - LEFT
# 3 - BOTTOM - RIGHT

import bpy
#
# bl_info = {
#     "name": "Jimmy_pie_uv",
#     "description": "Jimmy's UV select mode pie menu",
#     "category": "3D View",
# }


# Operators

class Placeholder(bpy.types.Operator):
    """Placeholder to get pie menu items in arbitrary positions"""
    bl_idname = "ui.placeholder"
    bl_label = ""

    @classmethod
    def poll(cls, context):
        return False

    def execute(self, context):
        return {'FINISHED'}


class SplitAndGrab(bpy.types.Operator):
    """Same as pressing Y, then G in UV editor"""
    bl_idname = "uv.split_and_grab"
    bl_label = "Rip Face"

    def execute(self, context):

        bpy.ops.uv.select_split()
        bpy.ops.transform.translate()

        return {'FINISHED'}


# Menu

class UvSelectMode(bpy.types.Menu):
    bl_label = "UV Select Mode"
    bl_idname = "pie.uv_select_mode"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'
        toolsettings = context.tool_settings
        pie = layout.menu_pie()

        _ = 0 if toolsettings.use_uv_select_sync else 1

        # Left
        op = pie.operator("wm.context_set_value", text="Vertex",
                          icon=('VERTEXSEL', 'UV_VERTEXSEL')[_])
        op.value = ("(True, False, False)", "'VERTEX'")[_]
        op.data_path = "tool_settings.%s_select_mode" % ('mesh', 'uv')[_]

        # Right
        op = pie.operator("wm.context_set_string",
        text="Island", icon='UV_ISLANDSEL')
        if _:
            op.value = 'ISLAND'
            op.data_path = "tool_settings.uv_select_mode"

        # Bottom
        op = pie.operator("wm.context_set_value", text="Face",
                          icon=('FACESEL', 'UV_FACESEL')[_])
        op.value = ("(False, False, True)", "'FACE'")[_]
        op.data_path = "tool_settings.%s_select_mode" % ('mesh', 'uv')[_]

        # Top
        op = pie.operator("wm.context_set_value", text="Edge",
        icon=('EDGESEL', 'UV_EDGESEL')[_])
        op.value = ("(False, True, False)", "'EDGE'")[_]
        op.data_path = "tool_settings.%s_select_mode" % ('mesh', 'uv')[_]

        # Top-left linked
        op = pie.operator("uv.select_linked", text="Select Linked",
                          icon="OUTLINER_OB_LATTICE")

        # Top-right
        op = pie.operator("wm.context_set_value", text="Sync Selection",
                          icon="UV_SYNC_SELECT")
        op.value = ("False", "True")[_]
        op.data_path = "tool_settings.use_uv_select_sync"

        # Bottom-left
        op = pie.operator("uv.stitch", icon="SNAP_ON")

        # Bottom-right
        op = pie.operator("uv.split_and_grab", text="Rip Face",
                          icon="MOD_MESHDEFORM")


addon_keymaps = []


def register():
    bpy.utils.register_module(__name__)

    # Keymap Config
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Image',
                                             space_type='IMAGE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'RIGHTMOUSE', 'PRESS')
        kmi.properties.name = "pie.uv_select_mode"

        addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_module(__name__)

    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        for km in addon_keymaps:
            for kmi in km.keymap_items:
                km.keymap_items.remove(kmi)

            wm.keyconfigs.addon.keymaps.remove(km)

    del addon_keymaps[:]

if __name__ == "__main__":
    register()
