#!/usr/bin/env python3
"""
check_utf8.py

检查项目中的文本文件是否可按 UTF-8 读取，并尝试识别常见 mojibake / 乱码风险。

用法：
  python scripts/check_utf8.py .
  python scripts/check_utf8.py path/to/file_or_dir

说明：
- 该脚本不修改文件。
- 默认跳过 node_modules、dist、build、.git 等目录。
- 主要用于 Markdown / JSON / JS / TS / HTML / CSS / Python / 文档类文件。
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".txt",
    ".json", ".jsonc",
    ".js", ".jsx", ".ts", ".tsx",
    ".html", ".css", ".scss",
    ".py", ".yml", ".yaml",
    ".toml", ".ini", ".cfg",
    ".xml", ".svg",
    ".csv",
}

SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", "coverage", ".cache",
    ".next", ".vite", ".turbo", "__pycache__", ".pytest_cache",
}

# Keep these as escaped literals so this checker does not flag its own source.
SUSPICIOUS_PATTERNS = [
    "\ufffd",                # replacement character
    "\u00c3", "\u00c2",      # common mojibake markers
    "\u00e4\u00b8",          # common Chinese UTF-8 decoded as latin1 fragment
    "\u00e6", "\u00e5", "\u00e7", "\u00e8",
    "\u9286", "\u4f77", "\u6d93", "\u934f",  # common GBK/UTF-8 mojibake fragments
]


def is_text_candidate(path: Path) -> bool:
    if path.name in {".editorconfig", ".gitattributes", ".gitignore"}:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS


def iter_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return

    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        base = Path(current_root)
        for filename in files:
            path = base / filename
            if is_text_candidate(path):
                yield path


def check_file(path: Path) -> list[str]:
    issues: list[str] = []

    try:
        data = path.read_bytes()
    except OSError as exc:
        return [f"读取失败：{exc}"]

    if not data:
        return issues

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"无法按 UTF-8 解码：{exc}"]

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in text:
            issues.append(f"疑似乱码 / mojibake 标记：{pattern!r}")
            break

    if "\x00" in text:
        issues.append("发现 NUL 字符，可能不是文本文件或已损坏")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="检查 UTF-8 和疑似乱码。")
    parser.add_argument("paths", nargs="*", default=["."], help="要检查的文件或目录")
    args = parser.parse_args()

    all_issues: list[tuple[Path, list[str]]] = []

    for raw in args.paths:
        root = Path(raw)
        if not root.exists():
            all_issues.append((root, ["路径不存在"]))
            continue

        for path in iter_files(root):
            issues = check_file(path)
            if issues:
                all_issues.append((path, issues))

    if all_issues:
        print("UTF-8 / 乱码检查发现问题：", file=sys.stderr)
        for path, issues in all_issues:
            print(f"\n- {path}", file=sys.stderr)
            for issue in issues:
                print(f"  - {issue}", file=sys.stderr)
        return 1

    print("UTF-8 / 乱码检查通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
