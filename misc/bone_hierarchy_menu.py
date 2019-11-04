# ボーンを階層表示する
col = layout.column(align=True)
if not bpy.context.object == None:
  obj = bpy.context.object
  if obj.type == "ARMATURE":
    for bone in obj.data.bones: # 選択オブジェクトの全ボーンの中の (編集モードではeditbones)
      if not bone.parent: # 親がない(一番上)のボーンの
        col.prop(bone ,"name",text="",icon="ADD")

        for bone in bone.children: # 1つ子のボーン
          sp = col.split(align=True,factor=0.15)
          sp.label(text=str(len(bone.children_recursive)),icon="NONE") # 下階層の子ボーンの数
          sp.prop(bone ,"name",text="",icon="NONE")

          for bone in bone.children:
            bone_loop(bone,col,8) # メニュー。下記のfor文を内側に繰り返すことができれば行けそう
            for bone in bone.children:
              bone_loop(bone,col,9)
              for bone in bone.children:
                bone_loop(bone,col,10)
                for bone in bone.children:
                  bone_loop(bone,col,11)
                  for bone in bone.children:
                    bone_loop(bone,col,12)
                    for bone in bone.children:
                      bone_loop(bone,col,13)
                      for bone in bone.children:
                        bone_loop(bone,col,14)
          col.separator()
        col.separator()

        

def bone_loop(bone,col,range_c):
	rows = col.row(align=True)
	for i in range(range_c):
		rows.separator()
	rows.prop(bone ,"name",text="",icon="NONE")
