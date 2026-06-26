# 快速开始

目标：用 15-30 分钟，把一个普通项目升级成"适合 AI 协作"的项目骨架。

这不是让你一次性写完所有文档，而是先建立最小可用的上下文、边界和门禁。

---

## 0. 最小可用流程

你不需要一开始填写所有文档。

最小只需要：

1. `skills/codex-ide-executor-zh/SKILL.md`
2. 一个 `CommandPack`

普通用户可以先填写 `templates/TASK_INTAKE.md.template`（任务意图表），再由项目负责人、规划型 AI、CLI 或插件生成 CommandPack。

`.ai_rules.md` 是项目级规则摘要，适合未来 CLI / 插件生成。手工使用时可以先不创建。

如果你看不懂 CommandPack 里的工程词汇，如门禁、依赖、权限、schema、幂等、并发、回滚，可以先看：

- `docs/11-engineering-concepts-foundation.zh-CN.md`

文件选择详见：[`docs/10-file-roles-and-usage-modes.zh-CN.md`](docs/10-file-roles-and-usage-modes.zh-CN.md)

---

## 1. 前置原则

不要直接让 AI 开始写功能。

先建立以下最小结构：

```txt
your-project/
  README.md
  AGENTS.md
  docs/
    CONTEXT_PACK.md
    MODULE_BOUNDARY.md
    TESTING.md
    PR_SUMMARIES.md
  scripts/
    check_utf8.py
  .editorconfig
  .gitattributes
  .gitignore
```

然后再用 CommandPack 让 AI 执行具体任务。

---

## 2. 复制基础模板

从本仓库复制：

```txt
templates/AGENTS.md.template              -> your-project/AGENTS.md
templates/AI_RULES.md.template            -> your-project/.ai_rules.md
templates/CONTEXT_PACK.md.template        -> your-project/docs/CONTEXT_PACK.md
templates/MODULE_BOUNDARY.md.template     -> your-project/docs/MODULE_BOUNDARY.md
templates/TESTING.md.template             -> your-project/docs/TESTING.md
templates/PR_SUMMARIES.md.template        -> your-project/docs/PR_SUMMARIES.md
templates/.editorconfig.template          -> your-project/.editorconfig
templates/.gitattributes.template         -> your-project/.gitattributes
templates/.gitignore.template             -> your-project/.gitignore
scripts/check_utf8.py                     -> your-project/scripts/check_utf8.py
```

重要：复制 `AI_RULES.md.template` 为 `.ai_rules.md` 后，按项目实际情况替换 `{{PLACEHOLDER}}` 占位符。这是项目级规则摘要，按需使用，不是 AI 每次任务必读文件。

如果你的项目已经有这些文件，不要直接覆盖，先合并内容。

---

## 2. 写 README.md

README 先写最小版本即可：

```md
# 项目名称

## 项目定位

一句话说明项目解决什么问题。

## 当前状态

- 当前版本：
- 已完成：
- 未完成：
- 暂不做：

## 技术栈

- 前端：
- 后端：
- 桌面端：
- 数据库：
- AI 接入：

## 本地开发

```bash
npm install
npm run dev
```

## 测试与构建

```bash
npm run lint
npm run typecheck
npm test
npm run build
```
```

README 的目的不是写论文，而是让人和 AI 快速知道项目是什么、怎么跑。

---

## 3. 写 AGENTS.md

AGENTS.md 是给 AI 执行代理看的仓库规则。

你至少要写清楚：

- 仓库结构。
- 哪些目录可以改。
- 哪些路径不能乱改。
- 常用命令。
- UTF-8 规则。
- 防屎山规则。
- 门禁要求。
- ExecutionReport 要求。

可以直接从模板开始：

```txt
templates/AGENTS.md.template
```

---

## 4. 写 CONTEXT_PACK.md

ContextPack 是给 AI 快速读取的项目上下文包。

默认推荐分层结构：

- `docs/CONTEXT_PACK.md`：L1 上下文入口（普通用户通常只需要维护这个）。
- `docs/context/CONTEXT_PACK_L2.md`：深入协作上下文。
- `docs/context/CONTEXT_PACK_L3.md`：审计 / 交接上下文。

