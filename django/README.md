# django環境の始め方
djangoを使ったAPサーバ。

## 注意
今回の環境はサンプルにつき、`settings.py`を`SECRET_KEY`そのまま含めている。
自分で利用する場合は、
`test_app`をまるっと削除し、
composeファイルの`command: python3 manage.py runserver 0.0.0.0:8080`をコメントアウトした上で、

コンテナ内に入って、
```commandline
django-admin startproject test_app .
```
を実行しsetting.pyを含むアプリを生成、
setting.pyの以下を変更すること
``` python
ALLOWED_HOSTS = ['localhost', '0.0.0.0']
```

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'POST': 3306
    }
}
```

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