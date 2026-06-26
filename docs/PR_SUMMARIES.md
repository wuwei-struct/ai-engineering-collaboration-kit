# PR_SUMMARIES

## v0.1.16 - README Story and Visual Flow

- 目标：增强 README 的第一印象表达，让用户快速理解"我也遇到过这些问题"。
- 更新：新增痛点共鸣区、Vibe Coding vs AI Engineering Collaboration 对比表、核心闭环 Mermaid 流程图。
- 核心价值：README 不再只是文件和规范说明，而是先讲清楚 AI 编程为什么会乱，以及本 Kit 如何通过任务合同、上下文路由、门禁、报告和回写形成工程协作闭环。

## v0.1.15 - README Structure Sync

- 目标：同步 README 中过期的"本仓库结构"区块。
- 更新：README 仓库结构改为核心结构概览，体现 docs/12、ContextPack 分层、Task Intake、CommandPack、Task Contract Library 和 templates/context。
- 核心规则：README 只展示核心结构，完整文件清单以 `MANIFEST.md` 为准，避免 README 成为高维护成本的全量清单。

## v0.1.14 - CommandPack Generation Layer

- 目标：新增任务合同生成层与执行合同库机制，解决普通用户不知道工程路径、不能直接写完整 CommandPack 的问题。
- 新增：`docs/12-commandpack-generation-layer.zh-CN.md`
- 新增模板：`templates/TASK_CONTRACT_LIBRARY.md.template`
- 更新：Task Intake、CommandPack 模板、CommandPack 生成指南、非程序员流程、文件角色矩阵、工程概念基础、README、QUICK_START、USAGE。
- 核心规则：普通用户只提供任务意图；规划层根据上下文生成 CommandPack；合同进入执行合同库；只有 active 合同可以执行；执行 Agent 必须验证推断路径。

## v0.1.13 - Split ContextPack Layers

- 日期：2026-06-26
- 目标：将 ContextPack 从单文件 L1/L2/L3 结构升级为入口索引 + 分层文件结构。
- 新增：`docs/context/CONTEXT_PACK_L2.md`、`docs/context/CONTEXT_PACK_L3.md`。
- 新增模板：`templates/context/CONTEXT_PACK_L2.md.template`、`templates/context/CONTEXT_PACK_L3.md.template`。
- 更新：`docs/CONTEXT_PACK.md`、ContextPack 生命周期文档、CommandPack 生成指南、文件角色矩阵、README、QUICK_START、USAGE。
- 核心规则：普通任务读 L1，中等任务读 L1+L2，高风险/审计任务读 L1+L2+L3。
- 执行门禁：`python scripts/check_utf8.py .`、`python scripts/validate_project_structure.py .`
- 风险：仅拆分文档结构，未修改 Skill、模板逻辑、脚本、示例。
- 回滚方式：`git revert` 到 v0.1.12。

## v0.1.12 - Generalized Engineering Concepts

- 日期：2026-06-26
- 目标：将工程概念基础文档从偏 Electron/Web 的具体概念重构为跨项目通用的软件工程概念地图。
- 变更：重构第 5 节为"软件结构与通信概念"，新增契约与兼容性、错误处理与稳定性、可观测性等通用概念。
- 调整：IPC、component、view、store 降级为具体实现例子，不再作为所有项目的一级通用概念。
- 价值：让文档更适用于 Web、Electron、CLI、后端服务、小程序、插件、脚本工具和 AI 应用等多种项目类型。
- 执行门禁：`python scripts/check_utf8.py .`、`python scripts/validate_project_structure.py .`
- 风险：仅重构文档结构和概念层级，未修改 Skill、模板、脚本、示例。
- 回滚方式：`git revert` 到 v0.1.11。

## v0.1.11 - Engineering Concepts Foundation

- 日期：2026-06-26
- 目标：新增 AI 编程工程概念基础模块，帮助普通用户理解 CommandPack 和工程风险词汇。
- 新增：`docs/11-engineering-concepts-foundation.zh-CN.md`
- 更新：README、QUICK_START、SELF_DIAGNOSIS、docs/10、docs/07、MANIFEST、CHANGELOG
- 核心价值：让用户知道哪些概念是低风险，哪些概念涉及权限、计费、schema、生产配置、密钥和用户数据等高风险区域。
- 执行门禁：`python scripts/check_utf8.py .`、`python scripts/validate_project_structure.py .`
- 风险：仅新增文档模块和入口引用，未修改 Skill、模板、脚本、示例。
- 回滚方式：`git revert` 到 v0.1.10。

---

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
