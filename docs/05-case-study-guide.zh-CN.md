# 案例分析指南

本文件用于说明如何为本框架补充真实或示例案例。

一个好案例不只是展示“用了哪些模板”，而是展示：

> 项目从混乱到有上下文、有边界、有门禁、有回滚的变化过程。

---

## 1. 推荐案例结构

每个案例建议包含：

```txt
case-name/
  README.md
  before/
    structure.txt
    problems.md
  after/
    AGENTS.md
    docs/
      CONTEXT_PACK.md
      MODULE_BOUNDARY.md
      TESTING.md
      PR_SUMMARIES.md
  CommandPack.example.md
  ExecutionReport.example.md
  lessons-learned.md
```

---

## 2. 案例应该回答的问题

### 项目背景

- 项目是什么？
- 技术栈是什么？
- AI 在项目中承担什么角色？
- 项目规模大概多大？

### 原始问题

- AI 是否乱改文件？
- 是否经常上下文断裂？
- 是否有中央大文件膨胀？
- 是否有中文乱码？
- 是否缺测试门禁？
- 是否没有回滚方式？

### 采用的框架部分

- 是否新增 AGENTS.md？
- 是否新增 ContextPack？
- 是否新增 ModuleBoundary？
- 是否新增 Testing？
- 是否使用 CommandPack？
- 是否要求 ExecutionReport？

### 改进结果

- AI 是否更少越界？
- diff 是否更容易审查？
- 中文乱码是否减少？
- 是否更容易判断任务完成？
- 是否更容易交接给下一轮 AI？

### 仍然存在的问题

- 哪些规范仍然不够？
- 哪些任务仍需人工判断？
- 哪些门禁需要补充？
- 哪些文档需要维护成本？

---

## 3. before / after 对比重点

推荐对比：

| 维度 | Before | After |
|---|---|---|
| 上下文 | 靠聊天记录 | ContextPack |
| 仓库规则 | 没有 | AGENTS.md |
| 模块边界 | 模糊 | MODULE_BOUNDARY.md |
| 任务输入 | 口头描述 | CommandPack |
| 结果输出 | “完成了” | ExecutionReport |
| 测试门禁 | 不固定 | TESTING.md |
| 中文编码 | 经常风险 | UTF-8 检查 |
| 回滚方式 | 不清楚 | rollback notes |

---

## 4. 案例写作模板

```md
# 案例：<项目名>

## 项目背景

-

## Before：原始问题

-

## 引入的规范

-

## 关键模板

- AGENTS.md：
- CONTEXT_PACK.md：
- MODULE_BOUNDARY.md：
- TESTING.md：
- CommandPack：

## 一次真实任务

### 任务目标

-

### CommandPack 摘要

-

### ExecutionReport 摘要

-

## After：效果

-

## 经验

-

## 仍需改进

-
```

---

## 5. 隐私和安全

提交真实案例时，必须移除：

- 密钥。
- 用户数据。
- 公司内部接口。
- 私有业务规则。
- 客户名称。
- 不应公开的商业信息。

如果不确定是否可以公开，先做抽象化案例。

---

## 6. 当前示例

本仓库提供三个基础骨架：

- `examples/01-simple-node-cli/`
- `examples/02-electron-app/`
- `examples/03-web-service/`

这些不是完整产品，而是展示如何组织 AI 协作相关文档。
