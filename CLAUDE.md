# プロジェクト概要

このプロジェクトは、ゲーム「無人都市トウキョウ―AFTER 7:12―」（`C:\Users\Admin\Desktop\地域制圧ゲーム`）を小説にするためのもの。
書き方の形は、小説「現代ダンジョン奮闘記」（`C:\Users\Admin\Desktop\現代ダンジョン奮闘記`）と同じにする。

## 小説の決まり

- **本編は天城 閃の一人称「俺」**で書く
- **閑話**は視点を自由にしてよい（ほかの勢力のキャラの視点、7:12〈大人が消えた朝〉より前の話など）
- **1章（学校統一）から**書く
- **ゲームの数値は出さない**。兵の数・HP・必殺技の回数・倍率・ターンなどは本文に書かず、描写だけで見せる（人数は「30人ほど」のように、物語の中の人数として書いてよい）
- 1話の目安は2,000〜3,000文字（盛り上がる話は5,000文字ほどまで）

## ゲームとの関係

- ゲームの資料は**元ネタ**。小説の正は、このプロジェクトの `docs/` と確定した本文
- 小説で筋を変えたり、設定を足したりしてよい。ゲームの分岐（勝ち負け・選択肢・ルート）は、`docs/plot_plans.md` で1本に決める
- 新しい章を書き始めるときは、ゲームの資料から、その章の分だけナレッジベースに写す（下の「元ネタの場所」）
- 小説で決めたことを、ゲームの資料に勝手に書き戻さない

### 元ネタの場所（ゲーム側。読むだけ）

| 何 | ファイル |
|---|---|
| 物語の文（全章） | `地域制圧ゲーム\docs\data\story-list.md` |
| 世界・ルールの決まり | `地域制圧ゲーム\docs\spec\concept.md` |
| 章ごとの流れ | `地域制圧ゲーム\docs\spec\chapter1-design.md`・`chapter2-design.md`・`chapter3-design.md` |
| キャラ | `地域制圧ゲーム\docs\data\characters.md`・`characters\`、`docs\prompts\characters\character-visuals.md`・`chapter3-visuals.md` |
| 話し方 | `地域制圧ゲーム\docs\story\style\voices.md` |
| 3章の勢力と真相 | `地域制圧ゲーム\docs\story\briefs\chapter3-story-brief.md`・`chapter3-main-story-brief.md` |

## ファイル構成

- `001.txt` 〜 — 本編各話
- `閑話001.txt` 〜 — 閑話（番外編）

### docs/ — 設定・ナレッジベース

| ファイル | 用途 |
|---|---|
| `docs/story_knowledge_base.md` | 確定した本文のあらすじ・話数索引 |
| `docs/characters_knowledge_base.md` | キャラクター設定（見た目・性格・話し方・呼び方） |
| `docs/world_knowledge_base.md` | 世界観・状況の決まり |
| `docs/skills_knowledge_base.md` | 必殺技・合体技（見た目・使い方。数値は書かない） |
| `docs/map_location_notes.md` | 場所（校舎・墨田区・23区） |
| `docs/plot_plans.md` | まだ書いていない先の展開の案（章ごと・話数ごと） |
| `docs/title.md` | 各話タイトルと品質評価スコア表 |

**文体・NG表現のルールは、奮闘記のものを使う**（このプロジェクトには置かない）:
- `C:\Users\Admin\Desktop\現代ダンジョン奮闘記\docs\prose_style.md` — 文体・構成の方針
- `C:\Users\Admin\Desktop\現代ダンジョン奮闘記\docs\ng_expressions.md` — NG表現リスト

## 利用可能なスキル（.claude/skills/）

- `chapter-polish` — 下書き原稿を設定・NG表現と照合しながら校正
- `chapter-score` — 確定済み原稿を5軸で品質評価
- `kb-sync` — 確定した本編・閑話の内容をナレッジベースに反映
- `git-sync` — 変更をコミット（リモートを設定したら push も）

## 作業ルール

- やりとりはすべて**日本語**で行う
- 回答は**簡潔**にする
- 小説の文体・世界観・キャラクター設定に一貫性を保つ
- **すべての作業において、まず `docs/` フォルダ内のナレッジベースを参照すること**
- キャラクターの言動は必ずナレッジベースと照合し、設定と矛盾しないようにする
- 新しい設定を追加・変更した場合は、対応するナレッジベースの更新を提案する（`kb-sync`スキルを利用可能）
