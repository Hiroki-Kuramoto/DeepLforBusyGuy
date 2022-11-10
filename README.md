"[DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy)" solves the following problems.
- You want to translate an English text, but you can't copy it (e.g., the English text in an image).
- When you copy and paste on the DeepL website, the sentenses you copied contain line breaks in improper places and you can't translate the text properly.

今回紹介する「[DeepLforBusyGuy]([DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy))」は，以下のような問題を解決します．
- 英文を翻訳したいけど，コピーできない（e.g., 画像中の英文）
- コピー&ペーストすると変なところに改行が入ってうまく翻訳できない

# あらまし

”忙しい人のための”シリーズをご存じでしょうか？
忙しいくて急いでいる人にも内容を知ってもらうために，様々なコンテンツを要約してあげようという取り組みです．

- [忙しい人のための「翼をください」](https://www.youtube.com/watch?v=kkb-0AdXJu0)
- [忙しい人のための「大きな古時計」](https://www.youtube.com/watch?v=4m-Dn6cpyS0)

さて，今回紹介するのは，デスクトップに表示されている英語を日本語に翻訳し，さらにその要約を表示するツール[DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy)です．

デスクトップ上の翻訳したい英文を矩形選択すると，OCRで文字を認識し，DeepL REST APIを通して日本語に翻訳します．また内部で深層学習ライブラリのpysummarizeによって，要約文を生成します．

早速，使ってみましょう．

# 使い方
## セットアップ編
1. まずDeepLの無料のAPIキーを取得します[[ここから]](https://www.deepl.com/pro#developer)．
2. [DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy)をクローン
3. クローンしたディレクトリに移動
4. `exe.py`の先頭の方にあるグローバル変数`DEEPL_KEY`に(1.)で取得したDeepLキーを貼り付ける．
5. `pip install -r requirements.txt`
6. `sudo python exe.py`
指示に応じて画面の監視やキーボード入力の監視の権限をTerminalに付与する必要があります．

以下の表示がでれば，成功です．

 <img width="484" alt="スクリーンショット 2022-11-10 15.58.23.png (78.9 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/10/104140/3b9bb569-cd2d-4119-aa98-7c587888fcb0.png">

さて，実際に動かしてみましょう．

## 使ってみる
1. まず翻訳&要約したい文章の左上（topLeft）の位置にマウスを置いて，[SPACE]キーを押します．
<img width="1077" alt="スクリーンショット 2022-11-10 16.02.41.png (389.2 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/10/104140/89e93165-6cb6-4c1c-9dc8-65590d9c6a36.png">

すると，
<img width="727" alt="スクリーンショット 2022-11-10 16.03.31.png (171.2 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/10/104140/1a790ea6-c6b5-4fea-9331-f01936f0370a.png">
[SPACE]キーが押されたことを認識し，その時のカーソルの位置を取得しました．

2. 次は，翻訳&要約したい文章の右下（bottomRight）を同じように指定します．
3. 数秒後に，翻訳された文章と，要約された文章が出力されます．（できた！）

<img width="927" alt="スクリーンショット 2022-11-10 16.09.31.png (651.1 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/10/104140/7c47270b-1e94-4e18-bdb1-de618eabe49d.png">

4. (1.)から繰り返せます．

## Issues
- 要約の精度が悪い
多くの場合，最初の一文をちょこっとだけ変えて表示されるだけになっている．（期待しないでという意味を込めて，薄く表示しています）
今後，アップデートするかもしれません．
