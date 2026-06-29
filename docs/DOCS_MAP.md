# DOCS_MAP / 文档地图

> 本文件用于说明仓库中重要文档的位置、用途、阅读时机和更新时机。
>
> 它不是完整文件清单。
> 完整文件清单以 `MANIFEST.md` 为准。
>
> 它也不是项目上下文本身。
> 项目上下文以 `docs/CONTEXT_PACK.md` 和 `docs/context/` 为准。
>
> DOCS_MAP 的作用是帮助人和 AI 判断：当前任务应该读哪份文档、更新哪份文档。

## 1. 文档类型标签

| 标签 | 含义 | 典型用途 |
|---|---|---|
| ENTRY | 入口文档 | 新用户、新 AI 进入项目时先看 |
| RUNTIME | 运行时文档 | AI 执行任务时可能需要读取 |
| CONTRACT | 任务合同相关 | Task Intake、CommandPack、合同库 |
| CONTEXT | 项目上下文 | 项目状态、模块、阶段、风险 |
| REFERENCE | 参考说明 | 方法说明、概念解释、FAQ |
| HISTORY | 历史记录 | PR 记录、变更历史、版本变化 |
| AUDIT | 审计 / 高风险 | 架构、权限、数据库、发布前审查 |
| TEMPLATE | 模板 | 用于复制或生成项目文件 |

## 2. 如何使用文档地图

### 普通用户

优先阅读：

- `README.md`
- `QUICK_START.md`
- `SELF_DIAGNOSIS.md`

如果不知道某个工程概念，阅读：

- `docs/11-engineering-concepts-foundation.zh-CN.md`

### 规划型 AI / Contract Generator

生成 CommandPack 前，优先检查：

