# Example 01：Simple Node CLI

这是一个最小 Node CLI 项目骨架，用来展示如何为小型项目建立 AI 协作文档。

## 项目定位

一个演示用 CLI：输入名字，输出问候语。

## 运行

```bash
node src/cli.js Wuwei
```

## 测试

```bash
node tests/greet.test.js
```

## AI 协作重点

- `src/cli.js` 只做命令行入口。
- `src/greet.js` 放业务逻辑。
- 新功能不要继续堆进 `cli.js`。
- 修改中文文案时运行 `python scripts/check_utf8.py .`。
