# 工具集成指南

本指南说明如何把 AI Engineering Collaboration Kit 用到不同 AI 编程工具和工程环境中。

核心原则：

> 工具可以不同，但流程应稳定：读上下文、锁范围、最小修改、跑门禁、交报告。

---

## 1. 通用 AI 编程代理使用方式

不管你使用 Codex、Claude、Copilot、Cursor、Trae、IDE Agent 还是 CLI Agent，都建议采用同一套协作结构：

```txt
仓库规则：AGENTS.md
项目上下文：docs/CONTEXT_PACK.md
模块边界：docs/MODULE_BOUNDARY.md
测试门禁：docs/TESTING.md
任务合同：CommandPack
执行结果：ExecutionReport
```

每次任务流程：

1. 先让 AI 阅读 `AGENTS.md` 和必要上下文。
2. 通过 CommandPack 明确任务目标、允许路径、禁止路径、门禁。
3. AI 按 FAST / SAFE / AUDIT 执行。
4. AI 输出 ExecutionReport。
5. 人审查 diff、门禁结果、风险和回滚方式。
6. 重要变更更新 `PR_SUMMARIES.md` / `CONTEXT_PACK.md`。

---

## 2. Codex / IDE Skill 集成

本仓库提供 Codex/IDE 风格的 Skill：

```txt
skills/codex-ide-executor-zh/
  SKILL.md          # 路由型 Skill（约 330 行），AI 日常执行入口
  SKILL_RUNTIME.md  # 可选更短 Runtime 摘要
  references/
    FULL_EXECUTION_SPEC.zh-CN.md  # 完整执行规范引用副本（维护/审计用）
  scripts/
  assets/
```

### 2.1 使用方式

如果你的工具支持 Skill 目录：

1. 将 `skills/codex-ide-executor-zh/` 复制到工具支持的 Skill 目录。
2. 确认 `SKILL.md` 中的 `name` 和 `description` 保持不变。
3. 日常任务：使用 `SKILL.md + CommandPack`。
4. AUDIT 任务：使用完整执行规范（`references/FULL_EXECUTION_SPEC.zh-CN.md`）。
5. 每次任务仍然使用 CommandPack。

### 2.2 仓库级规则

将：

```txt
templates/AGENTS.md.template
```

复制到目标项目根目录：

```txt
your-project/AGENTS.md
```

然后根据项目实际结构修改。

### 2.3 自定义指令

如果工具支持“全局自定义指令”，不要塞入整份规范，只放短硬规则：

```md
你是代码执行代理。所有仓库任务必须：
- 先读 AGENTS.md / README / ContextPack。
- 按当前任务合同执行，不扩大范围。
- 保持 UTF-8，不破坏中文。
- 不把新逻辑塞进中央大文件。
- 运行可运行门禁。
- 完成后输出 ExecutionReport。
- 如上下文不足、范围不足、编码异常、安全风险不明，必须 STOP。
```

完整细则放在 Skill / AGENTS.md / 仓库文档中。

---

## 3. Claude / 通用聊天式 AI 使用方式

如果工具不支持 Codex Skill 格式，也可以使用这套框架。

### 3.1 推荐 Prompt

把以下内容交给 Claude：

```text
请按下面两个文件执行任务：

1. 当前 CommandPack
2. Skill 执行规则：skills/codex-ide-executor-zh/SKILL.md

你只需要按这两份执行。若任务需要更多上下文，再按 Skill 判断读取 .ai_rules.md、AGENTS.md、CONTEXT_PACK、相关源码和测试。

不要默认读取完整规范。完成后输出 ExecutionReport。
```

### 3.2 关键原则

- Claude Project / Custom Instructions 中只放稳定规则，不放项目临时信息。
- 每次任务用 CommandPack 约束范围。
- 日常任务让 Claude 读 CommandPack + SKILL.md，不读完整规范。
- 任务完成后让人检查 ExecutionReport。

### 3.3 方式一：把执行规范作为项目规则

