# 使用指南

## 这套规范怎么用

本项目不是让 AI 每次读取完整执行规范。

所有文件分为三类：

### 1. 运行时文件

AI 每次真正需要的是：

- `CommandPack`
- `skills/codex-ide-executor-zh/SKILL.md`

其中：

- `CommandPack` 是本次任务合同，说明要做啥、不做啥、允许改哪、禁止改哪、必跑什么门禁。
- `SKILL.md` 是压缩执行器，负责判断 FAST / SAFE / AUDIT、STOP 条件、UTF-8、防屎山、门禁和报告要求。

### 2. 项目资料文件

这些不是每次必读，而是按需读取：

- `.ai_rules.md`
- `AGENTS.md`
- `docs/CONTEXT_PACK.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 相关源码和测试

### 3. 维护与审计文件

这些给人类维护、复杂审计和规范演进使用：

- `docs/02-agent-execution-spec.zh-CN.md`
- `skills/codex-ide-executor-zh/references/FULL_EXECUTION_SPEC.zh-CN.md`

日常任务默认只给 AI 两样东西：

1. 当前 CommandPack
2. `skills/codex-ide-executor-zh/SKILL.md`

完整规范不作为日常 AI 上下文。遇到高风险、不明确或规则冲突时，AI 应 STOP，而不是自行读取完整规范继续执行。

---

## 新项目怎么设置

1. 复制 `templates/AGENTS.md.template` 为 `AGENTS.md`
2. 复制 `templates/AI_RULES.md.template` 为 `.ai_rules.md`
3. 复制 `templates/CONTEXT_PACK.md.template` 为 `docs/CONTEXT_PACK.md`
4. 复制 `templates/MODULE_BOUNDARY.md.template` 为 `docs/MODULE_BOUNDARY.md`
5. 复制 `templates/TESTING.md.template` 为 `docs/TESTING.md`
6. 复制 `.editorconfig.template` / `.gitattributes.template`
7. 复制 `scripts/check_utf8.py`
8. 按项目实际情况替换占位符

---

## 已有项目怎么设置

1. 先读 `SELF_DIAGNOSIS.md`
2. 检查缺失的规范文件
3. 先补 `AGENTS.md`
4. 再补 `.ai_rules.md`
5. 再补 `CONTEXT_PACK.md`
6. 再补 `MODULE_BOUNDARY.md`
7. 再补 `TESTING.md`
8. 不要一次性重写全部文档，先建立最小可用规则

---

## 每次让 AI 改代码时怎么做

1. 普通用户先填写 `templates/TASK_INTAKE.md.template`（任务意图表），不需要手写 CommandPack。
2. CommandPack 可以由项目负责人、规划型 AI、CLI 或插件从 Task Intake 生成。
3. CommandPack 中明确任务目标、允许路径、禁止路径、必读上下文、门禁、STOP 条件
4. 把 CommandPack + `SKILL.md` 给 AI
5. AI 按需读取项目资料
6. AI 执行后必须输出 ExecutionReport
7. 人检查 diff、测试结果、风险和回滚方式
8. 重要变更写入 `PR_SUMMARIES.md` 和 `CONTEXT_PACK.md`

---

## Claude / Codex / Cursor 怎么用

### Claude / Claude Code

把以下内容交给 Claude：

- 当前 CommandPack
- `skills/codex-ide-executor-zh/SKILL.md`

告诉它：

> 请按 CommandPack 和 SKILL.md 执行任务。若任务需要更多上下文，再按需读取 .ai_rules.md、AGENTS.md、CONTEXT_PACK、相关源码和测试。不要默认读取完整规范。完成后输出 ExecutionReport。

### Codex

推荐使用：

- `skills/codex-ide-executor-zh/SKILL.md`（路由型 Skill）
- 当前 CommandPack

`SKILL_RUNTIME.md` 是可选更短 Runtime 摘要。

完整规范不作为日常 AI 上下文。遇到高风险、不明确或规则冲突时，AI 应 STOP。

### Cursor / Copilot / 其他 IDE Agent

如果工具不支持 Skill，就使用通用方式：

- 把 `SKILL.md` 作为执行规则文本
- 把 CommandPack 作为当前任务合同
- `.ai_rules.md` / `AGENTS.md` / ContextPack 是按需项目资料
- 要求 AI 不扩大范围
- 要求输出 ExecutionReport
- 不需要附完整规范

---

## ContextPack 应从项目开始维护

ContextPack 不应该等项目后期才一次性生成。

推荐流程：

1. 用 `PROJECT_INTAKE.md.template` 收集项目基本情况。
2. 生成初始 L1 ContextPack。
3. 每个重要任务后记录 Context Delta。
4. 阶段性整理 L2 / L3。

未来 CLI / 插件可以自动生成，但在此之前，可以由项目负责人、规划型 AI 或执行代理在授权范围内维护。

详见：[`docs/09-contextpack-lifecycle.zh-CN.md`](docs/09-contextpack-lifecycle.zh-CN.md)

---

## 文档不是死文件

本套规范依赖仓库文档保存长期上下文。

重要变更后，应同步更新项目文档。以下路径是本套件推荐的标准模板路径，实际项目可以按自己的文档结构调整：

- `docs/CONTEXT_PACK.md`（项目上下文）
- `docs/MODULE_BOUNDARY.md`（模块边界）
- `docs/TESTING.md`（测试门禁）
- `docs/PR_SUMMARIES.md`（迭代记录）
- `MANIFEST.md`（文件清单）
- `CHANGELOG.md`（变更日志）

如果项目采用不同名称，可在 CommandPack / AGENTS.md / `.ai_rules.md` 中声明。

如果 AI 没有权限更新相关文档，必须在 ExecutionReport 中明确标记需要回写。

---

## 一句话原则

> 完整规范是母版。  
> Skill 是压缩执行器。  
> CommandPack 是本次任务合同。  
> AI 平时只需要后两者。
