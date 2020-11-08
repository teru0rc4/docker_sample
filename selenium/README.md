# TensolFlow環境の始め方
## imageのビルド
```
docker-compose build
```

## コンテナの起動、tensolflowサーバーの立ち上げ
```
docker-compose up -d
```

## VNCでの確認
macの場合はFinder→移動→サーバへ接続→サーバアドレス `vnc://localhost:5900`でVNCに接続
passwordは`secret`

## 実行する方法
`docker-compose exec selenium bash`でコンテナ内に入って、`python3 sample.py `で実行
