# 任务合同生成层与执行合同库

本文件说明 Task Intake、CommandPack 和 Task Contract Library 之间的关系。

普通用户不需要直接写 CommandPack。
普通用户只需要描述任务意图。
CommandPack 应由规划型 AI、强模型、项目负责人、CLI 或插件根据上下文生成。
生成后的 CommandPack 默认进入执行合同库，只有被标记为 `active` 的合同才允许执行。

---

## 1. 总体链路

```txt
用户自然语言需求
  ↓
Task Intake / 任务意图表
  ↓
Contract Generator / 任务合同生成层
  ↓
CommandPack / 执行任务合同
  ↓
Task Contract Library / 执行合同库
  ↓
active CommandPack
  ↓
Executor Agent / 执行 Agent
  ↓
ExecutionReport / 执行回执
  ↓
Context Delta / 上下文变化
```

解释：

- `Task Intake` 是需求输入，不是执行合同。
- `CommandPack` 是 AI 执行代理可执行的任务合同。
- `Task Contract Library` 是多个 CommandPack 的状态管理集合。
- 执行 Agent 只能执行 `active` 合同。
- `draft`、`reviewed`、`pending` 都不是执行授权。

---

## 2. 角色分工

### 普通用户

负责描述：

- 想做什么；
- 当前哪里不对；
- 希望完成后是什么效果；
- 哪些功能不要影响；
- 最怕哪里出问题；
- 如何判断改好了。

普通用户不负责填写：

- 允许修改路径；
- 禁止修改路径；
- 模块边界；
- 上下文读取层级；
- 门禁命令；
- STOP 条件。

### 规划层 / Contract Generator

负责根据 Task Intake、ContextPack、ModuleBoundary、项目扫描结果生成 CommandPack。

规划层可以是：

- 项目负责人；
- 规划型 AI；
- 更强推理模型；
- CLI；
- IDE 插件；
- 协作助理。

### 执行 Agent

负责按照 active CommandPack 执行：

- 验证候选路径；
- 修改代码或文档；
- 运行门禁；
- 输出 ExecutionReport；
- 不得执行非 active 合同。

---

## 3. 模型选择建议

CommandPack 生成阶段建议使用能力更强的模型，尤其是以下任务：

- SAFE 任务；
- AUDIT 任务；
- 跨模块任务；
- 涉及权限、license、计费、数据库、schema、migration 的任务；
- 涉及部署上线、生产配置、密钥、用户数据的任务；
- 需要推断允许路径和禁止路径的任务；
- 需要从 ContextPack L2/L3 中抽取上下文的任务。

原因：

- 生成合同是决策行为，不只是文本生成；
- 合同一旦生成错误，后续执行容易跑偏；
- 强模型更适合做风险判断、上下文路由、路径推断和 STOP 条件设计。

但执行阶段不一定必须使用同一个强模型。
执行 Agent 可以是 Codex、Claude Code、Cursor、IDE Agent 或其他代码执行工具。

---

## 4. 语义边界映射

普通用户通常不知道项目文件路径。

因此，用户只需要描述语义边界：

- 允许修改什么功能；
- 不希望影响什么功能；
- 哪些业务不能动；
- 哪些地方风险最高。

规划层负责将语义边界转换为工程边界：

- 候选允许路径；
- 候选禁止路径；
- 必读上下文；
- STOP 条件；
- 门禁命令。

这个过程叫语义边界映射。

### 示例

用户输入：

> 导出 PDF 中文乱码。不要影响登录、支付、license、数据库。不要重构。

规划层生成：

- 用户语义授权：PDF 导出相关逻辑；
- 禁止影响：登录、支付、license、数据库；
- 推断候选路径：
  - `src/export/**`
  - `src/main/pdf/**`
  - `tests/export/**`
- 禁止路径：
  - `src/license/**`
  - `src/billing/**`
  - `src/db/**`
  - `.env*`
- 执行要求：
  - 修改前必须验证候选路径是否存在；
  - 如果实际相关文件不在候选路径内，必须 STOP；
  - 如果需要修改 license / billing / database，必须 STOP。

---

## 5. 路径推断可信度

CommandPack 中的允许路径可以来自规划层推断，但必须标明来源和可信度。

建议字段：

- 路径来源：
  - Task Intake；
  - ContextPack；
  - ModuleBoundary；
  - 项目目录扫描；
  - 关键词搜索；
  - 历史 PR_SUMMARIES；
- 可信度：
  - `high`；
  - `medium`；
  - `low`；
- 是否必须执行前验证：
  - 是。

规则：

- `high`：路径与上下文、目录结构、历史记录高度一致，但执行前仍需验证。
- `medium`：路径大概率相关，但需要先只读定位。
- `low`：路径只是候选，不得直接修改，必须先执行文件定位阶段。

执行 Agent 不得盲信推断路径。
如果路径不匹配、范围不足、需要改禁止路径，必须 STOP。

---

## 6. Task Contract Library / 执行合同库

执行合同库用于保存多个 CommandPack 及其状态。

建议状态：

- `draft`：刚生成，未确认，不可执行；
- `reviewed`：已审查，但尚未授权执行；
- `active`：当前允许执行；
- `executing`：正在执行；
- `done`：已完成；
- `blocked`：阻塞；
- `superseded`：已被新合同替代；
- `cancelled`：取消。

核心规则：

- 只有 `active` 合同可以执行。
- `draft` 不是执行授权。
- `reviewed` 不是执行授权。
- `pending` 不是执行授权。
- `done` 不得重复执行。
- `blocked` 必须先解决阻塞。
- `superseded` 不得继续执行。
- 未明确开启 batch mode 时，同一时间只能有一个 active 合同。

---

## 7. 批量执行规则

任务合同库可以保存 PR-01 到 PR-10 的多个合同。

但这不代表 AI 可以自动连续执行所有任务。

批量执行必须显式开启 batch mode。

开启 batch mode 时必须满足：

- 用户或项目负责人明确授权；
- 每个任务都有独立 CommandPack；
- 每个任务都有独立验收标准；
- 每个任务完成后必须运行门禁；
- 每个任务完成后必须输出独立 ExecutionReport section；
- 任一任务失败，立即 STOP；
- 不得跨任务顺手重构；
- 不得跳过 blocked 任务；
- 不得自动执行高风险任务。

---

## 8. CommandPack 生成检查清单

生成 CommandPack 前，规划层必须确认：

- 任务目标是否明确；
- 非目标是否明确；
- 用户语义边界是否清楚；
- 风险等级是否合理；
- 上下文读取层级是否合理；
- 是否需要 L1 / L2 / L3；
- 是否需要专项文档；
- 候选允许路径是否有来源；
- 候选禁止路径是否明确；
- 推断路径可信度是否标明；
- 是否需要文件定位阶段；
- 门禁命令是否明确；
- STOP 条件是否覆盖高风险区域；
- ExecutionReport 格式是否明确；
- 是否需要 Context Delta；
- 是否授权文档回写。
