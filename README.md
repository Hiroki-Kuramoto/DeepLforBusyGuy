DeepLforBusyGuy solves the following problems.

- You want to translate an English text, but you can't copy it (e.g., the English text in an image).

- When you copy and paste on the DeepL website, the sentenses you copied contain line breaks in improper places and you can't translate the text properly.

By default, this tool translate English to Japanese as you can see in `settings.cfg`, but you may be able to use another language sets.

# DeepLforBusyGuy
今回紹介する「[DeepLforBusyGuy]([DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy))」は，以下のような問題を解決します．
- 英文を翻訳したいけど，コピーできない（e.g., 画像中の英文）
- コピー&ペーストすると変なところに改行が入ってうまく翻訳できない

# あらまし

”忙しい人のための”シリーズをご存じでしょうか？
忙しいくて急いでいる人にも内容を知ってもらうために，様々なコンテンツを要約してあげようという取り組みです．

- [忙しい人のための「翼をください」](https://www.youtube.com/watch?v=kkb-0AdXJu0)
- [忙しい人のための「大きな古時計」](https://www.youtube.com/watch?v=4m-Dn6cpyS0)

さて，今回紹介するのは，デスクトップに表示されている英語を日本語に翻訳し，さらにその要約を表示するツール [DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy) です．

デスクトップ上の翻訳したい英文を矩形選択すると，OCRで文字を認識し，DeepL REST APIを通して日本語に翻訳します．また内部で深層学習ライブラリのpysummarizeによって，要約文を生成します．

早速，使ってみましょう．

# 使い方
## セットアップ編
1. まずDeepLの無料のAPIキーを取得します[[ここから]](https://www.deepl.com/pro#developer)．
2. [DeepLforBusyGuy](https://github.com/Hiroki-Kuramoto/DeepLforBusyGuy)をクローン
3. クローンしたディレクトリに移動
4. `settings.cfg`のにある`DEEPL_KEY`に(1.)で取得したDeepLキーを貼り付ける．
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

## Contribution
<img width="500" alt="スクリーンショット 2022-11-11 14.52.29.png (68.1 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/11/104140/3f00072d-3d1a-4742-9afc-33c2ed37dcc9.png">

DeepLforBusyGuyが，同様の機能を備えている DeepL desktop を凌駕していることを示します．

<details><summary><img width="20" alt="スクリーンショット 2022-11-11 14.36.21.png (10.6 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/11/104140/7b5c3356-25fd-43dc-821d-2bfe8e7d7cce.png">DeepL desktopによる翻訳</summary>
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

ACMは、コンピュータや情報技術に関する数十の分野で、50以上の学術的な査読付きジャーナルを発行しています。
を出版しています。 ACMのインパクトのある査読付きジャーナルは、印刷物でもオンラインでも入手可能です。
ACMのインパクトのある査読付きジャーナルは、コンピューティングの革新に関する膨大で包括的なアーカイブを構成しています。
実用的かつ理論的なアプリケーションのための新旧のコンピューティング研究を網羅し、コンピューティングイノベーションの広大かつ包括的なアーカイブを構成しています。ACMジャーナル編集者は、各分野の
ACMのジャーナル編集者は各分野のソートリーダーであり、ACMは迅速な出版に重点を置いているため、エキサイティングな新しいアイデアや発見の伝達の遅れを最小限に抑えることができます。
ACMは迅速な出版を重視しており、エキサイティングな新しいアイデアや発見の伝達を最小限に抑えます。

＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
</details>
<details ><summary><img width="20" alt="スクリーンショット 2022-11-11 14.40.46.png (124.3 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/11/104140/bb5293e5-6703-4ec9-aa9d-3bf47f987635.png">DeepLforBusyGuyによる翻訳</summary>
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

ACMは、コンピューティングと情報技術の多くの分野で50以上の学術的な査読付きジャーナルを発行しています。印刷版とオンライン版があり、ACMの高インパクトの査読付きジャーナルは、実用と理論の両方のアプリケーションのための新興および既存のコンピューティング研究をカバーし、コンピューティング革新の広大で包括的なアーカイブを構成しています。
ACMのジャーナル編集者は各分野のソートリーダーであり、ACMは迅速な出版を重視しているため、刺激的な新しいアイデアや発見を伝えるのに遅れはほとんどありません。

＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
</details>

上記は，章「使ってみる」で扱ったACM Journalの説明文を翻訳した結果です．

<img width="20" alt="スクリーンショット 2022-11-11 14.36.21.png (10.6 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/11/104140/7b5c3356-25fd-43dc-821d-2bfe8e7d7cce.png">DeepL desktopでは，「〜を発行しています。を出版しています。 」という適切でない翻訳が返ってきます．

<img width="20" alt="スクリーンショット 2022-11-11 14.40.46.png (124.3 kB)" src="https://img.esa.io/uploads/production/attachments/17714/2022/11/11/104140/bb5293e5-6703-4ec9-aa9d-3bf47f987635.png">DeepLforBusyGuyは，そういった問題を解決していることがわかります．

## Issues
- 要約の精度が悪い
多くの場合，最初の一文をちょこっとだけ変えて表示されるだけになっている．（期待しないでという意味を込めて，薄く表示しています）
今後，アップデートするかもしれません．
