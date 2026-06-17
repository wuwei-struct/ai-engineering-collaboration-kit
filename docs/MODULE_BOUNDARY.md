# MODULE_BOUNDARY

## docs/

承载给人阅读的框架文档。

不得把工具脚本放入 docs。

## skills/

承载给 AI 执行代理使用的 Skill 包。

`skills/codex-ide-executor-zh/SKILL.md` 必须保持可独立使用，不能依赖外部聊天上下文。

## templates/

承载可复制到用户项目中的模板。

模板应保持通用，不写入本用户的私有项目路径或敏感信息。

## scripts/

承载通用脚本。

脚本应可独立运行，不依赖私有环境。

## examples/

承载示例项目骨架。

示例只展示协作结构，不包含真实业务敏感信息。
