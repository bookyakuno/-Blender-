<!--
<link href="https://github.com/bookyakuno/img/blob/master/Blender_readme.css
" rel="stylesheet"></link>
<a class="button" href="#"><span>Hover</span><span>Button</span></a>

<p style="color:red;">ここの文字が赤くなる</p>
<p style="font-size:18px;color:#f00;">フォントサイズが18pxで赤文字で書く</p>

-->



# group_layer.py
アウトライナーでグループをレイヤーのように使うアドオン

* 全グループから除外
* 既存グループに追加
* 全除外して新規グループ作成
* グループに属さないものを_rootグループに追加

このアドオンの課題
* 事前に_rootグループを作成しておかなければならない


グループをレイヤーとして扱う既知の問題
* 階層化できない
* グループを複数共有できてしまう
  * このアドオンでグループ管理すれば複数共有が起きないよう修正。





# multi_ob_bake.py

複数のオブジェクトを結合したベイク用オブジェクトと、  
ベイク用ターゲットオブジェクト、  
ベイク用のテクスチャを作成し、  
すぐさまベイクできるように設定するアドオン。  
背景などの動かないオブジェクトをまるごと同じテクスチャにベイクしたい時に使える。  
  
<img src="https://github.com/bookyakuno/img/blob/master/multi_ob_bake.jpg" alt="multi_ob_bake">  
  
  
このアドオンは下記の2つのアドオンを利用します。  
インストール必須です。  
  
AddAsImageTexture  
https://github.com/chichige-bobo/BlenderPython/blob/master/AddAsImageTexture.py  
  
Blender-Scramble-Addon  
https://github.com/saidenka/Blender-Scramble-Addon  
  
  
  
  
下記のような、一連の動作を自動化します。  
  
2. 選択オブジェクトを複製し、名前を「アクティブオブジェクトの名前+"_target"」に変更  
3. モディファイア適用 (alt + Cの 「カーブ/メタ/サーフェス/テキストからメッシュ」)  
4. 選択オブジェクトを結合  
5. さらに1つ複製し、名前を「アクティブオブジェクトの名前+"_bake"」に変更  
6. Scramble Addon でマテリアル全削除  
8. 「UVの大きさを平均化」・「島をパッキング」でUVを隙間なく敷き詰める  
7. Scramble Addon でベイク用の新しいテクスチャを作成 1024px  
1. AddAsImageTexture でベイク用テクスチャを元にマテリアルを作成  
10. 選択 → アクティブ にチェックを入れて、レイの距離を0.01に設定  
  
あとは「結合」で全ての要素をベイクし、ベイクしたテクスチャを保存する  
  
※ 事前にUV展開済みの複数のオブジェクトを用意して選択しておくこと。  
※ ターゲットオブジェクトは削除してしまってかまわない。  
※ マテリアルを設定していないオブジェクトは、結合した時に勝手に他のマテリアルが割り当てられてしまうので注意。  
  
  



# dup_x.py  
パーツを表面にくっつけまくるアドオン。  
zbrushのアレをBlenderでもやりたいと思い作ってみた。  
下記の操作を順番にやる。  
1. スナップの各種項目を表面に吸着するように設定  
1. 選択オブジェクトをリンク複製  
1. 表面へ吸着  
1. スケール調整  
1. ローカルZ軸回転調整  


# vert_circle_x.py
選択している頂点を中心に円形を作るアドオン  
仕組みは簡単で  
頂点1つ選択状態から、  
拡張選択して、  
押し出して、  
円形にして、  
50%縮小しているだけ  
なので拡張選択で隣接してしまうほど近いとうまく円にできないので注意  
  
<a href="https://github.com/bookyakuno/-Blender-/raw/master/vert_circle_x.py" target="_blank">
    【このリンクを右クリック→名前を付けてリンク先を保存】
    </a>
  

# sharp_knife.py
# Snap Utilities Line bk.Edit  

  
標準のものより非常に吸着しやすいナイフアドオン。  
これはSnap Utilities Lineアドオンを元に、  
ナイフツールとして使いやすいよう編集したものです。  
サクサク切れます。  
~~あえてポリゴン作成できないようにしています。~~  
812行付近の、ポリゴン作成できないようにしたのを削除  
Y軸固定にYキーも追加して変更を修正  

