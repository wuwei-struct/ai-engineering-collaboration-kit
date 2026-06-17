# CommandPack 规范

CommandPack 是每次交给 AI 执行代码任务的“任务合同”。

它的目标是把模糊需求转成：

- 明确目标。
- 明确范围。
- 明确禁止事项。
- 明确上下文。
- 明确门禁。
- 明确回滚。
- 明确报告格式。

---

## 1. 必填字段

每个 CommandPack 至少包含：

- planId / iteration
- repoRoot
- base branch
- 执行模式：FAST / SAFE / AUDIT
- 任务目标
- 不做什么
- 必读上下文
- 允许修改路径
- 禁止修改路径
- 具体任务步骤
- UTF-8 / 中文防乱码要求
- anti-spaghetti 要求
- 必跑门禁
- 验收标准
- STOP 条件
- ExecutionReport 要求
- 回滚要求

---

## 2. 执行模式选择

- FAST：小 bug、小文案、小样式、单文件低风险修复。
- SAFE：普通 PR、功能开发、小模块开发、常规 bugfix。
- AUDIT：权限、license、计费、schema、生产配置、架构迁移、发布前检查。

默认 SAFE。  
触及核心规则自动 AUDIT。

---

## 3. 允许路径与禁止路径

允许路径应足够支撑模块化实现。

错误示例：

```md
允许修改：
- src/main.js
```

但任务实际需要新增 service / parser / builder。  
这会逼 AI 把新逻辑塞进中央大文件。

更好的写法：

```md
允许修改：
- src/main.js（仅 wiring）
- src/services/**
- src/parsers/**
- src/builders/**
- tests/**
```

---

## 4. STOP 条件

CommandPack 中必须写明：

- 上下文不足。
- 指令冲突。
- 允许路径不足。
- 中文乱码。
- 需要修改禁止路径。
- 需要访问密钥。
- 业务规则不清楚。
- 继续执行会制造屎山代码。

---

## 5. 最小模板

```md
# CommandPack：<任务名称>

## 0. 基本信息

- planId：
- iteration：
- repoRoot：
- base branch：
- 执行模式：FAST / SAFE / AUDIT

## 1. 任务目标

本次只完成：

-

不做：

-

## 2. 必读上下文

请先读取：

- AGENTS.md
- README.md
- docs/CONTEXT_PACK.md
- docs/MODULE_BOUNDARY.md
- docs/TESTING.md
- 与本任务相关源码

如果上下文缺失，请停止并报告。

## 3. 允许修改路径

允许修改：

-

## 4. 禁止修改路径

禁止修改：

-

## 5. 具体任务步骤

1.
2.
3.

## 6. UTF-8 / 中文防乱码要求

- 所有文件保持 UTF-8。
- 修改含中文文件必须显式指定编码。
- 一旦发现乱码，立即 STOP。

## 7. anti-spaghetti 要求

- 不得把新业务逻辑塞进中央大文件。
- 如需新增模块，应放到合适目录。
- 如果允许路径不足，应 STOP 并报告。

## 8. 必跑门禁

-

## 9. 验收标准

-

## 10. STOP 条件

-

## 11. ExecutionReport

完成后输出：
- 目标
- 修改文件
- 范围遵守情况
- 测试/门禁
- 风险
- 回滚方式
- 下一步建议
```
