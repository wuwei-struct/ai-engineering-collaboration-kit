# CONTEXT_PACK

> 本文件是 AI 进入项目时的上下文入口。
>
> 默认只保留 L1：最小可用上下文。
> 更详细的 L2 / L3 上下文已拆分到 `docs/context/` 目录。

## 0. 上下文读取规则

- 普通任务：读取本文件即可。
- 中等复杂任务：读取本文件 + `docs/context/CONTEXT_PACK_L2.md`。
- 高风险 / 架构 / 权限 / 计费 / 数据库 / 迁移 / 发布 / 审计任务：读取本文件 + L2 + `docs/context/CONTEXT_PACK_L3.md`。
- 不要默认读取全部上下文。
- 由当前 CommandPack 决定最终读取范围。

## 1. L1：最小可用上下文

### 项目定位

AI Engineering Collaboration Kit 是一套 AI 工程协作规范套件，帮助开发者用仓库文档、CommandPack、Skill、门禁和 ExecutionReport 管理 AI 编程。

### 当前状态

v0.1.13，中文首发版持续迭代中。

### 当前阶段目标

保证开源仓库包完整、可读、可复制、无中文乱码，持续完善规范体系。

### 核心目录 / 文件

```txt
docs/
skills/
templates/
scripts/
examples/
```

### 常用命令

```bash
python scripts/check_utf8.py .
python scripts/validate_project_structure.py .
```

### 当前禁止事项

- 不要加入敏感数据。
- 不要把项目宣传为全自动开发。
- 不要破坏模板和 Skill 的对应关系。

### 最近重要变化

- v0.1.13：ContextPack 拆分为 L1/L2/L3 分层文件结构。

## 2. L2 / L3 索引

- L2 深入协作上下文：`docs/context/CONTEXT_PACK_L2.md`
- L3 审计 / 交接上下文：`docs/context/CONTEXT_PACK_L3.md`

## 3. Context Delta 入口

重要任务完成后，应在 ExecutionReport 中输出 Context Delta。

如果 CommandPack 授权文档回写，则同步更新：

- 本文件的 L1 当前状态；
- `docs/context/CONTEXT_PACK_L2.md` 的模块 / 决策 / 任务上下文；
- `docs/context/CONTEXT_PACK_L3.md` 的审计 / 风险 / 交接上下文。
