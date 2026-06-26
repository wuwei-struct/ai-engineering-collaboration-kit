# CONTEXT_PACK_L3：审计 / 交接上下文

> 本文件用于保存长期、深层、审计级上下文。
>
> 适用于架构审查、权限/计费/数据库/迁移/生产配置等高风险任务，以及项目交接、发布前审计和长期维护。

## 1. 架构决策历史

- 采用 SKILL.md 路由型架构，SKILL.md 作为压缩执行器，完整规范独立维护。
- 采用 CommandPack + ExecutionReport 闭环，每次任务可追踪。
- 采用分层文档结构，按用户类型和项目阶段逐步引入文件。

## 2. 高风险模块说明

- `skills/codex-ide-executor-zh/SKILL.md`：核心执行路由，修改需充分验证。
- `scripts/`：门禁脚本，修改可能影响所有项目验证。
- 无计费、权限、数据库或生产配置模块。

## 3. 权限 / license / 计费 / 数据相关边界

- 本项目为开源规范套件，不涉及计费。
- 代码和文档分别使用独立许可证：LICENSE-CODE、LICENSE-DOCS。
- 不包含用户数据或生产配置。

## 4. 数据库 / schema / migration 记录

- 本项目不涉及数据库。

## 5. 发布 / 部署 / 回滚策略

- 发布到 GitHub，使用 git tag 标记版本。
- 回滚方式：`git revert` 到目标版本。
- 发布前必须通过 UTF-8 检查和项目结构验证。

## 6. 长期风险登记

- 示例项目与规范耦合度：示例可能随规范演进而需要同步更新。
- 模板兼容性：模板修改需向后兼容已有项目。

## 7. 历史重要事故 / 修复记录

- 无重大事故记录。

## 8. 交接说明

- 仓库结构见 MANIFEST.md。
- 规范入口：README.md、QUICK_START.md、USAGE.md。
- 核心 Skill：`skills/codex-ide-executor-zh/SKILL.md`。

## 9. 审计备注

- 首个可开源包。
- 发布前重点检查：文档完整性、UTF-8 无乱码、License 边界、模板可复制、Skill 细节完整。
