# React環境の始め方

## imageのビルド
```
docker-compose build
```


## reactの環境の作成(一回だけでよい)
```
docker-compose run --rm react_node_service sh -c "npm install -g create-react-app && create-react-app react-sample"
```
`react_node_service`の部分はサービス名なので適宜変更すること

すると`react-sample`というディレクトリとサンプルのアプリが作成される。

立ち上げるアプリの名前を変える場合、`create-react-app react-sample`の名前と、
`docker-compose.yml`の`command: sh -c "cd react-sample && yarn start"`をそれぞれ変更する。

### React + TypeScript
TypeScript環境が作成したい場合は、`--typescript`オプションをつけた下記コマンドを実行する
```
docker-compose run --rm node sh -c "npm install -g create-react-app && create-react-app react-sample --typescript"
```

インストール環境によっては、時間のかかりすぎでyarnの実行中に失敗することがある。
```
yarn add v1.22.4
[1/4] Resolving packages...
[2/4] Fetching packages...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
info There appears to be trouble with your network connection. Retrying...
error An unexpected error occurred: "https://registry.yarnpkg.com/rxjs/-/rxjs-6.5.4.tgz: ESOCKETTIMEDOUT".
info If you think this is a bug, please open a bug report with the information provided in "/usr/src/app/react-sample/yarn-error.log".
info Visit https://yarnpkg.com/en/docs/cli/add for documentation about this command.
```

その場合は、`.yarnrc`を作成し以下のように記載する。
単位はミリ秒なので、下記の場合は10分である。
```
network-timeout 600000
```



## コンテナの起動、reactサーバーの立ち上げ
```
docker-compose up -d
```

## ブラウザ上での確認
`http://localhost:3000/` へアクセスする。
