# CONTEXT_PACK

## L1：最小可用上下文

### 项目定位

演示用 Node CLI。输入名字，输出问候语。

### 当前状态

- 已有 CLI 入口：`src/cli.js`
- 已有业务函数：`src/greet.js`
- 已有测试：`tests/greet.test.js`

### 主要目录

```txt
src/
  cli.js      # CLI 入口，只做参数读取和输出
  greet.js    # 问候语业务逻辑
tests/
  greet.test.js
```

### 常用命令

```bash
npm test
python scripts/check_utf8.py .
```

### 禁止事项

- 不要把业务逻辑继续堆进 `src/cli.js`。
- 不要引入依赖，除非任务明确要求。
- 不要修改 package 配置，除非任务明确要求。
