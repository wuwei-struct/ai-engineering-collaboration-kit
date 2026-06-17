# PRODUCT_ARCHITECTURE

## 组成

- 人类手册：项目怎么开始、怎么迭代、怎么审查。
- AI 执行规范：执行代理如何读取上下文、锁范围、跑门禁。
- 模板：AGENTS、CommandPack、ContextPack、ModuleBoundary、Testing。
- 脚本：UTF-8 检查、项目结构验证、项目骨架初始化。
- 示例：不同项目类型的文档骨架。

## 关键闭环

```txt
人定义目标 -> CommandPack -> AI 按 Skill 执行 -> ExecutionReport -> 人审查 -> 文档沉淀
```
