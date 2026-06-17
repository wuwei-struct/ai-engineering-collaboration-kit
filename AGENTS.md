# AGENTS.md

## 项目概况

本仓库是 AI Engineering Collaboration Kit / AI 工程协作规范套件，用于沉淀 AI 编程中的项目协作手册、执行规范、模板、脚本和示例。

## 仓库结构

```txt
docs/       # 给人阅读的框架文档
skills/     # 可导入执行环境的 Skill 包
templates/  # 可复制到用户项目的模板
scripts/    # 检查、初始化、验证脚本
examples/   # 示例项目骨架
```

## 常用命令

UTF-8 检查：

```bash
python scripts/check_utf8.py .
```

项目结构检查：

```bash
python scripts/validate_project_structure.py .
```

## 修改规则

- 不得删除核心文档、模板、Skill、脚本。
- 修改含中文文档时必须保持 UTF-8。
- 不得引入密钥、私有项目数据、真实客户信息。
- 不得把具体商业项目的敏感信息放进 examples。
- 不得把本项目宣传为“AI 全自动开发工具”。
- 本项目定位为 AI 工程协作规范套件。

## 模块边界

- `docs/`：人类项目协作方法、集成指南、FAQ、案例说明。
- `skills/codex-ide-executor-zh/`：给 AI 执行代理使用的 Skill。
- `templates/`：用户可复制的项目模板。
- `scripts/`：通用脚本。
- `examples/`：示例骨架，不承载真实业务。

## 门禁要求

修改后至少运行：

```bash
python scripts/check_utf8.py .
```

如果修改了仓库结构，运行：

```bash
python scripts/validate_project_structure.py .
```

## ExecutionReport 要求

任何代码或文档批量修改完成后，应说明：

- 修改文件。
- 是否保持 UTF-8。
- 是否影响 Skill / 模板 / 脚本。
- 是否运行检查。
- 风险与回滚方式。
