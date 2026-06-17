# AGENTS.md

## 项目概况

本项目是：`一个演示用 Node CLI 项目`。

当前阶段：`骨架期`。

## 仓库结构

```txt
<填写主要目录结构>
```

示例：

```txt
src/
  main/
  renderer/
  services/
  schemas/
  components/
docs/
scripts/
tests/
```

## 常用命令

安装依赖：

```bash
<填写命令>
```

本地开发：

```bash
<填写命令>
```

测试：

```bash
<填写命令>
```

构建：

```bash
<填写命令>
```

UTF-8 检查：

```bash
python scripts/check_utf8.py .
```

## 修改规则

- 当前任务合同 / CommandPack 优先。
- 一次任务只完成一个明确意图。
- 不得顺手重构。
- 不得顺手改 UI。
- 不得顺手升级依赖。
- 不得格式化全仓库。
- 不得修改未授权路径。
- 不得提交构建产物、缓存、日志、`node_modules`、`dist`。
- 不得读取、打印、提交密钥。
- 不得随意修改 `.env`、生产配置、license key、凭证。

## UTF-8 / 中文防乱码规则

- 所有文件默认 UTF-8。
- 修改含中文文件时必须显式指定编码。
- Python 使用 `encoding="utf-8"`。
- Node fs read/write 使用 `"utf8"`。
- PowerShell 使用 PowerShell 7，并使用 `-Encoding utf8`。
- 一旦发现中文乱码、mojibake、异常字符，必须 STOP。
- 不得复制乱码上下文继续修改。
- 涉及中文文件时应运行 `python scripts/check_utf8.py .`。

## 模块边界

以下文件只允许做 wiring / 初始化 / 路由接线 / 兼容委托 / 简单入口：

- `<填写入口文件，例如 src/main.js>`
- `<填写入口文件，例如 src/App.tsx>`
- `<填写入口文件，例如 src/styles.css>`

不得继续向这些文件新增大段业务逻辑。

新业务逻辑应优先放入：

- `src/services/`
- `src/schemas/`
- `src/parsers/`
- `src/builders/`
- `src/components/`
- `src/views/`
- `src/stores/`
- `src/validators/`
- `src/exporters/`
- `<按项目实际补充>`

如果当前允许修改路径不足，会导致新逻辑被迫塞进中央大文件，必须 STOP 并报告。

## 执行模式

默认使用 SAFE MODE。

- FAST：小 bug、小文案、小样式、低风险单文件修复。
- SAFE：普通 PR、功能开发、小模块开发、常规 bugfix。
- AUDIT：权限、license、计费、schema、生产配置、架构迁移、发布前检查。

触及权限、license、计费、schema、生产配置、密钥、安全逻辑时，必须自动升级为 AUDIT MODE。

## 上下文读取

修改代码前优先读取：

- `AGENTS.md`
- `README.md`
- `docs/CONTEXT_PACK.md`
- `docs/MODULE_BOUNDARY.md`
- `docs/TESTING.md`
- 与本次任务相关源码
- 与本次任务相关测试

如果上下文不足，必须 STOP 并报告。

## 门禁要求

普通任务建议运行：

```bash
npm run lint --if-present
npm run typecheck --if-present
npm test
```

涉及中文文件时运行：

```bash
python scripts/check_utf8.py .
```

发布前运行：

```bash
npm run build --if-present
```

如果无法运行某个门禁，必须说明原因，并给出应后续运行的命令。

## STOP 条件

遇到以下情况必须停止并报告：

- 指令冲突。
- 上下文不足。
- 允许路径不足。
- 需要修改禁止路径。
- 中文乱码。
- 编码不明。
- 需要访问密钥。
- 业务规则不清楚。
- 继续执行会制造屎山代码。
- 任务触及权限、license、计费、schema、生产配置但未明确授权。

## ExecutionReport 要求

任务完成后必须输出：

- 目标。
- 执行模式。
- 修改文件。
- 范围遵守情况。
- 关键实现说明。
- UTF-8 / 中文检查。
- anti-spaghetti 检查。
- 执行的测试 / 门禁。
- 未执行检查及原因。
- 风险与兼容性。
- 回滚方式。
- 下一步建议。
