# React環境の始め方

## imageのビルド
```
docker-compose build
```


## reactの環境の作成(一回だけでよい)
```
docker-compose run --rm node sh -c "npm install -g create-react-app && create-react-app react-sample"
```
すると`react-sample`というディレクトリとサンプルのアプリが作成される。

立ち上げるアプリの名前を変える場合、`create-react-app react-sample`の名前と、
`docker-compose.yml`の`command: sh -c "cd react-sample && yarn start"`をそれぞれ変更する。


## コンテナの起動、reactサーバーの立ち上げ
```
docker-compose up -d
```

## ブラウザ上での確認
`http://localhost:3000/` へアクセスする。
