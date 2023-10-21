# voicevox_fat_resource

VOICEVOX 用のリソースファイルのうちファイル容量が特に大きいもの置き場

## 音声モデル(.vvm)追加の流れ

1. `core/model` に `.vvm` ファイルを追加
1. キャラクターが増えた場合は README に利用規約情報を追記
1. `scripts/make_docs_core_voice.py`を実行して対応表を更新