- `docs/DOCS_MAP.md`
- `docs/CONTEXT_PACK.md`
- 必要时读取 L2 / L3 ContextPack
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`

### 执行 Agent

执行任务时，不应盲目读取全部文档。

应根据 CommandPack 指定范围读取：

- Skill / CommandPack
- 必要上下文
- 相关源码和测试

### 审查者 / Reviewer

审查执行结果时，优先读取：

- 当前 CommandPack
- ExecutionReport
- `docs/PR_SUMMARIES.md`
- 必要时读取 ContextPack / TESTING / MODULE_BOUNDARY

## 3. 核心文档地图

| 文档 | 类型 | 主要内容 | 谁会读 | 什么时候读 | 什么时候更新 |
|---|---|---|---|---|---|
| `README.md` | ENTRY | 项目定位、痛点、核心闭环、快速入口 | 所有人 | 第一次了解项目 | 项目定位、入口、结构概览变化时 |
| `QUICK_START.md` | ENTRY | 快速上手步骤 | 新用户 | 想快速试用时 | 使用流程变化时 |
| `SELF_DIAGNOSIS.md` | ENTRY / REFERENCE | 判断自己是否需要本 Kit | 普通用户 | 不确定是否适合时 | 目标用户或使用场景变化时 |
| `USAGE.md` | REFERENCE | 使用方式、常见操作 | 使用者 | 查具体用法时 | 使用流程或命令变化时 |
| `MANIFEST.md` | REFERENCE | 全量文件清单 | 维护者 / AI | 需要确认文件是否存在时 | 新增、删除、重命名文件时 |
| `AGENTS.md` | RUNTIME | 仓库级 AI 协作规则 | AI / 维护者 | 执行任务前或规则冲突时 | 仓库规则变化时 |
| `docs/CONTEXT_PACK.md` | CONTEXT / RUNTIME | L1 最小上下文入口 | AI / 规划者 | 普通任务、首次进入项目 | 项目当前状态、阶段目标、常用命令变化时 |
| `docs/context/CONTEXT_PACK_L2.md` | CONTEXT | 深入协作上下文 | 规划型 AI / SAFE 任务 | 中等复杂任务 | 模块边界、业务规则、阶段计划变化时 |
| `docs/context/CONTEXT_PACK_L3.md` | CONTEXT / AUDIT | 审计、交接、高风险上下文 | 审查者 / AUDIT 任务 | 高风险任务、交接、发布前 | 高风险边界、架构、生产策略变化时 |
| `docs/MODULE_BOUNDARY.md` | CONTEXT / AUDIT | 模块边界、中央文件、职责划分 | AI / 维护者 | 新功能、重构、跨模块任务 | 模块职责、目录结构、中央文件规则变化时 |
| `docs/TESTING.md` | RUNTIME / REFERENCE | 测试、构建、门禁命令 | AI / 维护者 | 生成 CommandPack 或执行门禁时 | 测试命令、构建方式、门禁策略变化时 |
| `docs/PR_SUMMARIES.md` | HISTORY | 重要任务记录 | 维护者 / AI | 查历史、生成下一步计划时 | 每个重要 PR 完成后 |
| `docs/NEXT_PHASE_PLAN.md` | CONTEXT / HISTORY | 下一阶段计划 | 项目负责人 / AI | 规划下一步任务时 | 阶段目标变化时 |
| `docs/PRODUCT_BRIEF.md` | CONTEXT | 产品定位和目标用户 | 规划者 | 任务涉及产品方向时 | 产品定位变化时 |
| `docs/PRODUCT_ARCHITECTURE.md` | CONTEXT / AUDIT | 产品架构与核心模块 | 规划者 / 审查者 | 架构、模块、路线变化时 | 架构决策变化时 |
| `docs/DEV_GUIDE.md` | REFERENCE | 开发说明 | 开发者 / AI | 需要了解开发约定时 | 开发流程变化时 |
| `docs/00-how-to-use-with-ai-agent.zh-CN.md` | ENTRY / RUNTIME | 如何配合 AI Agent 使用本 Kit | AI 用户 | 第一次接入 AI 工具时 | AI 使用流程变化时 |
| `docs/01-ai-project-collaboration-handbook.zh-CN.md` | REFERENCE | AI 项目协作手册 | 人类用户 | 想理解协作方法时 | 协作方法变化时 |
| `docs/02-agent-execution-spec.zh-CN.md` | REFERENCE / AUDIT | 完整执行规范母版 | 维护者 / 审查者 | 维护规则、审计冲突时 | 执行规范变化时 |
| `docs/03-tool-integration-guide.zh-CN.md` | REFERENCE | 工具集成说明 | 工具使用者 | 接入 Codex / Claude / Cursor 等工具时 | 工具适配变化时 |
| `docs/04-faq.zh-CN.md` | REFERENCE | 常见问题 | 普通用户 | 遇到疑问时 | 新问题沉淀时 |
| `docs/05-case-study-guide.zh-CN.md` | REFERENCE | 案例说明 | 使用者 | 想看示例时 | 新案例增加时 |
| `docs/06-release-checklist.zh-CN.md` | AUDIT / REFERENCE | 发布检查清单 | 维护者 | 发布前 | 发布流程变化时 |
| `docs/07-non-programmer-workflow.zh-CN.md` | ENTRY / REFERENCE | 非程序员使用流程 | 普通用户 | 不懂代码但想用 AI 做项目时 | 普通用户流程变化时 |
| `docs/08-commandpack-generation-guide.zh-CN.md` | CONTRACT / REFERENCE | 如何生成 CommandPack | 规划型 AI / 项目负责人 | 生成任务合同时 | 合同生成流程变化时 |
| `docs/09-contextpack-lifecycle.zh-CN.md` | CONTEXT / REFERENCE | ContextPack 生命周期 | 维护者 / AI | 上下文初始化、回写、压缩时 | 上下文机制变化时 |
| `docs/10-file-roles-and-usage-modes.zh-CN.md` | REFERENCE | 文件角色与使用模式 | 新用户 / 维护者 | 不知道文件用途时 | 文件角色变化时 |
| `docs/11-engineering-concepts-foundation.zh-CN.md` | REFERENCE | AI 编程工程概念基础 | 普通用户 / 初学者 | 不理解工程概念时 | 概念体系变化时 |
| `docs/12-commandpack-generation-layer.zh-CN.md` | CONTRACT / REFERENCE | 任务合同生成层与执行合同库 | 规划型 AI / 项目负责人 | 从 Task Intake 生成合同时 | 合同生成层机制变化时 |

## 4. 模板文档地图

| 模板 | 类型 | 主要用途 | 什么时候用 |
|---|---|---|---|
| `templates/TASK_INTAKE.md.template` | TEMPLATE / CONTRACT | 普通用户任务意图表 | 用户不知道如何描述任务时 |
| `templates/CommandPack.md.template` | TEMPLATE / CONTRACT | 执行任务合同模板 | 生成 AI 执行任务合同时 |
| `templates/TASK_CONTRACT_LIBRARY.md.template` | TEMPLATE / CONTRACT | 执行合同库模板 | 管理多个 CommandPack 时 |
| `templates/CONTEXT_PACK.md.template` | TEMPLATE / CONTEXT | L1 ContextPack 模板 | 初始化项目上下文时 |
| `templates/context/CONTEXT_PACK_L2.md.template` | TEMPLATE / CONTEXT | L2 深入上下文模板 | 中长期项目补充协作上下文时 |
| `templates/context/CONTEXT_PACK_L3.md.template` | TEMPLATE / AUDIT | L3 审计上下文模板 | 高风险项目、交接、发布前审计时 |
| `templates/AGENTS.md.template` | TEMPLATE / RUNTIME | 仓库级 AI 协作规则模板 | 初始化项目 AI 规则时 |
| `templates/AI_RULES.md.template` | TEMPLATE / RUNTIME | 压缩 AI 执行规则模板 | 生成 `.ai_rules.md` 时 |
| `templates/MODULE_BOUNDARY.md.template` | TEMPLATE / CONTEXT | 模块边界模板 | 防止中央文件继续膨胀时 |
| `templates/TESTING.md.template` | TEMPLATE / RUNTIME | 测试门禁模板 | 初始化门禁说明时 |

## 5. 文档读取策略

### DOCS_MAP-first 读取策略

当仓库文档较多时，规划层或 AI 不应盲目读取整个 `docs/` 目录。

推荐流程：

1. 先读取当前 CommandPack 或任务意图。
2. 读取 `docs/DOCS_MAP.md` 判断相关文档类型。
3. 根据任务风险选择：
   - FAST：只读最小必要文档；
   - SAFE：读 L1 + 必要 L2 / MODULE_BOUNDARY / TESTING；
   - AUDIT：读 L1 + L2 + L3 + 相关专项文档。
4. 如果 DOCS_MAP 显示目标文档缺失或过期，应 STOP 并报告上下文缺口。

### FAST 任务

通常只需要：

- 当前 CommandPack
- Skill / AI 执行规则
- 相关文件
- 必要时读取 `docs/CONTEXT_PACK.md`

### SAFE 任务

通常需要：

- 当前 CommandPack
- `docs/CONTEXT_PACK.md`
- 必要时读取 `docs/context/CONTEXT_PACK_L2.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 相关源码和测试

