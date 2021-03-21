# django環境の始め方
djangoを使ったAPサーバ。

## imageのビルド
```commandline
docker-compose build --no-cache
docker-compose build up -d
```


## コンテナの起動
```commandline
docker-compose up -d
```

## djangoサーバの起動
ホスト側で下記のコマンドを実行してコンテナに入る
```commandline
docker-compose exec django bash
```

コンテナ内で以下のコマンドを実行
```commandline
python3 manage.py runserver 0.0.0.0:8080
```

ホスト側で、`http://localhost:8000/` または `0.0.0.0:8000`にアクセスする確認ができる
`settings.py`の`ALLOWED_HOSTS`に書き込まれているところが利用可能