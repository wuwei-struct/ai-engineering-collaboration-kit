# PR_SUMMARIES

## PR-002：v0.1.10 - Controlled Opportunistic Fixes

- 日期：2026-06-22
- 目标：优化受控小修机制，避免规则过硬导致低风险小问题无法处理。
- 新增：前置修复白名单、同因同类小修复、必须 STOP 黑名单。
- 更新：SKILL、Runtime、完整规范、CommandPack 模板、AI_RULES 模板、README、USAGE、QUICK_START、MANIFEST、CHANGELOG。
- 核心口径：低风险、同因、局部、可验证的问题可以处理；涉及密钥、生产配置、schema、权限、license、计费、用户数据等必须 STOP。
- 执行门禁：python scripts/check_utf8.py .、python scripts/validate_project_structure.py .
- 风险：仅优化规范和模板，未改底层执行逻辑和门禁。
- 回滚方式：git revert 到 v0.1.9。

---

## PR-001：v0.1.9 - Lightweight Entry and File Role Matrix

- 日期：2026-06-21
- 目标：降低开源项目入口复杂度，明确不同用户和不同项目阶段需要哪些文件。
- 新增：`docs/10-file-roles-and-usage-modes.zh-CN.md`
- 更新：README、QUICK_START、USAGE、SELF_DIAGNOSIS、docs/00、docs/07、docs/08、docs/09
- 核心口径：最小模式只需要 `SKILL.md + CommandPack`；项目复杂后再逐步补充 AGENTS、ContextPack、Testing、ModuleBoundary 等文档。
- 执行门禁：python scripts/check_utf8.py .、python scripts/validate_project_structure.py .
- 风险：仅文档入口减重，未改底层执行规则和 Skill。
- 回滚方式：git revert 到 v0.1.8。

---

## PR-000：创建 AI 工程协作规范套件开源包

- 日期：2026-06-17
- 目标：生成首个可开源仓库包。
- 修改文件：README、SELF_DIAGNOSIS、QUICK_START、docs、skills、templates、scripts、examples、license。
- 执行门禁：python scripts/check_utf8.py .
- 风险：许可证文本为简明声明版本，正式发布前可按需核对。
- 回滚方式：删除本仓库目录或恢复到上一版本。
- 下一步：上传 GitHub 前做一次人工审查。
