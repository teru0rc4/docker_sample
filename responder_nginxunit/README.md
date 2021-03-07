# nginx-unit+responder環境の始め方
nginx-unit+responderを使ったAPサーバ。

## imageのビルド
```commandline
docker-compose build --no-cache
docker-compose build up -d
```


## コンテナの起動、tensolflowサーバーの立ち上げ
```commandline
docker-compose up -d
```

## 
`curl localhost:8000`で`Hello, World!`、
`curl localhost:8000//hello/{who}`で`Hello, {who}!`を返す