<a href="https://github.com/bookyakuno/-Blender-/raw/master/sharp_knife.py" target="_blank">
    【このリンクを右クリック→名前を付けてリンク先を保存】
    </a>
  

<img src="https://github.com/bookyakuno/img/blob/master/sharp_knife.gif" alt="sharp_knife" >  
    
Home · Mano-Wii/Addon-Snap-Utilities-Line Wiki  
https://github.com/Mano-Wii/Addon-Snap-Utilities-Line/wiki  
  
▼ 変更点  
『##』 で始まるコメントアウトに変更点を書いたので検索してください。  
* センターへのスナップの許容範囲が強力に  
* 終了に、リターン(エンター)、スペース、Aキーを追加  
* Y軸固定にCキーを追加  
* 点とセンターの色を見やすく変更  
* ツールシェルフに出るパネルを削除  
  
▼ 標準のナイフツールと比べたメリット  
スナップの許容範囲が大きいので軽快に切れる  
ワンストロークずつ戻ることが可能  
  
▼デメリット  
突き抜けて分割が不可  
ワンストロークずつ履歴に残るので古い履歴に戻れなくなる  
標準のものでは一度にセンターを切ることができるが、これでは凸凹があると不可  
  
  
  
# Sculpt_status_header.py  
  
スカルプトモードでのステータスをヘッダーで確認できるアドオン。  
* ヘッダーで対称とダイナトポのステータスを確認
* ハイポリメッシュを多重解像度のレベルに変換する機能(convert_multiReso)
* マスク部分の分離
* マスク部分の複製
* グリースペンシルで切り取り
* グリースペンシルで囲った部分にマテリアルを割り当て(zbrushのポリグループっぽく)
  <img src="https://github.com/bookyakuno/img/blob/master/convert_multiReso.jpg" alt="Sculpt_status_header">  

  
# 45_rotate_gesture.py  
  
マウスホイールで45度回転する簡単ジェスチャーアドオン。  
  
90や180のような数値入力が楽になる。  
  
ショートカットはCtrl + Shift + D  
  
マウスホイール  
    …… ビュー視点で45/-45度回転  
Shift / Alt / Cmd + マウスホイール  
    …… X / Y / Z 軸指定45/-45度回転  
ZXCY  
    …… 軸指定 45度回転  
Shift + ZXCY  
    …… 軸指定 -45度回転  


<img src="https://github.com/bookyakuno/img/blob/master/45_rotate_gesture.gif" alt="45_rotate_gesture" >  
  
  
# easy_render_settings_check.py  
  
  
レンダリング設定を簡単に確認するアドオン。  
他にも  
X-Y解像度入れ替え  
レンダリングの履歴をスロットに保存など  
Properties >  
Render >  
Dimensions  
  
  
<img src="https://github.com/bookyakuno/img/blob/master/render_.jpg" alt="Sample" width="320px">  
  
  
# Curve & Array Set  
  
一発でカーブモディファイアと配列複製モディファイアを設定するアドオン。  
  
1.カーブ 2.オブジェクト の順に選択して、  
ツールシェルフの作成タブの  
" Curve & Array Set "を実行してください。  
カーブの名前は、『 "cv_" + オブジェクト名 』に自動でリネームされます。  
  
  
<img src="https://github.com/bookyakuno/img/blob/master/Curve_Array_Set.jpg" alt="Curve_Array_Set">  
  
  
# OBJ & Thumbnail for Asset Flinger  
  
