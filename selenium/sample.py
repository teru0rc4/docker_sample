# -*- Coding: UTF-8 -*-
from selenium import webdriver

options = webdriver.ChromeOptions()
# headlessオプションをつけると、ブラウザの実際の動作を確認できなくなる
# options.add_argument('--headless')

# Seleniumサーバー(4444ポート)に接続
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

# ブラウザを操作、URLにアクセス
driver.get('https://qiita.com')

# 画面キャプチャを取得
driver.save_screenshot('screenshot.png')

# アクセスしているURLを出力
print(driver.current_url)

# ブラウザを終了する
driver.quit()