### AUDIT 任务

通常需要：

- 当前 CommandPack
- `docs/CONTEXT_PACK.md`
- `docs/context/CONTEXT_PACK_L2.md`
- `docs/context/CONTEXT_PACK_L3.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 与任务相关的专项文档

### STOP 情况

如果当前任务需要某份文档，但该文档缺失、过期或内容明显冲突，应 STOP，并在 ExecutionReport 中说明缺口。

## 6. 文档更新策略

文档更新不应凭感觉乱改。

原则：

- 新增、删除、重命名文件：更新 `MANIFEST.md`。
- 新增重要文档：更新 `docs/DOCS_MAP.md`。
- 项目状态变化：更新 `docs/CONTEXT_PACK.md`。
- 模块边界变化：更新 `docs/MODULE_BOUNDARY.md`。
- 测试 / 构建命令变化：更新 `docs/TESTING.md`。
- 重要 PR 完成：更新 `docs/PR_SUMMARIES.md`。
- 下一阶段计划变化：更新 `docs/NEXT_PHASE_PLAN.md`。
- 合同生成流程变化：更新 `docs/08-commandpack-generation-guide.zh-CN.md` 或 `docs/12-commandpack-generation-layer.zh-CN.md`。

### 6.1 重要文档变更同步规则

当新增、删除、重命名重要文档时，必须同步检查以下文件：

1. `MANIFEST.md`
   - 记录文件是否存在；
   - 记录文件路径；
   - 维护完整文件清单。

2. `docs/DOCS_MAP.md`
   - 记录该文档的用途；
   - 记录谁会读；
   - 记录什么时候读；
   - 记录什么时候更新。

3. `README.md`
   - 只有当新增文档影响项目入口、核心结构或新用户理解时才需要更新；
   - 不要让 README 变成全量文档清单。

4. `docs/PR_SUMMARIES.md`
   - 重要文档新增 / 删除 / 重命名应在对应 PR 记录中说明。

规则：

- 新增重要文档：更新 `DOCS_MAP.md`。
- 删除重要文档：从 `DOCS_MAP.md` 移除或标记迁移。
- 重命名重要文档：同步更新 `DOCS_MAP.md` 中的路径。
- 普通小文档或临时草稿不一定进入 DOCS_MAP，但进入正式 docs 体系后必须补充。
