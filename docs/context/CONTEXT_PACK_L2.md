# CONTEXT_PACK_L2：深入协作上下文

> 本文件用于保存比 L1 更详细的项目协作上下文。
>
> 适用于功能开发、模块修改、跨文件任务、阶段计划和中等复杂度任务。

## 1. 模块结构

```txt
docs/       # 给人阅读的框架文档
skills/     # 可导入执行环境的 Skill 包
templates/  # 可复制到用户项目的模板
scripts/    # 检查、初始化、验证脚本
examples/   # 示例项目骨架
```

## 2. 模块边界

- `docs/`：人类项目协作方法、集成指南、FAQ、案例说明。
- `skills/codex-ide-executor-zh/`：给 AI 执行代理使用的 Skill。
- `templates/`：用户可复制的项目模板。
- `scripts/`：通用脚本。
- `examples/`：示例骨架，不承载真实业务。

## 3. 当前阶段计划

- 持续完善规范体系。
- 增加真实案例。
- 增加英文文档。
- 增加 CI / Git Hook 示例。
- 增加更多技术栈模板。

## 4. 关键业务规则

- 不得删除核心文档、模板、Skill、脚本。
- 修改含中文文档时必须保持 UTF-8。
- 不得引入密钥、私有项目数据、真实客户信息。
- 不得把具体商业项目的敏感信息放进 examples。
- 不得把本项目宣传为"AI 全自动开发工具"。
- 本项目定位为 AI 工程协作规范套件。

## 5. 重要技术决策

- 采用 SKILL.md 作为路由型压缩执行器。
- 采用 CommandPack 作为任务合同。
- 采用 ExecutionReport 作为任务完成证据。
- 采用 ContextPack 分层结构（L1/L2/L3）管理项目长期上下文。

## 6. 常用命令与门禁

```bash
python scripts/check_utf8.py .
python scripts/validate_project_structure.py .
```

## 7. 近期 PR / 任务摘要

- v0.1.13：ContextPack 拆分为 L1/L2/L3 分层文件结构。
- v0.1.12：将工程概念基础文档重构为跨项目通用概念地图。
- v0.1.11：新增 AI 编程工程概念基础模块。
- v0.1.10：优化受控顺手修机制。

## 8. 已知问题与风险

- 示例项目骨架较简单，需要更多真实场景覆盖。
- 英文文档尚未完整。

## 9. 文档回写规则

- 重要变更后应同步更新 ContextPack 相关层级。
- 如果 CommandPack 未授权回写，在 ExecutionReport 中输出 Context Delta。
