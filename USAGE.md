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

1. 先写一个 CommandPack
2. CommandPack 中明确任务目标、允许路径、禁止路径、必读上下文、门禁、STOP 条件
3. 把 CommandPack + `SKILL.md` 给 AI
4. AI 按需读取项目资料
5. AI 执行后必须输出 ExecutionReport
6. 人检查 diff、测试结果、风险和回滚方式
7. 重要变更写入 `PR_SUMMARIES.md` 和 `CONTEXT_PACK.md`

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

## 一句话原则

> 完整规范是母版。  
> Skill 是压缩执行器。  
> CommandPack 是本次任务合同。  
> AI 平时只需要后两者。