将：

```txt
docs/02-agent-execution-spec.zh-CN.md
```

作为长期项目规则，放入你的项目文档或 Claude Project instructions。

注意不要把项目临时信息都写进长期规则。  
长期规则只写稳定要求：上下文、范围、UTF-8、anti-spaghetti、门禁、报告。

### 3.4 方式二：每次任务使用 CommandPack

即使工具没有 Skill，CommandPack 仍然有效。

模板：

```txt
templates/CommandPack.md.template
```

每次任务至少写清楚：

- 目标。
- 不做什么。
- 必读上下文。
- 允许修改路径。
- 禁止修改路径。
- 必跑门禁。
- STOP 条件。
- ExecutionReport 格式。

### 3.5 方式三：把 ContextPack 粘给 AI

如果 AI 不能直接读取仓库文件，可以把 `docs/CONTEXT_PACK.md` 的 L1/L2 摘要提供给它。

但要注意：

- 仓库文件仍是事实来源。
- 聊天上下文不能替代代码和测试。
- 重要规则应沉淀回仓库文档，而不是只留在聊天记录里。

---

## 4. Cursor / VS Code / IDE Agent

如果工具不支持 Skill 格式，使用通用方式：

1. 如果工具不支持 Skill，就把 `SKILL.md` 当成执行规则文本。
2. 再附上 CommandPack。
3. 不需要附完整规范。
4. `.ai_rules.md` / `AGENTS.md` / ContextPack 是按需项目资料。
5. 要求 AI 不要在中央大文件中堆逻辑。
6. 让它执行本地门禁。
7. 要求输出 ExecutionReport。

如果 AI 不主动读取 `.ai_rules.md`，可以手动粘贴给它。

---

## 5. GitHub Actions / CI 集成

建议把本框架中的“门禁”逐步落实为 CI。

最小 CI 门禁：

- lint
- typecheck
- test
- build
- UTF-8 check

示例：

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run lint --if-present
      - run: npm run typecheck --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
      - run: python scripts/check_utf8.py .
```

如果项目不是 Node，请替换成对应语言的命令。

---

## 6. Git Hook / pre-commit 集成

可以用 pre-commit 或简单 Git hook 保证提交前检查 UTF-8。

示例 `.git/hooks/pre-commit`：

```bash
#!/usr/bin/env bash
set -e

python scripts/check_utf8.py .
```

启用：

```bash
chmod +x .git/hooks/pre-commit
```

注意：

- 不要把复杂构建都塞进 pre-commit。
- 复杂门禁放到 CI。
- pre-commit 适合轻量检查，如 UTF-8、格式、敏感文件。

---

## 7. 人类审查流程集成

AI 完成任务后，人应该看三样东西：

1. `git diff`
2. 门禁结果
3. ExecutionReport

审查重点：

- 是否超范围。
- 是否修改禁止路径。
- 是否产生中文乱码。
- 是否把业务逻辑塞进中央大文件。
- 是否修改业务规则、权限、license、计费、schema。
- 是否跑了必要门禁。
- 是否说明了失败和风险。
- 是否有回滚方式。

没有证据，不要合并。

---

## 8. 团队使用建议

如果团队多人协作，建议统一：

- 同一套 AGENTS.md。
- 同一套 CommandPack 模板。
- 同一套 ExecutionReport 模板。
- 同一套 ContextPack 更新规则。
- 同一套 PR_SUMMARIES 格式。
- 同一套 CI 门禁。

不要让每个人用自己的“魔法 prompt”。  
团队协作靠规则，不靠个人手感。

---

## 9. 工具边界

这套框架不能保证 AI 永远不犯错。

它能做的是：

- 降低 AI 乱改的概率。
- 让错误更容易被发现。
- 让变更更容易回滚。
- 让上下文不依赖聊天记录。
- 让项目从一次性 prompt 走向工程协作。

不要把它当作全自动开发系统。  
它是人和 AI 协作的工程护栏。
