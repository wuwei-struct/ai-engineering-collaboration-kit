# Changelog

## v0.1.5 - Release Close and Runtime Finalization

### Changed
- Finalized the runtime model: daily AI execution requires only `CommandPack + SKILL.md`.
- Reframed `.ai_rules.md`, `AGENTS.md`, ContextPack, module boundary docs, and testing docs as optional project context.
- Clarified that full execution specs are for human maintenance, audit, teaching, review, and spec evolution, not daily AI runtime.
- High-risk, unclear, or rule-conflict scenarios: AI must STOP and request clearer CommandPack, authorization scope, acceptance criteria, and rollback requirements.
- Updated README, USAGE, QUICK_START, tool integration guide, Skill, Runtime summary, CommandPack template, and AI rules template to match the final runtime model.

### Release
- Prepared the repository for the first public GitHub release.

## v0.1.4 - Runtime Simplification

### Changed
- Simplified the runtime model: daily AI tasks now require only `CommandPack + SKILL.md`.
- Reframed `.ai_rules.md`, `AGENTS.md`, and ContextPack as optional project context files instead of mandatory default reads.
- Clarified that the full execution spec is for human maintenance, audit, and complex rule conflicts, not daily AI execution.
- Updated README, USAGE, QUICK_START, tool integration guide (`docs/00`, `docs/03`), CommandPack template, AI rules template, SKILL.md, SKILL_RUNTIME.md, and MANIFEST to match the simplified runtime model.

## v0.1.3 - Router Skill Architecture

### Added

- Added `skills/codex-ide-executor-zh/references/FULL_EXECUTION_SPEC.zh-CN.md` as a full execution spec reference for standalone Skill export.

### Changed

- Refactored `skills/codex-ide-executor-zh/SKILL.md` into a lightweight router Skill (~330 lines from ~1700 lines).
- Merged duplicated full-spec content into `docs/02-agent-execution-spec.zh-CN.md` as the canonical human-readable spec.
- Clarified the four-layer rule architecture: router Skill, runtime summary, project rules, full spec.
- Updated `SKILL_RUNTIME.md` references to point to new full spec locations.
- Updated README, USAGE, QUICK_START, docs/00, docs/03, MANIFEST with new file roles.

## v0.1.2 - 2026-06-17

### Added

- Added `USAGE.md` to explain how users should apply the three-layer rule model.
- Added `docs/00-how-to-use-with-ai-agent.zh-CN.md` with detailed Claude / Codex / Cursor usage guidance.

### Changed

- Updated README and QUICK_START to clarify that daily tasks should use `.ai_rules.md` + CommandPack instead of reading the full Skill every time.
- Updated tool integration guide with `.ai_rules.md` and `SKILL_RUNTIME.md` references for Claude, Codex, Cursor usage.

## v0.1.1 - 2026-06-17

### Added

- Added `SKILL_RUNTIME.md` as a lightweight runtime summary for daily AI coding tasks.
- Added `templates/AI_RULES.md.template` for project-level `.ai_rules.md`.

### Changed

- Documented the three-layer rule model: full spec, runtime rules, CommandPack.
- Updated quick start and CommandPack template to avoid requiring full Skill reads for every task.

## v0.1.0 - 2026-06-17

首个开源仓库包版本。

包含：

- 顶层 README。
- SELF_DIAGNOSIS 自诊清单。
- QUICK_START 快速开始。
- AI 编程项目协作手册 v1.0。
- Codex/IDE 执行规范 Skill v1.2。
- 工具集成指南。
- FAQ。
- 案例分析指南。
- 发布前检查清单。
- Codex/IDE Skill 包。
- AGENTS / CommandPack / ContextPack / ModuleBoundary / Testing 等模板。
- UTF-8 检查脚本。
- 项目结构验证脚本。
- 项目骨架初始化脚本。
- 三个示例项目骨架。

## Roadmap

### v0.2

- 增加更多真实案例。
- 增加 GitHub Actions 示例。
- 增加 pre-commit 示例。
- 增加英文 README。

### v0.3

- 增加英文核心文档。
- 增加更多技术栈模板。
- 增加案例 before/after 对比。

### v1.0

- 中英双语文档成熟。
- 案例覆盖 CLI / Electron / Web / 后端 / 文档项目。
- 脚本稳定。
- 工具集成说明完善。
