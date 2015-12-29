bl_info = {
"name": "Compact_Properties _x3",
"author": "bookyakuno",
"version": (1.0),
"blender": (2, 76),
"location": "Please add a shortcut object.compact_prop",
"description": "Simple Panel",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "3D View"}



import bpy




class DialogOperator(bpy.types.Operator):
    bl_idname = "object.compact_prop"
    bl_label = "Compact Properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
#        col.label(text="Hello World!!")
        view = context.space_data
        scene = context.scene
        obj = context.object
        obj_type = obj.type











### アイテム
        ob = context.active_object
        row = layout.row()
        row.label(text="", icon='OBJECT_DATA')
        row.prop(ob, "name", text="")

        if ob.type == 'ARMATURE' and ob.mode in {'EDIT', 'POSE'}:
            bone = context.active_bone
            if bone:
                row = layout.row()
                row.label(text="", icon='BONE_DATA')
                row.prop(bone, "name", text="")




### Amaranth Toolset のフレームオンシェード(displayWireframe)


        row = col.row(align=True)
        row.operator("object.amth_wire_toggle" ,
                                 icon="MOD_WIREFRAME", text="Display").clear = False
        row.operator("object.amth_wire_toggle" ,
                                 icon="X", text="Clear").clear = True
        row = col.row(align=True)
        row.operator("mesh.presel", text="PreSel" ,icon="LOOPSEL")
        row.operator("presel.stop", text="PreSel" ,icon="X")
			







### その他いろいろ
        col = layout.column(align=True)


        layout.separator()
        row = layout.row()
        row.prop(view, "show_world", text="World.")
#        row.prop(view, "lock_camera", text="Lok.Cam")


#        col.prop(view, "show_only_render")        
        row = layout.row()
        row.prop(obj, "show_x_ray", text="X-Ray.")
        row.prop(obj, "show_wire", text="Wire")

        col = layout.column(align=True)
        col.operator("view3d.view_persportho", text="View Persp/Ortho")  
        
        rd = scene.render
        
        
        
        layout.separator()
        col = layout.column(align=True)
        col.prop(view, "use_matcap")
        if view.use_matcap:
            col.template_icon_view(view, "matcap_icon")
        col.prop(view, "show_backface_culling")
        
        
        

        if rd.has_multiple_engines:
            layout.prop(rd, "engine", text="")





#PreSel








        
### AO
        
        
        col = layout.column(align=True)
        fx_settings = view.fx_settings

        if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
            sub = col.column()
            sub.active = view.region_3d.view_perspective == 'CAMERA'
            sub.prop(fx_settings, "use_dof")
            col.prop(fx_settings, "use_ssao", text="Ambient Occlusion")
            if fx_settings.use_ssao:
                ssao_settings = fx_settings.ssao
                subcol = col.column(align=True)
                subcol.prop(ssao_settings, "factor")
                subcol.prop(ssao_settings, "distance_max")
                subcol.prop(ssao_settings, "attenuation")
                subcol.prop(ssao_settings, "samples")
                subcol.prop(ssao_settings, "color")

        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        
        
        
### 自動キーフレーム挿入        

        row = layout.row(align=True)
        row.prop(toolsettings, "use_keyframe_insert_auto", text="", toggle=True)
        if toolsettings.use_keyframe_insert_auto:
            row.prop(toolsettings, "use_keyframe_insert_keyingset", text="", toggle=True)

            if screen.is_animation_playing and not userprefs.edit.use_keyframe_insert_available:
                subsub = row.row(align=True)
                subsub.prop(toolsettings, "use_record_with_nla", toggle=True)

        
        
"""
                

        









        return {'FINISHED'}

"""




class play_hide(bpy.types.Operator):
    bl_idname = "object.play_hide"
    bl_label = "PLAY & HIDE"



    def execute(self, context):

        

        if (bpy.context.screen.is_animation_playing == False):
            	bpy.context.space_data.show_only_render = True
            	bpy.ops.screen.animation_play(reverse=False, sync=False)
        
        else:
            	bpy.context.space_data.show_only_render = False
            	bpy.ops.screen.animation_play(reverse=False, sync=False)

        

        return {'FINISHED'}


"""
   
        
        
        
        
        
        
        
        
        
        
        


def register():
    bpy.utils.register_class(DialogOperator)
#    bpy.utils.register_class(play_hide)
def unregister():
    bpy.utils.unregister_class(DialogOperator)
#    bpy.utils.unregister_class(play_hide)
if __name__ == "__main__":
    register()

