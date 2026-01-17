# Djangoの学習メモ

## 目次
- 現在実施したこと

1. Djangoを起動する
2. venvとは
3. ファイルの役割
4. ページを作成
5. ユーザーの作成
6. DjangoモデルのForeignKey


## 1. 現在実施したこと
- Djangoについて
- Djangoの環境構築
- CRUD
- 標準ビューを使用したCRUD
- バリデーションチェック
- ログインページ
- LoginRequiredMixin
- 一覧にページネーション
- 検索機能
- joinはとっとやれ！
- mysqlやsqliteなどの差を吸収しているか
- セッション、クッキー 

## 1. Djangoを起動する
### 1.1. Django 配下に移動する
```
cd project
```

### 1.2. venvをactivateにする
```
source venv/bin/activate
```

### 1.3. サーバーを起動する
```
python manage.py runserver 0.0.0.0:8000
```


## 2. venvとは
virtualenv が Python 3.3 から標準機能として取り込まれたもの。
→ virtualenv とは
   virtualenvは一つのシステムの中に分離されたPythonの仮想環境を作ることができるソフトウェア。
   コマンドで仮想環境を作ったり、仮想環境に出入りすることができる。

→ Pythonの仮想環境とは
   インストールしたモジュールやパッケージ、またPythonのバージョンごとに分離された環境のこと。
   依存関係の発生やそれぞれのバージョン違いによる問題などを、
   Pythonの仮想環境を作ってソフトウェアごとにバージョンの違うパッケージを用意することで、
   同じシステム内の環境を汚すこと無く開発することができる。

つまり、venv は、Pythonの仮想環境を作成するツール。
pip によるパッケージの導入状態をプロジェクトごとに独立させることができる。

→ 
virtualenvが使えなくなったわけではないが、
公式は、Python 3.3以降では、venvを推奨している。



## 3. ファイルの役割

django-adminを使うと作成してくれるファイルの役割。
- manage.py: 
  Django プロジェクトに対する様々な操作を行うためのコマンドラインユーティリティ。
  すべての Django コマンドは、最終的にここを通る。

実行の全体像として、
1. python manage.py runserver
2. manage.py が起動
3. settings.py 読み込み
4. INSTALLED_APPS の読み込み
5. urls.py の読み込み
6. DB接続準備

- config/: (作成者によって名称が異なる。)
  実際のプロジェクト用のPythonパッケージを含むディレクトリ。
  このディレクトリの名前は、内部のモジュールやパッケージをインポートするために使用するPythonパッケージ名になります

- config/__init__.py: 
  このディレクトリが Python パッケージであることを Python に知らせるための空のファイル。

- config/settings.py: 
  Djangoの設定ファイル。
  laravelでいうconfigやenv。

- config/urls.py: 
  Django プロジェクトの URL 宣言。

config/asgi.py: 
  プロジェクトをサーブするためのASGI互換Webサーバーとのエントリーポイント。
  ASGI ( Asynchronous Server Gateway Interface ) は WSGI の精神的な後継であり、
  非同期対応の Python Web サーバー、フレームワーク、およびアプリケーション間の標準インターフェイスを提供することを目的としている。
  →一旦勉強として後回し。

config/wsgi.py: 
  プロジェクトをサーブするためのWSGI互換Webサーバーとのエントリーポイント。
  →一旦勉強として後回し。



## 4. ページを作成

### 4.1. Modelの作成
DBの設計

作成後はマイグレーションする
```
python manage.py makemigrations
python manage.py migrate
```

### 4.2. URLの作成
app配下と、config配下それぞれ修正がいる。
- app配下
→ app/+++ で何があるか
- config配下
→ 読み込むファイルの設定

### 4.3. View
forms.pyの作成をする。
- 使用するModelの設定、フィールド
- バリデーション
- HTMLの自動生成
を行える。

views.pyの作成をする。
実際の動作の記載




## 5. ユーザーの作成
```
(venv) hoge@Django:~/study$ python manage.py createsuperuser
Username (leave blank to use 'hoge'): hoge
Email address: terayama419@gmail.com
Password:
Password (again):
Superuser created successfully.
```

→ ユーザー情報を管理画面で確認できるようにするか確認


## 5. LoginRequiredMixin
ログインしていないユーザーをログインページへ強制送還する仕組み。
LoginRequiredMixinをclassにつけるだけｍ未ログイン時へのアクセスするとログイン画面へリダイレクトされる。

LOGIN_URL = '/login/'


## 6. DjangoモデルのForeignKey
### 6.1. モデルを紐づけるリレーションフィールド
ForeignKeyは、Djangoのモデル間を紐づけるリレーションフィールドの一つ。
Djangoのモデルには以下の３種類のリレーションフィールドが用意されており、それらの違いはモデルデータ間の関係性にある。

|フィールド名|関係性|使用例|
|---|---|---|
|ForeignKey|一対多|学科
|ManyToManyField|多対多|講義
|OneToOneField|一対一|学生

PROTECT → 参照中のカテゴリは消せない
related_name='memos' → join学習に超便利

## 7. Django アプリケーションのライフサイクル
### 7.1. 全体像
1. ブラウザ HTTPリクエスト
2. URLルーティング
3. View（FBV / CBV）
4. Form（入力チェック）
5. Model / ORM（DB）
6. Template（HTML生成）
7. HttpResponse
8. ブラウザ


## 8. セッションは初期設定だとどこで管理するのか？
Djangoのセッションは、初期設定では「DB（データベース）」で管理される。

### 8.1. どこで確認するのか
settings.pyで確認する

1. INSTALLED_APPS
'django.contrib.sessions',
2. MIDDLEWARE
'django.contrib.sessions.middleware.SessionMiddleware',
3. セッションエンジン（デフォルト）
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

django_sessionというもので登録されている

login_required、request.userがセッション機構に依存している。

## mysqlやsqliteなどの差を吸収しているか
### Object-Relational Mapperを採用している

```
Memo.objects.filter(title__icontains='test')
```

SQLはDBごとに違うが、Djangoがある程度変換している。

### 吸収される範囲
1. CRUD
2. トランザクション
```
transaction.atomic()
```

### 吸収されない範囲
1. DB固有機能
mysqlのFULLTEXTやPostgreSQLの配列型など

### 生sqlの書き方
```
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM app_memo")
    rows = cursor.fetchall()
```

#### SQLインジェクション
プレースホルダを使用
```
cursor.execute(
    "SELECT * FROM app_memo WHERE title = %s",
    [title]
)
```

## ネクストアクション


- ユーザー情報を管理画面で確認できるようにするか確認
- memo をユーザー単位で完全分離
- CSRF / セキュリティ理解
- 権限（管理者だけ削除可能）
- middleware でアクセス制御
- Django セキュリティ設計
- ASGIとは何か
- WSGIとは何か
- どちらともどのような違いがあるか
