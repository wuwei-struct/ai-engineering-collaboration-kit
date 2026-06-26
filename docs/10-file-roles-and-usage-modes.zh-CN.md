# 文件角色与使用模式

## 1. 核心原则

本套件文件很多，但不是所有文件都需要一开始使用。

最小运行时只需要：

1. `skills/codex-ide-executor-zh/SKILL.md`
2. 当前 `CommandPack`

其他文件都是按项目复杂度逐步加入。

---

## 2. 使用模式矩阵

| 模式 | 适合场景 | 必需文件 | 推荐文件 | 可选文件 |
|---|---|---|---|---|
| 最小模式 | 小项目、单次任务、快速验证 | `SKILL.md`、`CommandPack` | `TASK_INTAKE` | `.ai_rules.md`、`AGENTS.md` |
| 标准模式 | 普通项目、持续开发 | `SKILL.md`、`CommandPack` | `AGENTS.md`、`CONTEXT_PACK.md`、`TESTING.md` | `.ai_rules.md`、`MODULE_BOUNDARY.md` |
| 长期项目模式 | 多轮迭代、复杂项目 | `SKILL.md`、`CommandPack`、`CONTEXT_PACK.md` | `MODULE_BOUNDARY.md`、`PR_SUMMARIES.md`、`NEXT_PHASE_PLAN.md` | `.ai_rules.md`、`MANIFEST.md` |
| 审计 / 发布模式 | 发布、迁移、重构、交接 | `SKILL.md`、`CommandPack`、相关项目文档 | 完整规范、Release checklist、PR_SUMMARIES | RepoSense 输出、L3 ContextPack |

---

## 3. 文件角色速查

| 文件 | 角色 | 是否一开始必需 |
|---|---|---|
| `SKILL.md` | AI 压缩执行器 | 是 |
| `CommandPack` | 本次任务合同 | 是 |
| `TASK_INTAKE.md` | 普通用户任务意图表 | 推荐 |
| `PROJECT_INTAKE.md` | 项目初始化意图表 | 推荐 |
| `AGENTS.md` | 仓库级项目规则 | 标准模式推荐 |
| `.ai_rules.md` | 项目级规则摘要 / 未来工具生成物 | 可选 |
| `CONTEXT_PACK.md` | 项目长期上下文 | 持续项目推荐 |
| `MODULE_BOUNDARY.md` | 模块边界与防屎山文档 | 中大型项目推荐 |
| `TESTING.md` | 测试与门禁说明 | 持续项目推荐 |
| `PR_SUMMARIES.md` | 迭代历史 | 长期项目推荐 |
| `CHANGELOG.md` | 对外版本变化 | 发布时需要 |
| 完整执行规范 | 母版 / 审计 / 教学 / 维护 | 不作为日常运行输入 |

---

## 4. 普通用户从哪里开始

如果你不懂代码，只看：

1. `SELF_DIAGNOSIS.md`
2. `QUICK_START.md`
3. `templates/TASK_INTAKE.md.template`

不要一开始读完整规范。

如果对工程概念不熟悉（门禁、依赖、权限、幂等、schema、migration 等），先阅读：

- `docs/11-engineering-concepts-foundation.zh-CN.md`

---

## 5. 半懂代码用户从哪里开始

建议：

1. 填 `TASK_INTAKE`
2. 生成 `CommandPack`
3. 使用 `SKILL.md`
4. 按需补充 `AGENTS.md` / `CONTEXT_PACK.md`

---

## 6. 工程用户从哪里开始

建议：

1. 读 `README.md`
2. 读 `QUICK_START.md`
3. 使用 `templates/CommandPack.md.template`
4. 根据项目复杂度补 `AGENTS.md`、`CONTEXT_PACK.md`、`MODULE_BOUNDARY.md`、`TESTING.md`

---

## 7. `.ai_rules.md` 的定位

`.ai_rules.md` 不是所有用户都必须手写。

它更适合：

- CLI / 插件自动生成
- 中大型项目压缩项目规则
- 作为 `AGENTS.md` 和 ContextPack 的轻量摘要

手工使用时，可以先不创建 `.ai_rules.md`。

---

## 8. 一句话

先用最小模式跑起来。  
项目复杂了，再逐步补文档。  
不要一开始把所有文件都填满。
