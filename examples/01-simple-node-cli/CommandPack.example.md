# CommandPack：给 greet 增加中文问候选项

## 0. 基本信息

- 执行模式：SAFE

## 1. 任务目标

新增一个可选参数，让 `greet(name, locale)` 在 `locale === "zh-CN"` 时返回 `你好，<name>！`。

不做：

- 不改 CLI 参数解析。
- 不引入依赖。
- 不重构项目结构。

## 2. 必读上下文

- AGENTS.md
- README.md
- docs/CONTEXT_PACK.md
- docs/MODULE_BOUNDARY.md
- docs/TESTING.md
- src/greet.js
- tests/greet.test.js

## 3. 允许修改路径

- src/greet.js
- tests/greet.test.js

## 4. 禁止修改路径

- src/cli.js
- package.json

## 5. 必跑门禁

- npm test
- python scripts/check_utf8.py .

## 6. STOP 条件

- 需要修改 CLI 入口。
- 需要引入依赖。
- 中文乱码。
