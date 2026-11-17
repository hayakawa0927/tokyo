# プロジェクト概要

このプロジェクトは、ゲーム「無人都市トウキョウ―AFTER 7:12―」（下の表の〈ゲーム〉）を小説にするためのもの。
書き方の形は、小説「現代ダンジョン奮闘記」（下の表の〈奮闘記〉）と同じにする。

### PCごとのフォルダの場所

| PC | 〈ゲーム〉 | 〈奮闘記〉 |
|---|---|---|
| 別のPC（Admin） | `C:\Users\Admin\Desktop\地域制圧ゲーム` | `C:\Users\Admin\Desktop\現代ダンジョン奮闘記` |
| hayakawa.masayoshi のPC | `C:\Users\hayakawa.masayoshi\Desktop\AI\地域` | `C:\Users\hayakawa.masayoshi\Desktop\AI\現代` |

- 今のPCのユーザー名を見て、合う行の場所を使う

## 小説の決まり

- **本編は天城 閃の一人称「俺」**で書く
- **閑話**は視点を自由にしてよい（ほかの勢力のキャラの視点、7:12〈大人が消えた朝〉より前の話など）
- **1章（学校統一）から**書く
- **ゲームの数値は出さない**。兵の数・HP・必殺技の回数・倍率・ターンなどは本文に書かず、描写だけで見せる（人数は「30人ほど」のように、物語の中の人数として書いてよい）
- 1話の目安は2,000〜3,000文字（盛り上がる話は5,000文字ほどまで）
- 全体は**100話ほど、20万〜40万文字**。プロローグ2〜3話・1章5話ほど・2章10〜20話・3章が残り（`docs/plot_plans.md` の「全体の骨子」）。どれも目安で、増えても減ってもよい（全体で80話でも200話でもよい）。本編のファイルの番号は、プロローグから通しで `001.txt` から付ける

## ゲームとの関係

- ゲームの資料は**元ネタ**。小説の正は、このプロジェクトの `docs/` と確定した本文
- 小説で筋を変えたり、設定を足したりしてよい。ゲームの分岐（勝ち負け・選択肢・ルート）は、`docs/plot_plans.md` で1本に決める
- 新しい章を書き始めるときは、`source-sync` スキルで、ゲームの資料からその章の分だけを `docs/source/` に写し、ナレッジベースに足す
- 小説で決めたことを、ゲームの資料に勝手に書き戻さない

### 〈ゲーム〉〈奮闘記〉を見てよい作業

- **本文を書く・直す・採点する・KBを直す作業では、〈ゲーム〉〈奮闘記〉のフォルダを見ない。** 見るのは `docs/`（`docs/source/` の写しを含む）と、このプロジェクトの本文だけ
- 例外は次の2つだけ
  - `source-sync` スキル（ゲームの資料を写す・ゲーム側の変更を確かめる）
  - `chapter-score` スキルの基準の2話（〈奮闘記〉の135話・9話）
- 写しにないことが要るときは、ゲームを直接見にいかず、`source-sync` で写しを足す

### 元ネタの写し（`docs/source/`）

- `docs/source/chNN/` に、章ごとのゲームの資料を**そのまま**写す。写しは直さない（小説で変えることは、ナレッジベースと `plot_plans.md` に書く）
- どのファイルの、どの範囲を、ゲームのどのコミットから写したかは `docs/source/import_log.md` に書く
- 写しにはゲームの数値も残っている。本文に数値を出さないのは、写しではなく本文の決まり

### 元ネタの場所（ゲーム側。`source-sync` だけが読む）

| 何 | ファイル |
|---|---|
| 物語の文（全章） | `〈ゲーム〉\docs\data\story-list.md` |
| 世界・ルールの決まり | `〈ゲーム〉\docs\spec\concept.md` |
| 章ごとの流れ | `〈ゲーム〉\docs\spec\chapter1-design.md`・`chapter2-design.md`・`chapter3-design.md` |
| キャラ | `〈ゲーム〉\docs\data\characters.md`・`characters\`、`docs\prompts\characters\character-visuals.md`・`chapter3-visuals.md` |
| 話し方 | `〈ゲーム〉\docs\story\style\voices.md` |
| 3章の勢力と真相 | `〈ゲーム〉\docs\story\briefs\chapter3-story-brief.md`・`chapter3-main-story-brief.md` |
| 必殺技の中身 | `〈ゲーム〉\docs\data\chapter1-units.md`・`chapter2-units.md`・`chapter3-skills.md` |
| 必殺技の見た目 | `〈ゲーム〉\docs\prompts\skill-fx\*.md`（`docs\data\skill-fx.md` は画像の秒数の表だけなので使わない） |
| 場所 | `〈ゲーム〉\docs\data\places.md`、`docs\spec\ui-design.md`（マップ） |
| 文体（ゲームの文の書き方） | `〈ゲーム〉\docs\story\style\prose-style.md`・`ng-expressions.md`（奮闘記のルールをもとに作者がゲーム用に直したもの。小説の文体の正は、このプロジェクトの `prose_style.md`） |

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
| `docs/prose_style.md` | 文体・構成の方針 |
| `docs/ng_expressions.md` | NG表現リスト |
| `docs/source/` | 元ネタ（ゲームの資料）の写し。章ごと。直さない |
| `docs/source/import_log.md` | 写した記録（ファイル・範囲・ゲームのコミット） |

- `prose_style.md`・`ng_expressions.md` は、奮闘記のものを写して始め、この世界に合わせて直した。ゲームの文体ルールのうち小説にも使える項目も取り込んである（「ゲームの文体ルールから」と書いた項目）。更新するときは、このプロジェクトのファイルだけを直す（奮闘記・ゲームのファイルは直さない）

## 利用可能なスキル（.claude/skills/）

- `chapter-polish` — 下書き原稿を設定・NG表現と照合しながら校正
- `chapter-score` — 確定済み原稿を5軸で品質評価
- `kb-sync` — 確定した本編・閑話の内容をナレッジベースに反映
- `git-sync` — 変更をコミット（リモートを設定したら push も）
- `source-sync` — ゲームの資料を章の分だけ `docs/source/` に写し、KBに足す。ゲーム側の変更を確かめる（このプロジェクトだけのスキル）
- `chapter-draft` — plot_plans の案と写し・KB・文体ルールから、1話の下書きを書く（このプロジェクトだけのスキル）

- 書く流れ: `chapter-draft`（下書き）→ `chapter-polish`（校正）→ 確定 → `kb-sync`（KBに反映）→ `chapter-score`（採点）

- `chapter-polish`・`chapter-score`・`kb-sync`・`git-sync` の4つは、奮闘記のものを写して、この小説に合わせて書き換えた。更新するときは、このプロジェクトのファイルだけを直す（奮闘記のスキルは直さない。奮闘記のスキルが直されても、こちらには自動で写さない）

## 作業ルール

- やりとりはすべて**日本語**で行う
- 回答は**簡潔**にする
- 小説の文体・世界観・キャラクター設定に一貫性を保つ
- **すべての作業において、まず `docs/` フォルダ内のナレッジベースを参照すること**
- キャラクターの言動は必ずナレッジベースと照合し、設定と矛盾しないようにする
- 新しい設定を追加・変更した場合は、対応するナレッジベースの更新を提案する（`kb-sync`スキルを利用可能）
