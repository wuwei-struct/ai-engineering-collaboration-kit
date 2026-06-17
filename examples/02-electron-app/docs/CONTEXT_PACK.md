# CONTEXT_PACK

## L1：最小可用上下文

### 项目定位

Electron 应用骨架示例。

### 当前状态

仅有文档和目录骨架，未实现真实业务。

### 主要目录

```txt
src/main/
src/preload/
src/renderer/
src/services/
src/ipc/
```

### 禁止事项

- 不要把业务逻辑写进 main / preload。
- 不要修改生产配置。
- 不要引入依赖，除非任务明确要求。
