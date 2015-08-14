# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Sorry, but the key map assignments please do manually.  >> " object.delete_xxx "

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
		bpy.ops.anim.keyframe_delete_v3d() #これが実際に削除するやつ。普通にAlt + Iから実行する方は、『警告 + この文』を実行しているので、この文だけを実行させる
		return {'FINISHED'}



def menu_func(self, context):
    self.layout.operator(DeleteUnmassage_xxx.bl_idname)

def register():
    bpy.utils.register_class(DeleteUnmassage_xxx)




def unregister():
    bpy.utils.register_class(DeleteUnmassage_xxx)







    
# メイン関数
if __name__ == "__main__":
    register()
