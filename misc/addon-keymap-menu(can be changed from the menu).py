# "addon_keymaps" に登録されたアドオンのキーと一致するキーを、Blenderの設定内から検索して、表示するメニュー

box = layout.box()
col = box.column()
col.label(text="Keymap List:",icon="KEYINGSET")

wm = bpy.context.window_manager
kc = wm.keyconfigs.user
old_km_name = ""
for km_add, kmi_add in addon_keymaps:
    for km_con in kc.keymaps:
        if km_add.name == km_con.name:
            km = km_con

    for kmi_con in km.keymap_items:
        if kmi_add.name == kmi_con.name:
            # ここから  オペレーター名が同じで、プロパティが違う場合は、プロパティが同じものを判定する(例は"axis_x")。プロパティを設定していなければここは不要
            try:
                ad_pro = kmi_add.properties
                con_pro = kmi_con.properties
                if ad_pro.axis_x == con_pro.axis_x:
                    kmi = kmi_con
            except:
                # ここまで
                kmi = kmi_con
    try:
        if not km.name == old_km_name:
            col.label(text=str(km.name),icon="DOT")
        col.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
        col.separator()
        old_km_name = km.name
    except: pass

