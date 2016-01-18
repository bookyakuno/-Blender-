# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Sorry, but the key map assignments please do manually.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



#ユーザー設定のアドオンリストに表示される色々
bl_info = {'name':'Silent Key Del',
            'author':'bookyakuno',
            'version':(0,1),
            'category':'Animation',
            'location':'" object.delete_xxx "  key map assignments please do manually  >>  3D View > Object Mode  , 3D View > Pose  , Timeline',
            'description':'When you delete a key frame, the message is not displayed. '}


# Blender内部のデータ構造にアクセスするために必要
import bpy


# 実際の内容
class DeleteUnmassage_xxx(bpy.types.Operator):
	bl_idname = "object.delete_xxx"
	bl_label = "Silent_Key_Del"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):


		if (context.active_object):
		    self.report(type={"INFO"}, message="Silent_Key_Del")			# Message


		bpy.ops.anim.keyframe_delete_v3d() #これが実際に削除するやつ。普通にAlt + Iから実行する方は、『警告 + この文』を実行しているので、この文だけを実行させる
		return {'FINISHED'}




# 実際の内容
class DeleteUnmassage_graph_silent_del(bpy.types.Operator):
	bl_idname = "graph.silent_del"
	bl_label = "silent_graph_Key_Del"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):



		if (context.active_object):
		    self.report(type={"INFO"}, message="Silent_Key_Del")			# Message


		bpy.ops.graph.delete()
		 #これが実際に削除するやつ。普通にAlt + Iから実行する方は、『警告 + この文』を実行しているので、この文だけを実行させる
		return {'FINISHED'}





#
#def menu_func(self, context):
#    self.layout.operator(DeleteUnmassage_xxx.bl_idname)
#
#def register():
#    bpy.utils.register_class(DeleteUnmassage_xxx)
# #   bpy.types.TIMELINE_MT_frame.append(menu_func)
#
#
#
#def unregister():
#    bpy.utils.register_class(DeleteUnmassage_xxx)
##    bpy.types.TIMELINE_MT_frame.remove(menu_func)
#    

# プラグインをインストールしたときの処理
#def register():
#    bpy.utils.register_class(DeleteUnmassage_xxx)




# プラグインをアンインストールしたときの処理
#def unregister():
#    bpy.utils.unregister_class(DeleteUnmassage_xxx)
    
# メイン関数
#if __name__ == "__main__":
#    register()
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ===============================================================
    
    #

def register():    #登録
    bpy.utils.register_class(DeleteUnmassage_xxx)
    bpy.utils.register_class(DeleteUnmassage_graph_silent_del)


#    bpy.utils.register_class(DeleteUnmassage_xxx)
#    kc = bpy.context.window_manager.keyconfigs.addon
#    if kc:
#        km = kc.keymaps.new(name='WINDOW', space_type='VIEW_3D' , region_type='WINDOW')

# ショートカットキー登録
#        kmi = km.keymap_items.new('object.delete_xxx', 'BACK_SPACE', 'PRESS', alt=True)


def unregister():    #登録解除
    bpy.utils.unregister_class(DeleteUnmassage_xxx)
    bpy.utils.unregister_class(DeleteUnmassage_graph_silent_del)

#    bpy.utils.unregister_class(DeleteUnmassage_xxx)
#    kc = bpy.context.window_manager.keyconfigs.addon
#    if kc:
#        km = kc.keymaps["WINDOW"]
#        for kmi in km.keymap_items:
#            if kmi.idname == 'object.delete_xxx':
#                km.keymap_items.remove(kmi)
#                break

if __name__ == "__main__":
    register()








# object.delete_xxx
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
