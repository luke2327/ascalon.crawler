## Ascalon crawler

_Ascalon crawler_

eim で使うクローラーです
  
  
   
+ Scrapy version : [追加お願いします]
+ Python version : 2.7

- - -

持続的なクローリングのためEC2に置くクローラーです

## コード管理です。
1. 簡単な修正はEC2に接続して修正します。
2. 通常はローカルで組んだ後クローンを受けてテストを行います
+ 現在Rusoが外部テスト進行方案を検討中です。

## フォルダ構造
#### spiders [ascalon/spiders/]
実際にクローリングされるコードが集まっている場所です。

#### pipelines [ascalon/pipelines/]
スパイダーから引き渡されたクローリング データを処理する場所です。

#### settings [ascalon/settings]
クローラーの各種セッティングが集まっているところです。

## 使い方です
scrapy [コマンド] [スパイダー名]
+ + ex) scrapy crawl vod_youtube_list

## スパイダー命名規則
vod_youtube_list

最初のアンダーバーの前にある単語は、クローリング形式に合わせて書きます。 追って追加される予定です。
+ + ex) vod, hlvod, rating, game, blog, ...

## スパイダーの種類
1. ascalon.spiders.rating
2. ascalon.spiders.vod
3. ascalon.spiders.job
4. ascalon.spiders.item

- - -

2021-05-13 minor update
