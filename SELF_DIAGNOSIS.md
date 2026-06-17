# 你的项目是否需要这套框架？

这份自诊清单用于判断：你的项目是否已经到了需要“AI 工程协作规范”的阶段。

如果只是一次性 demo，也许不需要。  
如果你希望项目长期维护、持续迭代，并且 AI 已经开始深度参与代码修改，那么这套框架会非常有用。

---

## 症状 1：AI 经常乱改文件

- [ ] AI 修改了不该修改的文件。
- [ ] AI 顺手重构了无关模块。
- [ ] AI 改了业务规则但没有告诉你。
- [ ] AI 为了完成任务，改动了很多无关路径。
- [ ] AI 把新逻辑塞进 `main.js`、`index.js`、`App.tsx`、`styles.css` 等中央大文件。
- [ ] 你经常需要手动回滚 AI 的“顺手改”。

可能原因：

你的项目缺少清晰的任务范围、允许路径、禁止路径和模块边界。

建议补充：

- `AGENTS.md`
- `docs/MODULE_BOUNDARY.md`
- `templates/CommandPack.md.template`

---

## 症状 2：代码越来越乱

- [ ] 中央文件越来越大。
- [ ] 相同逻辑被复制粘贴多次。
- [ ] utils / service / main / App 等文件承担了过多职责。
- [ ] 新功能不知道该放在哪个目录。
- [ ] 模块之间随意调用，边界越来越模糊。
- [ ] AI 经常把临时实现伪装成正式实现。

可能原因：

项目缺少模块设计、架构边界和 anti-spaghetti 规则。

建议补充：

- `docs/MODULE_BOUNDARY.md`
- `docs/PRODUCT_ARCHITECTURE.md`
- `docs/DEV_GUIDE.md`
- `AGENTS.md`

---

## 症状 3：每次都要重新解释项目

- [ ] 每次跟 AI 讨论，都要重新说明项目结构。
- [ ] 换一个对话，AI 就忘记了之前的上下文。
- [ ] 聊天记录越来越长，项目上下文越来越散。
- [ ] AI 不知道最近完成了哪些 PR。
- [ ] AI 不知道哪些模块已经稳定，哪些还在重构。
- [ ] AI 反复提出已经否定过的方案。

可能原因：

项目缺少文档化上下文，长期记忆没有沉淀到仓库里。

建议补充：

- `docs/CONTEXT_PACK.md`
- `docs/PR_SUMMARIES.md`
- `docs/NEXT_PHASE_PLAN.md`
- `docs/AI_HANDOFF.md`（复杂项目可选）

---

## 症状 4：中文总是乱码

- [ ] 中文 Markdown 被写乱码。
- [ ] JSON 文案出现问号或异常字符。
- [ ] diff 中出现大量不可解释的中文变化。
- [ ] 出现 mojibake，例如 `<mojibake example>` 这类字符。
- [ ] PowerShell / 脚本写入后中文损坏。
- [ ] AI 复制了已经乱码的上下文继续修改。

可能原因：

项目缺少 UTF-8 编码规范和编码检查门禁。

建议补充：

- `.editorconfig`
- `.gitattributes`
- `scripts/check_utf8.py`
- `docs/TESTING.md`
- `AGENTS.md` 中的 UTF-8 硬规则

---

## 症状 5：AI 没验证就说完成

- [ ] AI 说完成了，但没有跑测试。
- [ ] AI 说“应该可以”，但没有门禁证据。
- [ ] build 失败后，AI 仍然声称任务完成。
- [ ] lint/typecheck/test 的失败没有被记录。
- [ ] 每次都需要你自己追问“跑测试了吗？”

可能原因：

项目缺少明确的测试门禁和 ExecutionReport 要求。

建议补充：

- `docs/TESTING.md`
- `templates/CommandPack.md.template`
- `templates/PR_SUMMARIES.md.template`
- `skills/codex-ide-executor-zh/SKILL.md`

---

## 症状 6：改完不知道怎么回滚

- [ ] AI 一次改了很多文件，不知道哪些是必要的。
- [ ] 没有 baseline commit。
- [ ] 没有阶段 tag。
- [ ] 没有 rollback notes。
- [ ] 出问题后只能手动对比文件。
- [ ] AI 执行前没有检查工作区是否干净。

可能原因：

项目缺少 Git 收口、阶段基线和回滚纪律。

建议补充：

- `docs/TESTING.md`
- `docs/PR_SUMMARIES.md`
- `templates/CommandPack.md.template`
- 每次任务的 ExecutionReport
- 重要阶段的 baseline commit / tag

---

## 症状 7：项目越来越依赖聊天记录

- [ ] 重要决策只存在于聊天里。
- [ ] 仓库文档没有更新。
- [ ] 新 AI 代理不知道项目真实状态。
- [ ] 代码变了，但 ContextPack 没变。
- [ ] 模块拆分了，但 MODULE_BOUNDARY 没更新。
- [ ] 测试命令变了，但 TESTING 没更新。

可能原因：

项目缺少“每次迭代后更新上下文文档”的收口流程。

建议补充：

- `docs/PR_SUMMARIES.md`
- `docs/CONTEXT_PACK.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 任务收口规则

---

## 快速判断

如果你只勾选了 0-2 项：

你可能只是偶尔用 AI 写代码，暂时不需要完整框架。可以先使用 `CommandPack` 模板和 UTF-8 检查脚本。

如果你勾选了 3-6 项：

你的项目已经需要基础协作规范。建议先补：

- `AGENTS.md`
- `CONTEXT_PACK.md`
- `MODULE_BOUNDARY.md`
- `TESTING.md`

如果你勾选了 7 项以上：

你的项目已经进入“AI 协作复杂化”阶段。建议完整采用本套件，并开始按 FAST / SAFE / AUDIT 模式管理 AI 任务。

---

## 推荐下一步

1. 阅读 `QUICK_START.md`。
2. 按照最小流程补齐项目基础文档。
3. 复制 `templates/AGENTS.md.template` 到项目根目录。
4. 复制 `templates/CONTEXT_PACK.md.template` 到 `docs/CONTEXT_PACK.md`。
5. 把 `scripts/check_utf8.py` 放进项目脚本目录。
6. 下一次给 AI 任务时，用 `templates/CommandPack.md.template`。
7. AI 执行完成后，要求它返回 ExecutionReport。

---

## 核心判断

如果 AI 只是帮你写几行代码，规范可以很轻。

如果 AI 已经在参与真实项目开发，那么你需要的不只是 prompt，而是一套工程协作系统：

> 上下文、范围、边界、门禁、回滚、报告。
