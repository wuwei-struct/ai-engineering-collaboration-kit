#!/usr/bin/env python3
"""
init_project_skeleton.py

将 AI 工程协作文档模板复制到目标项目中。

用法：
  python scripts/init_project_skeleton.py /path/to/project

默认不覆盖已有文件。
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

TEMPLATE_MAP = {
    "templates/AGENTS.md.template": "AGENTS.md",
    "templates/CONTEXT_PACK.md.template": "docs/CONTEXT_PACK.md",
    "templates/MODULE_BOUNDARY.md.template": "docs/MODULE_BOUNDARY.md",
    "templates/TESTING.md.template": "docs/TESTING.md",
    "templates/PR_SUMMARIES.md.template": "docs/PR_SUMMARIES.md",
    "templates/PRODUCT_BRIEF.md.template": "docs/PRODUCT_BRIEF.md",
    "templates/PRODUCT_ARCHITECTURE.md.template": "docs/PRODUCT_ARCHITECTURE.md",
    "templates/DEV_GUIDE.md.template": "docs/DEV_GUIDE.md",
    "templates/NEXT_PHASE_PLAN.md.template": "docs/NEXT_PHASE_PLAN.md",
    "templates/.editorconfig.template": ".editorconfig",
    "templates/.gitattributes.template": ".gitattributes",
    "templates/.gitignore.template": ".gitignore",
    "scripts/check_utf8.py": "scripts/check_utf8.py",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--force", action="store_true", help="覆盖已有文件")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    target = Path(args.project).resolve()
    target.mkdir(parents=True, exist_ok=True)

    copied = []
    skipped = []
    missing = []

    for src_rel, dst_rel in TEMPLATE_MAP.items():
        src = repo / src_rel
        dst = target / dst_rel

        if not src.exists():
            missing.append(src_rel)
            continue

        if dst.exists() and not args.force:
            skipped.append(dst_rel)
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        copied.append(dst_rel)

    print("复制完成。")

    if copied:
        print("\n已复制：")
        for item in copied:
            print(f"- {item}")

    if skipped:
        print("\n已跳过（已存在，使用 --force 可覆盖）：")
        for item in skipped:
            print(f"- {item}")

    if missing:
        print("\n模板缺失：")
        for item in missing:
            print(f"- {item}")

    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