ContextPack 不应该等项目后期才一次性生成。推荐从项目开始就建立 L1，每个重要任务后记录 Context Delta。

普通用户通常只需要维护 `docs/CONTEXT_PACK.md` 的 L1。
复杂项目或长期项目可以逐步补充 L2 / L3。

最小版本写清楚：

- 项目定位。
- 当前版本状态。
- 核心模块。
- 主要命令。
- 当前重点。
- 禁止事项。
- 下一步计划。

不要把所有细节都塞进去。  
ContextPack 是压缩上下文，不是文档垃圾桶。

详见：[`docs/09-contextpack-lifecycle.zh-CN.md`](docs/09-contextpack-lifecycle.zh-CN.md)

---

## 5. 写 MODULE_BOUNDARY.md

这是防止 AI 制造屎山代码的关键。

最小版本写清楚：

- 哪些文件只是入口。
- 哪些文件不能继续膨胀。
- 新功能应该放在哪些目录。
- 哪些模块之间不能随意调用。

尤其要明确：

```md
main.js / index.js / App.tsx / styles.css / preload.ts / renderer.ts
只允许做 wiring、初始化、路由接线、兼容委托。
不得继续加入大段业务逻辑。
```

---

## 6. 写 TESTING.md

最小版本写清楚：

- lint 怎么跑。
- typecheck 怎么跑。
- test 怎么跑。
- build 怎么跑。
- UTF-8 检查怎么跑。
- 哪些门禁失败必须阻断。

例如：

```md
## 普通 PR 必跑

- npm run lint
- npm run typecheck
- npm test

## 涉及中文文件时必跑

- python scripts/check_utf8.py

## 发布前必跑

- npm run build
```

---

## 7. 建立 UTF-8 门禁

复制：

```txt
templates/.editorconfig.template -> .editorconfig
templates/.gitattributes.template -> .gitattributes
scripts/check_utf8.py -> scripts/check_utf8.py
```

然后运行：

```bash
python scripts/check_utf8.py .
```

如果你的项目里包含中文 Markdown、JSON、JS、TS、HTML、CSS、UI 文案，这一步很重要。

---

## 8. 建立 Git 基线

项目初始化完成后，建立 baseline：

```bash
git status --short
git add .
git commit -m "chore: initialize AI collaboration docs"
git tag baseline-ai-collab-v0
```

如果项目已经有大量未提交改动，先不要盲目提交。  
先确认这些改动是否都应该进入基线。

---

## 9. 第一次给 AI 发任务

不要直接说：

> 帮我加一个功能。

不熟悉工程规范的用户可以先填写 `templates/TASK_INTAKE.md.template`（任务意图表），由项目负责人、规划型 AI、CLI 或插件生成 CommandPack。

使用 CommandPack：

```txt
templates/CommandPack.md.template
```

最小示例：

```md
# CommandPack：修复按钮文案错别字

## 基本信息

- 执行模式：FAST
- repoRoot：当前仓库

## 任务目标

只修复首页按钮上的错别字。

不做：

- 不改 UI 布局
- 不改业务逻辑
- 不重构组件

## 必读上下文

- AGENTS.md
- README.md
- docs/CONTEXT_PACK.md
- 相关组件文件

## 允许修改路径

- src/components/HomeButton.tsx

## 禁止修改路径

- package.json
- src/main.ts
- src/services/
- docs/

## 必跑门禁

- npm run typecheck
- python scripts/check_utf8.py

## STOP 条件

- 发现中文乱码
- 需要修改禁止路径
- 需要扩大范围
- 测试无法运行且原因不明

---

## 10. 文档不是死文件

本套规范依赖仓库文档保存长期上下文。

重要变更后，记得同步更新。以下路径是本套件推荐的标准模板路径，实际项目可以按自己的文档结构调整，Skill 不强制所有项目使用完全相同的文件名：

- `docs/CONTEXT_PACK.md`（项目上下文）
- `docs/MODULE_BOUNDARY.md`（模块边界）
- `docs/TESTING.md`（测试门禁）
- `docs/PR_SUMMARIES.md`（迭代记录）
- `MANIFEST.md`（文件清单）
- `CHANGELOG.md`（变更日志）

如果 AI 没有权限更新相关文档，要求其在 ExecutionReport 中明确标记需要回写。

## ExecutionReport

完成后输出目标、修改文件、门禁结果、UTF-8 检查、回滚方式。
```

