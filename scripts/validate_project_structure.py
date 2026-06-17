#!/usr/bin/env python3
"""
validate_project_structure.py

验证目标项目是否具备 AI 工程协作最小结构。

用法：
  python scripts/validate_project_structure.py path/to/project
"""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "docs/CONTEXT_PACK.md",
    "docs/MODULE_BOUNDARY.md",
    "docs/TESTING.md",
    "docs/PR_SUMMARIES.md",
    "scripts/check_utf8.py",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
]

RECOMMENDED = [
    "docs/PRODUCT_BRIEF.md",
    "docs/PRODUCT_ARCHITECTURE.md",
    "docs/DEV_GUIDE.md",
    "docs/NEXT_PHASE_PLAN.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.project).resolve()
    missing_required = [p for p in REQUIRED if not (root / p).exists()]
    missing_recommended = [p for p in RECOMMENDED if not (root / p).exists()]

    print(f"检查项目：{root}")

    if missing_required:
        print("\n缺少必需文件：")
        for p in missing_required:
            print(f"- {p}")
    else:
        print("\n必需文件齐全。")

    if missing_recommended:
        print("\n建议补充文件：")
        for p in missing_recommended:
            print(f"- {p}")
    else:
        print("\n建议文件齐全。")

    return 1 if missing_required else 0


if __name__ == "__main__":
    raise SystemExit(main())