Asset Flingerアドオンで使える、  
サムネ付きobjをすぐさま作成することを目的としたアドオン。  
オブジェクト名付きobjファイルと  
選択オブジェクトの小さいサムネイル画像を、  
指定したフォルダにすぐさま作成できる。  
  
  
<img src="https://github.com/bookyakuno/img/blob/master/Asset_Flinger.jpg" alt="Asset_Flinger">  
  
  
■ 使い方  
1. このアドオンをDLしてインストール  
2. 下記のリンクからAsset FlingerアドオンをDLしてインストール  
3. [BlenderAid/Asset-Flinger: Asset Flinger - Simple Mesh Importer for Blender](https://github.com/BlenderAid/Asset-Flinger)  
5. Asset Flinger アドオンの設定画面で、好きな場所のファイルパスを設定  
6. 2つのアドオンの設定画面で、Asset Flingerアドオンにて設定したファイルパスと同じファイルパスを設定  
7. 画像/UVエディターを分割表示しておく  
8. View3D > Tool Shelf > Create > Asset Flinger OBJ & Thumbnail ← ここにUIが追加されるので、OBJ Export と Thumbnail Export をそれぞれ実行。  
9. Thumbnail Export を実行すると画像/UVエディターにレンダリング結果が表示されるので、これを確認しながら何度か試して、良いアングルを見つけてください。  
10. 保存するとすぐに上書き保存がされるので、オブジェクト名がかぶらないように注意  
  
  
  
  
# info_header_useful.py  
  
Infoヘッダーを有効活用するアドオン。  
ヘッダーで名前が確認できるのは非常に便利  
最近使ったファイル一覧は、スプラッシュスクリーンよりスマート  
  
* 現在のフレームの確認、変更ができるように  
* 自動キーフレーム挿入ボタンを追加  
* 最近使ったファイル一覧を追加  
* 最新の自動保存を開けるように(最近使ったファイル一覧の一番下)  
* 選択中のオブジェクト名をリネームできるように  
* オブジェクトを名前で選択できるように  
  
<img src="https://github.com/bookyakuno/img/blob/master/info_header_useful.jpg" alt="info_header_useful">  
  
# Layer_M  
  
 Layer Managementを改良したアドオン。  
レイヤー移動とレイヤーの表示非表示、名前を確認すること以外のものを取り除いて、すっきりさせました。  
* プロパティシェルフに移動  
* 2列にして表示スペースを削減  
* パネルタイトルにレイヤー移動を追加  
* ワイヤーフレーム表示・ロックを非表示  
* レイヤー移動を左に移動  
* オプションをアイコン化  
  
  
<img src="https://github.com/bookyakuno/img/blob/master/Layer_m.jpg" alt="Layer_m">  
  
  
# SilentKeyDel.py  
  
  
  
現在のフレームのキーを『確認せずに』削除するアドオン。  
  
  
さいでんかさんのアドオン(saidenka/Blender-Scramble-Addon  
https://github.com/saidenka/Blender-Scramble-Addon )にある『確認せずに削除』系が大変作業が捗るので、"キーの削除"を自作してみた。  
  
アドオンをオンにし、以下を手動でショートカット登録してください  
  
object.delete_xxx  
  

# key_copypae_x.py  
  
  
アニメーションを補助する色々  
* タイムラインでキーのコピー・カット・ペースト  
    * shift + ctrl/cmd + X/C/V  
* ドープシートで開始・終了フレームを設定  
    * alt + S/E  
* 不要なものを非表示にして再生(PLAY & HIDE)  
    * プロパティシェルフ  
* キーを警告なしに削除  
    * バックスペース  
  
# save_all_renderlayers_and_passes_bk_edit.py  
  
レンダーレイヤーと各種パスを、名前を付け、フォルダにわけて保存してくれるアドオン"Create save_all_renderlayers_and_passes"を改良して、パスの名前が短くなるようにしました。  
135行付近です。  
  
ambient_occlusio      = ao  
combined              = cmb  
diffuse_color         = Dcl  
diffuse_direct        = Ddt  
diffuse_indirect      = Dit  
emit                  = emt  
environment           = evm  
glossy_color          = Gcl  
glossy_direct         = Gdt  
glossy_indirect       = Git  
material_index        = IDm  
object_index          = IDo  
mist                  = mst  
normal                = nml  
transmission_colo     = Tcl  
transmission_direct   = Tdt  
transmission_indirect = Tit  
shadow                = sdw  
subsurface_color      = Scl  
subsurface_direct     = Sdt  
subsurface_indirect   = Sit  
vector                = vcr  
 (z, UV はそのままでいいので除外)  


# rigify_select_pie_menu.py  
  
rigifyのリグを選択するパイメニューです。  
主要な部位の高速選択ができます。  
下記リンクの RigifyPicker アドオンと併用して下さい。  
  
Downloads | Salva Artero  
http://salvadorartero.com/downloads/  
  
  
# UbuntuAmbiance_bookyakunoEdit.xml  
  
Ubuntu Ambiance テーマを元に、気になった所を自分なりに改良したもの。  
  
   主張しすぎている赤紫を変更  
   メッシュは水色で、若干Maya準拠に  
   陰影処理のオンオフ表示をわかりやすく  
   グラフエディタのハンドルを大きく  
   薄いグラデーションで背景が平坦な印象にならないように  
  
Extensions:2.6/Py/Scripts/Interface/Themes/ - BlenderWiki  
http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Interface/Themes/  
  
  
# Compact_Properties.py  
  
プロパティシェルフにあるよく使う項目だけをダイアログで表示するアドオン。  
  
プロパティシェルフを極力使いたくない自分用に作ったアドオンです。  
  
AO・Matcap・ワイヤーフレーム表示に設定・選択オブジェクトをレントゲンに設定・ワールドの背景など。  
  
object.compact_prop  
Cmd + Ctrl + 3  
Shift + Ctrl + 3  
  
  
  
# Keymap set  
※ 再起動時に、アドオン設定画面で変更した設定が全て消える問題があるので、  
  
現状、変更は実質不可  
  
  
簡単に使いやすいショートカットを設定するアドオン。  
一般的なショートカットを設定することができます。  
このアドオンの設定にて、追加するキーマップの編集が可能です。  
  
* 矩形選択 …… マウスドラッグ  
* リンク選択 …… ダブルクリック  
* 削除・溶解 …… バックスペース  
メッシュ編集では、選択モードに応じて要素を削除するように  
* テンキーでのビュー変更 …… 1,2,3キー  
* カメラビューを4キー  
* レンダリングを5キー  
* トランスフォームY軸指定 …… Cキーでも可能に  
(キーボード左下のZXCで軸指定しやすいように)  
* ビューの回転と移動  
好きな様に変更して下さい  
* 全体を表示* 選択部分を表示  
MayaのようなA,Fキーなど、好きな様に変更して下さい  
* 対話モード …… Tab + 修飾キー  
■ バグ  
  
このアドオンのチェックを何度かオン・オフしていると、  
同じキーマップがいくつも生成されるが、重複するキーマップは、再起動に自動で消去される  
  
今の所3Dビューまわりのみだが、今後全エディターに対応する予定  
  
Mac基準(Cmdありき)のキー設定なので、Windowsユーザーは適宜キーマップを変更すること  
  
  
# Blender-Bookyakuno-config  
  
† 我以外扱うことの出来ない唯一無二の存在 †  
  
忘却野のキーコンフィグファイル  
キーコンフィグの参考にするだけでも  
  
  ▼▼このショートカット設定の推奨環境▼▼  
  
  
  
  ■  Mac(OS X)推奨  
   (Cmdキーを使用しているので)  
  
  ■  Ctrlキーをホームポジション小指近くに設定  
  (より多くのキーを押しやすくするため)  
  
  ■  5ボタンマウス推奨  
  (エンターと削除を副ボタンに割り当てる)  
  
  
  ■  LMBをセレクトマウスに設定  
  (一般的なマウス操作に合わせるため)  
  
  ■  外部キーリマップアプリでMMBとRMB入れ替え  
  (移動拡縮回転時の座標指定の操作を、押しやすい右クリックでやりたいので。  
 それに伴い、RMBが割り当てられている操作を全てMMBに変更した。文中でのRMBは実質MMB。  
 私は中ボタンクリックの硬さが死ぬほど嫌いなので、極力使用しない環境にしている。)  
  
  
  
  
  ■  「Wazou’s Pie Menu」アドオンを使用  
  (3Dビューのヘッダーでできることの大半を修飾キー各種 + MMBに割り当て)  
  Scripts-Blender/Wazou_Pie_Menus at master · pitiwazou/Scripts-Blender  
  https://github.com/pitiwazou/Scripts-Blender/blob/master/Wazou_Pie_Menus  
  
  
  
  ■  テンキー、「テンキーを模倣」を使用しない  
  視点変更は、123/Ctrl + 123に割り当てて場所を節約  
  数値入力は、karabinerを使用してQキーを押している間キーボード左側が一時的にテンキーになるように設定  
  
  
  
  
  
  
  ===============================================================  
  ===============================================================  
  
  
  
↓ ショートカット変更点 ↓  
  
  
  
  
◆視点変更  
123/Ctrl + 123  
場所を節約、かつ視点変更のショートカットを整理するため  
  
◆カメラ  
4  
現在の視点にカメラを合わせる  
4 + Ctrl  
フライナビゲーション  
4 + Ctrl + alt  
  
  
◆画像レンダリング  
5  
  
  
◆サブディビジョンレベル  
Cmd + 1 ……サブディビジョンレベル0  
Cmd + 3 ……サブディビジョンレベル2  
  
◆AutoMiller(編集モード中にもミラーを適応できるアドオン)  
Cmd + 4  
  
◆ミラー  
Cmd + Ctrl + 4  
  
  
◆適用(回転と拡縮)  
Shift + Cmd + 6  
ミラーやラジアルクローンなどがうまくいかない時に  
  
  
  
  
  
◆LMBドラッグを矩形選択に  
一般的なマウス操作に合わせるため。選択方法としてもやりやすいため。  
  
◆選択部分を表示  
  
◆全てを表示  
  
  
  
◆マウスでの視点操作  
Cmd + LMB ……視点を回転  
Cmd + RMB ……視点を移動  
  
◆煩わしいメッシュ削除  
さいでんか氏のアドオンセットScramble Addonにある、「メッシュ選択モードと同じ要素を削除する」で解消  
溶解は、「選択に溶解」を alt + delete に設定  
  
  
◆パイメニュー アドオンをRMB + 修飾キーにまとめる  
RMB + Shift + alt ……シェーディング  
RMB + Ctrl + alt ……座標系  
RMB + Cmd + alt ……スナップ対象  
RMB + Shift + Ctrl ……編集モード時のツールシェルフでできること各種  
RMB + Shift ……プリミティブ追加  
  
  
  
◆スナップ / プロポーショナル編集 のオンオフ  
V / B  
Mayaライクに  
  
  
  
◆  
7 ……選択物にカーソルを設定  
7ダブルクリック……カーソル  
8 ……カーソル位置に原点に設定  
※自分はこれを20ボタンマウスに設定しているが、  
 そうでない場合は5ボタンマウスで  
 alt + エンターなどのように割り当てるといいかもしれない。  
  
  
  
  
◆ナイフ  
Ctrl + Z  
  
  
  
  
  
  
  
◆移動 / 拡縮 / 回転  
A/S/D  
左手で押しやすく、XYZキーの近くするため  
  
  
◆外部キーリマップアプリで、CキーをYキーに入れ替え  
XYZのキーを揃えるため  
※文字打ちの時にCキーが押せなくなるので、CのタイプはCtrl + Cに割り当て  
  
  
  
◆対話モード変更をTab + 修飾キーにまとめる  
Tab ……編集  
Tabダブルクリック ……オブジェクト  
Tab + Shift ……スカルプト  
Tab + Ctrl  ……ポーズ  
Tab + Ctrl  ……ウェイトペイント  
Tab + alt  ……テクスチャペイント  
  
  
  
  
▼スカルプト  
アルファベット各種に設定  
  
Q/W/E ……ブラシ / Flatten(平らにする) / Clay Strips(ちょっとずつ塗りつける？)  
A/S/D ……ブラシサイズ変更 / スムース / Grab(つまむ)  
  
  
◆Blender終了をCmd + Qダブルクリックに  
(著者はkarabinerでアプリ全てに適応)  
  
  
  
  
  
◆ウィンドウ切り替え  
Shift + F1,F2,F2ダブルクリック,F3,F4,F5  
3Dビュー、アウトライナー、プロパティ、ユーザー設定、UV/画像エディター、ノードエディター  
(実際はパイメニューを使って済ませることが多い)  
  
  
◆スプラッシュスクリーン  
Cmd + 0  
最近使った項目に素早くアクセスするため。  
ちなみにダブルクリックで最近開いたファイルで最新のものを開く。  
  
  
  
その他諸々  
  
