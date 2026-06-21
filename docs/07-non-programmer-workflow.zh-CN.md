# 非程序员如何使用本套件

## 1. 不需要直接写 CommandPack

CommandPack 是工程任务合同，不适合要求所有用户手写。

非程序员只需要先描述：

- 想做什么
- 当前问题是什么
- 希望完成后是什么效果
- 哪些地方不能动
- 有哪些截图 / 报错 / 反馈
- 如何验收

这些内容可以写进 `templates/TASK_INTAKE.md.template`。

## 2. 不需要从零写 ContextPack

ContextPack 是项目上下文压缩包。

非程序员不需要直接写 ContextPack。

- `PROJECT_INTAKE` 可用于生成初始 ContextPack。
- 每次重要任务后，由上游规划者或执行代理给出 Context Delta。
- 用户只需要确认"当前状态是否记录正确"。

普通用户可以先填写 `templates/PROJECT_INTAKE.md.template`，后续由项目负责人、规划型 AI、CLI 或插件生成初始 ContextPack。

## 3. 推荐流程

1. 用户填写 Task Intake。
2. 上游规划者生成 CommandPack。
3. 代码执行代理读取 `CommandPack + SKILL.md`。
4. AI 执行任务。
5. AI 输出 ExecutionReport。
6. 用户或项目负责人审查结果。
7. 必要时回写项目文档。

## 4. 三类用户路径

### 完全不懂代码

使用：

- 截图
- 报错
- 目标描述
- Task Intake

由上游规划者生成 CommandPack。

### 半懂代码

可以补充：

- 页面路径
- 功能名称
- 可能相关文件
- 不想改的范围

### 懂代码

可以直接写 CommandPack。

## 5. 用户仍然要负责什么

本套件不能替代：

- 产品判断
- 客户理解
- 市场验证
- 功能优先级
- 验收标准
- 风险取舍

## 6. 一句话

用户不写工程合同。  
用户描述意图。  
上游规划者生成 CommandPack。  
AI 执行代理按 Skill 执行。
