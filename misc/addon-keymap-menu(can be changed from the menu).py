# "addon_keymaps" に登録されたアドオンのキーと一致するキーを、Blenderの設定内から検索して、表示するメニュー

box = layout.box()
col = box.column()
col.label(text="Keymap List:",icon="KEYINGSET")

wm = bpy.context.window_manager
kc = wm.keyconfigs.user
for km_add, kmi_add in addon_keymaps:
    for km_con in kc.keymaps:
        if km_add.name == km_con.name:
            km = km_con

    for kmi_con in km.keymap_items:
        if kmi_add.name == kmi_con.name:
            kmi = kmi_con
    try:
        col.label(text=str(km.name),icon="DOT")
        col.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
        col.separator()
    except: pass


