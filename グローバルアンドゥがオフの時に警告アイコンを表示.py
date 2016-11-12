# ヘッダーなどの、入れたい付近のアイコンなどを右クリックして、
# ソースを編集、
# 下記をコピペして保存

        userpref = context.user_preferences
        system = userpref.system
        edit = userpref.edit
        row = layout.row()
        col = row.column()
        if bpy.context.user_preferences.edit.use_global_undo== False:
            col.prop(edit, "use_global_undo", icon="ERROR",text="")


