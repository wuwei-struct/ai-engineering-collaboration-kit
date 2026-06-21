# 如何在 AI 编程工具中使用本规范包

> 文件选择和使用模式见：[`docs/10-file-roles-and-usage-modes.zh-CN.md`](10-file-roles-and-usage-modes.zh-CN.md)

---

## 1. 核心原则

AI 日常任务最小只需要：

1. 当前 `CommandPack`
2. `skills/codex-ide-executor-zh/SKILL.md`

不要求 AI 默认读取完整规范。按需再补充 `.ai_rules.md`、`AGENTS.md`、`CONTEXT_PACK.md` 等项目资料。

完整规范仅作为维护、审计、教学和复盘使用。

---

## 2. Claude 使用方式

### 推荐 Prompt

把以下内容交给 Claude：

```text
请按下面两个文件执行任务：

1. 当前 CommandPack
2. Skill 执行规则：skills/codex-ide-executor-zh/SKILL.md

你只需要按这两份执行。若任务需要更多上下文，再按 Skill 判断读取 .ai_rules.md、AGENTS.md、CONTEXT_PACK、相关源码和测试。

不要默认读取完整规范。完成后输出 ExecutionReport。
```

### 关键原则

- Claude Project / Custom Instructions 中只放稳定规则，不放项目临时信息。
- 每次任务用 CommandPack 约束范围。
- 任务完成后让人检查 ExecutionReport。

---

## 3. Codex 使用方式

SKILL.md 是 Codex Skill 主入口。  
CommandPack 是当前任务合同。  
.ai_rules.md / AGENTS.md / ContextPack 是按需项目资料。  
完整规范是维护/审计资料，不是日常任务默认上下文。

### 设置步骤

1. 将 `skills/codex-ide-executor-zh/` 复制到 Codex 支持的 Skill 目录。
2. 每次任务使用 CommandPack。
3. AGENTS.md /.ai_rules.md 按需求放置。

### 推荐做法

- 日常任务：`SKILL.md + CommandPack`。
- AUDIT 任务：加载完整执行规范。
- 始终配合 CommandPack 使用。

---

## 4. Cursor / Copilot / IDE Agent 使用方式

如果工具不支持 Skill 格式，使用通用方式：

1. 如果工具不支持 Skill，就把 `SKILL.md` 当成执行规则文本。
2. 再附上 CommandPack。
3. 不需要附完整规范。
4. `.ai_rules.md` / `AGENTS.md` / ContextPack 是按需项目资料。
5. 要求 AI 不扩大范围。
6. 要求输出 ExecutionReport。

如果 AI 不主动读取 `.ai_rules.md`，可以手动粘贴给它。

---

## 8. 错误用法

不要：

- 每次都粘贴完整执行规范。
- 只说"帮我改一下"而不给 CommandPack。
- 不写允许路径和禁止路径。
- 不要求测试门禁。
- 不检查 ExecutionReport。
- 不更新 ContextPack。

---

## 6. 正确用法

应该：

- 项目中长期保存 `.ai_rules.md`（可选）。
- 每次任务使用 CommandPack。
- 日常只用 CommandPack + SKILL.md。
- 审计任务才读完整规范。
- 执行后检查报告。
- 重要变更更新 `PR_SUMMARIES` / `CONTEXT_PACK`。

---

## 7. 快速检查清单

在给 AI 发任务前，确认：

- [ ] 项目根目录有 `.ai_rules.md` 吗？（可选）
- [ ] `.ai_rules.md` 中的占位符替换了吗？
- [ ] 当前 CommandPack 写好了吗？
- [ ] 任务模式判断对了吗（FAST / SAFE / AUDIT）？
- [ ] 允许路径和禁止路径明确了吗？
- [ ] 门禁要求写清楚了吗？
- [ ] AI 知道只需 CommandPack + SKILL.md 吗？
- [ ] 人准备好了审查 ExecutionReport 吗？
