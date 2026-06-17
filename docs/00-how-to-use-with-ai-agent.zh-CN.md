# 如何在 AI 编程工具中使用本规范包

## 1. 核心问题

不要每次把完整执行规范塞给 AI。

完整规范很重要，但它适合作为源规范、审计依据和复杂任务参考，不适合作为每次任务的默认上下文。

`SKILL.md` 已重构为轻量路由型 Skill（约 330 行），负责判断任务模式、读取顺序和升级规则。完整规范沉淀在 `docs/02-agent-execution-spec.zh-CN.md` 和 `references/FULL_EXECUTION_SPEC.zh-CN.md` 中，仅作为维护 / 审计资料。

---

## 2. 默认使用方式

AI 日常任务默认只需要：

1. 当前 `CommandPack`
2. `skills/codex-ide-executor-zh/SKILL.md`

不要默认要求 AI 读取完整规范。

如果 CommandPack 或 Skill 判断需要更多信息，再按需读取：

- `.ai_rules.md`
- `AGENTS.md`
- `docs/CONTEXT_PACK.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 相关源码和测试

---

## 3. 什么时候读完整规范

完整规范不作为默认 AI 运行上下文。

完整规范只在以下情况作为参考：

- 人类维护规范
- 修改 Skill / 执行规范本身
- 开源文档、教学、复盘、审计场景需要引用完整制度

日常代码任务不应依赖完整规范。

遇到高风险、不明确或规则冲突时，AI 应 STOP，而不是自行读取完整规范后继续执行。

---

## 4. FAST / SAFE / AUDIT 读取策略

### FAST MODE

读取：

- 当前 CommandPack
- `.ai_rules.md` / `AGENTS.md`，按需
- 当前相关文件

### SAFE MODE

读取：

- 当前 CommandPack
- `.ai_rules.md` / `AGENTS.md`，按需
- `docs/CONTEXT_PACK.md` L1
- `docs/MODULE_BOUNDARY.md` 相关部分
- 相关源码和测试

### AUDIT MODE

读取：

- 当前 CommandPack
- `.ai_rules.md`
- `AGENTS.md`
- `docs/CONTEXT_PACK.md` L2/L3
- `docs/PRODUCT_ARCHITECTURE.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`

高风险、不明确或规则冲突时，优先 STOP，要求更明确的 CommandPack 或人工确认。

---

## 5. Claude 使用方式

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

## 6. Codex 使用方式

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

## 7. Cursor / Copilot / IDE Agent 使用方式

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

## 9. 正确用法

应该：

- 项目中长期保存 `.ai_rules.md`（可选）。
- 每次任务使用 CommandPack。
- 日常只用 CommandPack + SKILL.md。
- 审计任务才读完整规范。
- 执行后检查报告。
- 重要变更更新 `PR_SUMMARIES` / `CONTEXT_PACK`。

---

## 10. 快速检查清单

在给 AI 发任务前，确认：

- [ ] 项目根目录有 `.ai_rules.md` 吗？（可选）
- [ ] `.ai_rules.md` 中的占位符替换了吗？
- [ ] 当前 CommandPack 写好了吗？
- [ ] 任务模式判断对了吗（FAST / SAFE / AUDIT）？
- [ ] 允许路径和禁止路径明确了吗？
- [ ] 门禁要求写清楚了吗？
- [ ] AI 知道只需 CommandPack + SKILL.md 吗？
- [ ] 人准备好了审查 ExecutionReport 吗？
