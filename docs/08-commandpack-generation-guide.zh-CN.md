# CommandPack 生成指南

## 1. CommandPack 不是普通提示词

CommandPack 是任务合同。

它必须明确：

- 做什么
- 不做什么
- 允许改哪里
- 禁止改哪里
- 读哪些上下文
- 怎么执行
- 怎么验证
- 什么时候 STOP
- 怎么报告
- 怎么回滚
- 是否需要文档回写

## 2. 不同用户的输入来源

- **普通用户**：Task Intake
- **半懂代码用户**：Task Intake + 相关页面 / 文件线索
- **工程用户**：直接写 CommandPack
- **CLI / 插件**：从 Project Intake、Task Intake、目录扫描、package scripts 生成 CommandPack

生成者不必是特定 AI，可以是项目负责人、规划型 AI、CLI 或插件。

### 具体输入形式

CommandPack 可以来自：

- 用户自然语言描述
- Task Intake
- Project Intake
- issue
- bug report
- PRD
- screenshot
- error log
- ExecutionReport
- 项目负责人判断
- CLI / 插件扫描结果

## 3. 生成步骤

### Step 1：识别任务目标

把用户意图改写为明确目标。

### Step 2：识别非目标

明确本轮不做什么。

### Step 3：判断任务模式

判断 FAST / SAFE / AUDIT。

### Step 4：识别上下文

列出必须读取的项目资料、源码、测试。

如果当前窗口已经提供足够上下文，不重复读取。

### Step 5：确定允许路径和禁止路径

如果不知道，写"需执行代理先报告候选路径，不得直接修改"。

### Step 6：写具体任务步骤

步骤要可执行，不要空泛。

### Step 7：写门禁和验收标准

包括 lint、test、build、UTF-8、手动检查等。

### Step 8：写 STOP 条件

包含上下文不足、路径冲突、业务规则不清、密钥、生产配置、乱码风险等。

## ContextPack 读取策略

生成 CommandPack 时，应根据任务风险决定上下文读取范围：

- FAST：默认读取 `docs/CONTEXT_PACK.md` 的 L1。
- SAFE：读取 L1，必要时追加 `docs/context/CONTEXT_PACK_L2.md`。
- AUDIT：读取 L1 + L2 + L3，并补充专项文档。
- STOP：当任务需要 L3 但 L3 缺失或明显过期时，应先补上下文，不要直接执行。

### Step 9：判断 ContextPack 生命周期

生成 CommandPack 时，应判断：

1. 项目是否已有 ContextPack。
2. 当前任务是否需要先建立 L1。
3. 当前任务完成后是否会产生 Context Delta。
4. 是否授权执行代理更新 ContextPack。
5. 如果不授权，是否要求 ExecutionReport 输出待回写内容。

原则：

> 重要任务不只改代码，还要留下上下文痕迹。

### Step 10：写文档回写要求

判断是否影响长期上下文。

### Step 11：写 ExecutionReport 格式

要求 AI 输出证据。

## 4. 生成原则

- 不替用户发明业务规则。
- 不擅自扩大范围。
- 不把多个意图塞进一个任务。
- 不让执行代理猜产品方向。
- 不清楚就让执行代理 STOP。
- 高风险任务必须写清授权、验收、回滚。

## 使用 DOCS_MAP 辅助生成 CommandPack

当仓库文档较多时，规划层生成 CommandPack 前，可以先读取：

- `docs/DOCS_MAP.md`

用于判断：

- 本次任务应该读取哪些上下文；
- 是否需要 ContextPack L2 / L3；
- 是否需要 MODULE_BOUNDARY；
- 是否需要 TESTING；
- 是否需要历史记录或专项文档。

注意：DOCS_MAP 只帮助选择文档，不替代 CommandPack 本身。

## 5. 任务合同生成层

CommandPack 不应默认由普通用户手写。

推荐流程：

1. 用户填写 Task Intake。
2. 规划层读取必要上下文。
3. 规划层扫描项目结构。
4. 规划层进行语义边界映射。
5. 规划层生成 CommandPack 草案。
6. CommandPack 草案进入执行合同库，状态为 draft。
7. 人工或规划层审查后，将其中一个合同标记为 active。
8. 执行 Agent 只执行 active 合同。

生成 CommandPack 时，建议使用能力更强的模型，尤其是 SAFE / AUDIT 任务。

## 普通用户不知道路径怎么办？

普通用户不负责填写允许路径。

用户只负责说明：

- 想改什么；
- 不想影响什么；
- 最怕什么；
- 如何验收。

允许路径和禁止路径由规划层根据上下文推断，并由执行 Agent 在执行前验证。

## 6. 示例：从自然语言到 CommandPack

用户说：

> 帮我修一下导出 PDF 后中文乱码的问题。

生成者应补全：

- 任务目标：修复 PDF 导出中文乱码。
- 非目标：不改 UI、不改其他导出格式、不改 license。
- 模式：SAFE 或 AUDIT，视是否涉及导出核心模块。
- 必读：导出模块、字体处理、测试说明。
- 允许路径：export/pdf 相关模块。
- 禁止路径：license、payment、database、production config。
- 门禁：UTF-8 检查、导出测试、手动打开 PDF。
- STOP：如果需要改字体库依赖或导出格式 contract，先报告。
