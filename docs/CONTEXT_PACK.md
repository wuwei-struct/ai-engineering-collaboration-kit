# CONTEXT_PACK

## L1：最小可用上下文

### 项目定位

AI Engineering Collaboration Kit 是一套 AI 工程协作规范套件，帮助开发者用仓库文档、CommandPack、Skill、门禁和 ExecutionReport 管理 AI 编程。

### 当前版本

v0.1.0，中文首发版。

### 主要目录

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

### 当前重点

保证开源仓库包完整、可读、可复制、无中文乱码。

### 禁止事项

- 不要加入敏感数据。
- 不要把项目宣传为全自动开发。
- 不要破坏模板和 Skill 的对应关系。

## L2：深入协作上下文

### 核心内容

- 给人的项目协作手册。
- 给 AI 的执行规范 Skill v1.2。
- 项目模板。
- UTF-8 检查脚本。
- 示例项目骨架。

### 已知后续方向

- 增加真实案例。
- 增加英文文档。
- 增加 CI / Git Hook 示例。
- 增加更多技术栈模板。

## L3：审计交接上下文

当前为首个可开源包。发布前重点检查：

- 文档完整性。
- UTF-8 无乱码。
- License 边界。
- 模板可复制。
- Skill v1.2 细节完整。
