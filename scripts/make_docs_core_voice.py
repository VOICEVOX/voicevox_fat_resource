# コアの音声モデル（vvm）内に含まれる声（キャラクター＋スタイル）の一覧ドキュメントを更新する

import json
import zipfile
from pathlib import Path
import re

dir_path = Path("core/model")
vvm_files = sorted(dir_path.glob("*.vvm"), key=lambda x: int(x.stem))

assert len(vvm_files) > 0, "コアの音声モデルが見つかりませんでした。"

output_text = "| vvmファイル名 | 話者名 | スタイル名 | スタイルID |\n"
output_text += "|--------------|------|---------|---------|\n"

# vvmファイル内のmetas.jsonを読み込み、必要な情報をテキストに追加
for vvm_file in vvm_files:
    with zipfile.ZipFile(vvm_file, "r") as zipf:
        with zipf.open("metas.json") as f:
            data = json.load(f)
            for entry in data:
                speaker_name = entry["name"]
                for style in entry["styles"]:
                    style_name = style["name"]
                    style_id = style["id"]
                    output_text += f"| {vvm_file.name} | {speaker_name} | {style_name} | {style_id} |\n"

# README.mdファイルを更新
readme_path = dir_path / "README.md"
with readme_path.open("r", encoding="utf-8") as f:
    content = f.read()

# テーブルの内容を置換
match = re.search(
    r"(?<=# 音声モデル\(.vvm\)ファイルと声（キャラクター・スタイル名）とスタイル ID の対応表\n\n).*?(?=\n---)",
    content,
    flags=re.DOTALL,
)
if match:
    updated_content = content[: match.start()] + output_text + content[match.end() :]
    with readme_path.open("w", encoding="utf-8") as f:
        f.write(updated_content)
    print("README.md has been updated!")
else:
    raise ValueError("対象範囲がREADME.mdに見つかりませんでした。")