---

## 10. 人类审查 ExecutionReport

AI 返回报告后，重点看：

- 是否只改了允许路径？
- 是否改了无关文件？
- 是否有中文乱码？
- 是否把逻辑塞进中央大文件？
- 是否运行了门禁？
- 门禁失败有没有说清楚？
- 是否给出回滚方式？
- 下一步建议是否合理？

没有验证证据，不要收口。

---

## 11. 每次重要 PR 后更新上下文

完成一次重要变更后，更新：

```txt
docs/PR_SUMMARIES.md
docs/CONTEXT_PACK.md
docs/MODULE_BOUNDARY.md（如模块边界变化）
docs/TESTING.md（如命令或门禁变化）
```

核心原则：

> 代码变了，文档也要变。  
> 不要让后续 AI 读取旧上下文。

---

## 12. 三种任务模式快速判断

### FAST

用于：

- 小 bug
- 小文案
- 小样式
- 单文件低风险修复

不用于：

- 权限
- license
- 计费
- schema
- 数据结构
- 生产配置
- 跨模块重构

### SAFE

用于：

- 普通功能
- 常规 PR
- 小模块开发
- UI 与数据联动

### AUDIT

用于：

- 架构
- 权限
- license
- 计费
- schema
- 数据迁移
- 生产发布
- 仓库收口

默认用 SAFE。  
小任务用 FAST。  
碰核心规则自动升级 AUDIT。

---

## 13. 最小成功标准

完成快速开始后，你的项目应该至少做到：

- AI 知道先读 `AGENTS.md`。
- AI 知道项目上下文在 `CONTEXT_PACK.md`。
- AI 知道新逻辑不能塞进中央大文件。
- AI 知道中文必须保持 UTF-8。
- AI 知道任务完成后必须跑门禁。
- AI 知道必须输出 ExecutionReport。
- 人知道如何审查 AI 的执行结果。

## 14. AI 工具使用流程

新手不需要先理解完整规范全文。  
先拿 `SKILL.md + CommandPack` 跑起来。  
有项目特殊规则时，再补 `.ai_rules.md` / `AGENTS.md` / ContextPack。  
完整规范用于后续深入理解，不是日常运行前置要求。

### 最小可用流程

1. 复制或使用 `skills/codex-ide-executor-zh/SKILL.md` 作为 AI 执行规则。
2. 用 `templates/CommandPack.md.template` 写本次任务合同。
3. 把 `SKILL.md + CommandPack` 给 AI。
4. AI 根据任务需要再读取项目资料。
5. AI 完成后输出 ExecutionReport。

### 每次任务的标准流程

1. 先复制 `templates/AI_RULES.md.template` 为 `.ai_rules.md`，替换占位符（可选，项目有特殊规则时）。
2. 每次任务写一个 CommandPack。
3. 把 `SKILL.md + CommandPack` 给 AI。
4. AI 按 FAST / SAFE / AUDIT 执行，按需读取项目资料。
5. 任务完成后，人检查 ExecutionReport。
6. 重要变更更新 `PR_SUMMARIES.md` 和 `CONTEXT_PACK.md`。

### 关键原则

- 日常任务只需要 `CommandPack + SKILL.md`。
- `.ai_rules.md` / `AGENTS.md` / ContextPack 是项目资料，按需读取。
- 完整规范是维护 / 审计 / 教学 / 复盘资料，不是日常任务默认上下文。
- 高风险、不明确或规则冲突时，AI 应 STOP，而不是自行读取完整规范继续执行。
- 本套件不是要求 AI 机械地遇到任何小问题都 STOP。在低风险、同因、局部、可验证的条件下，AI 可以处理必要的前置小问题和同类小修复。但涉及权限、license、计费、schema、密钥、生产配置、用户数据、依赖升级、跨模块重构时，必须 STOP。
- CommandPack 是每次任务的具体合同，必须写清楚目标、范围、门禁。

详细说明见 `USAGE.md` 和 `docs/00-how-to-use-with-ai-agent.zh-CN.md`。
