"""ゲームの資料を docs/source/chNN/ に写す・ゲーム側の変更を確かめる。

使い方（プロジェクトのフォルダで）:
  python -I .claude/skills/source-sync/snap.py copy  docs/source/ch01   … manifest.tsv のとおりに写す
  python -I .claude/skills/source-sync/snap.py check docs/source/ch01   … 写した版から、ゲーム側の元ファイルが変わったかを見る

manifest.tsv（タブ区切り。# で始まる行は飛ばす）:
  出力ファイル名  元ファイル（〈ゲーム〉\\docs からの相対、/ 区切り）  題  範囲
  範囲は「1-363」「67-99,219-305」「1-」（最後まで）
"""
import getpass
import pathlib
import re
import subprocess
import sys
from datetime import date

# PCごとの〈ゲーム〉の場所（CLAUDE.md の「PCごとのフォルダの場所」と合わせる）
GAME_DIRS = {
    "Admin": r"C:\Users\Admin\Desktop\地域制圧ゲーム",
    "hayakawa.masayoshi": r"C:\Users\hayakawa.masayoshi\Desktop\AI\地域",
}

HEAD_RE = re.compile(r"^> 写し元: `〈ゲーム〉\\docs\\(.+?)` の .+?（ゲームのコミット ([0-9a-f]+)、")


def game_dir() -> pathlib.Path:
    user = getpass.getuser()
    for key, path in GAME_DIRS.items():
        if key.lower() == user.lower() and pathlib.Path(path).is_dir():
            return pathlib.Path(path)
    for path in GAME_DIRS.values():
        if pathlib.Path(path).is_dir():
            return pathlib.Path(path)
    sys.exit("〈ゲーム〉のフォルダが見つからない。snap.py の GAME_DIRS と CLAUDE.md に、このPCの場所を足す")


def git(game: pathlib.Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(game), *args], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


def read_manifest(folder: pathlib.Path):
    rows = []
    for line in (folder / "manifest.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        out, src, title, ranges = line.split("\t")
        rows.append((out, src, title, ranges))
    return rows


def parse_ranges(text: str, n: int):
    result = []
    for part in text.split(","):
        a, _, b = part.partition("-")
        result.append((int(a), int(b) if b else n))
    return result


def copy(folder: pathlib.Path):
    game = game_dir()
    commit = git(game, "rev-parse", "--short", "HEAD").strip()
    dirty = git(game, "status", "--porcelain", "--", "docs").strip()
    if dirty:
        print("注意: ゲーム側の docs にコミットしていない変更がある。写しはコミット "
              f"{commit} の版と食い違うかもしれない:\n{dirty}\n")
    for out, src, title, ranges in read_manifest(folder):
        lines = (game / "docs" / src).read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        parts, labels = [], []
        for a, b in parse_ranges(ranges, len(lines)):
            labels.append(f"{a}〜{b}")
            parts.append("\n".join(lines[a - 1:b]).rstrip("\n"))
        disp = src.replace("/", "\\")
        head = (
            f"# 写し: {title}\n\n"
            f"> 写し元: `〈ゲーム〉\\docs\\{disp}` の {'・'.join(labels)}行"
            f"（ゲームのコミット {commit}、{date.today().isoformat()} に写した）。\n"
            "> 直さない。小説で変えることは docs/ のナレッジベースと plot_plans.md に書く。\n\n---\n\n"
        )
        (folder / out).write_text(head + "\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
        print(f"{out}\t{disp}\t{'・'.join(labels)}")
    print(f"\nゲームのコミット: {commit}")


def check(folder: pathlib.Path):
    game = game_dir()
    head = git(game, "rev-parse", "--short", "HEAD").strip()
    print(f"ゲームの今のコミット: {head}")
    seen = set()
    for out, src, _title, _ranges in read_manifest(folder):
        first = (folder / out).read_text(encoding="utf-8").splitlines()[2]
        m = HEAD_RE.match(first)
        if not m:
            print(f"{out}: 頭書きが読めない")
            continue
        commit = m.group(2)
        key = (src, commit)
        if key in seen:
            continue
        seen.add(key)
        stat = git(game, "diff", "--stat", commit, "--", f"docs/{src}").strip()
        dirty = git(game, "status", "--porcelain", "--", f"docs/{src}").strip()
        if not stat and not dirty:
            print(f"変わっていない\t{src}\t（写した版 {commit}）")
        else:
            print(f"変わった\t{src}\t（写した版 {commit}）{' ／コミット前の変更あり' if dirty else ''}")
            if stat:
                print("  " + stat.splitlines()[-1])
    print("\n中身の差は: git -C 〈ゲーム〉 diff <写した版> -- docs/<元ファイル>")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3 or sys.argv[1] not in ("copy", "check"):
        sys.exit(__doc__)
    {"copy": copy, "check": check}[sys.argv[1]](pathlib.Path(sys.argv[2]))
