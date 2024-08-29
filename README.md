# FastAPI_sample

## 実行コマンド
```
poetry install

# API立ち上げ
poetry run uvicorn app.main:app --reload

# test実行
poetry run pytest
```

## API呼び出し・ドキュメント
- http://127.0.0.1:8000/ にアクセス->デフォルトのGETメソッド呼び出し結果が出力
- http://127.0.0.1:8000/docs にアクセス->APIドキュメントが表示
- APIドキュメントの各メソッド内を開いたところにある「Try it out」でテストデータを入力して「Execute」によりAPI呼び出しが可能
- 呼び出す際のcurlコマンドも表示される

