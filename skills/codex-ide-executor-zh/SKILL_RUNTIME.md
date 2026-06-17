# Codex/IDE 执行规范 Runtime 摘要

> 本文件是 `SKILL.md` 的可选短摘要。
>
> 日常任务优先使用：
>
> 1. 当前 CommandPack
> 2. `SKILL.md`
>
> 本文件仅在工具需要更短执行规则文本时使用。
> 完整规范默认不进入 AI 运行时上下文。

## 0. 读取原则

完整执行规范是源规范 / 审计依据，不要求每次任务完整读取。

日常任务最小输入：

1. 当前 CommandPack
2. `SKILL.md` 或本 Runtime 摘要

项目资料按需读取：

- `.ai_rules.md`
- `AGENTS.md`
- `docs/CONTEXT_PACK.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 相关源码和测试

完整规范用于人类维护、审计、复盘和规范修改，不用于 AI 日常继续执行。

---

## 1. 模式判断

### FAST MODE

适用于小文案、小样式、单文件低风险改动。

读取：

- CommandPack
- 当前相关文件
- `.ai_rules.md` / `AGENTS.md`，按需

### SAFE MODE

适用于普通功能、普通 bugfix、小模块开发。

读取：

- CommandPack
- `.ai_rules.md` / `AGENTS.md`，按需
- `docs/CONTEXT_PACK.md` L1
- `docs/MODULE_BOUNDARY.md` 相关部分
- 相关源码和测试

### AUDIT MODE

适用于架构、权限、license、计费、schema、生产配置、跨模块重构、安全风险任务。

高风险、冲突、规则不明确时，优先 STOP，要求更明确的 CommandPack 或人工确认。

完整规范用于人类维护、审计、复盘和规范修改，不用于 AI 日常继续执行。

读取：

- CommandPack
- `.ai_rules.md` / `AGENTS.md`，按需
- `docs/CONTEXT_PACK.md` L2/L3
- `docs/PRODUCT_ARCHITECTURE.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`

---

## 2. 硬规则

- 当前任务合同优先。
- 不扩大范围。
- 不顺手重构。
- 不顺手升级依赖。
- 不顺手改业务逻辑。
- 不修改禁止路径。
- 不触碰密钥、`.env`、生产配置。
- 不把新逻辑塞进中央大文件。
- 中文文件必须保持 UTF-8。
- 没有验证证据，不得声称成功。

---

## 3. STOP 条件

遇到以下情况必须停止并报告：

- 上下文不足
- 指令冲突
- 允许路径不足
- 需要修改禁止路径
- 需要访问密钥
- 中文乱码 / mojibake
- 业务规则不清楚
- 任务混杂多个高风险意图
- 继续执行会制造屎山代码
- 需要扩大范围

---

## 4. UTF-8 / 中文防乱码

- Python 使用 `encoding="utf-8"`
- Node fs 读写使用 `"utf8"`
- PowerShell 使用 PowerShell 7 和 `-Encoding utf8`
- 不使用可能改变编码的 shell 重定向覆盖中文文件
- 发现乱码立即 STOP

---

## 5. anti-spaghetti code

不要继续把新功能堆进：

- `main.js`
- `index.js`
- `App.tsx`
- `renderer.ts`
- `preload.ts`
- `styles.css`
- `global.css`
- 巨大 service / utils / store / component 文件

新功能优先放入：

- services
- schemas
- parsers
- builders
- adapters
- validators
- exporters
- components
- views
- stores

如果允许路径过窄，导致只能把逻辑塞进中央大文件，必须 STOP。

---

## 6. 受控小修

允许处理小而同类、局部可测的问题。

边界：

- 单文件通常不超过 20 行
- 跨文件通常不超过 3 个文件
- 不改 API contract
- 不改 schema
- 不改权限 / license / 计费
- 不改生产配置
- 不新增依赖
- 不新增公共导出

超出边界，写入下一步建议或 STOP。

---

## 7. 必跑门禁

按项目规则运行：

- lint
- typecheck
- test
- build
- UTF-8 check
- contentCheck

无法运行必须说明原因。

---

## 7.5. 文档回写

任务完成前，检查本次变更是否影响项目长期上下文。

如果影响项目说明、执行规则、上下文状态、模块边界、测试门禁、阶段计划、版本记录或文件清单，应按当前项目文档体系同步更新。

如果当前任务不允许修改文档，不要扩大范围。
在 ExecutionReport 中标记"需要文档回写"，并说明建议写入位置和内容。

---

## 8. 输出要求

每次任务结束必须输出 ExecutionReport，至少包含：

- 目标
- 执行模式
- 修改文件
- 范围遵守情况
- UTF-8 / 中文检查
- anti-spaghetti 检查
- 执行的测试 / 门禁
- 未执行检查及原因
- 风险
- 回滚方式
- 下一步建议
