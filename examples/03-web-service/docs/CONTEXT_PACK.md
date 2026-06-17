# CONTEXT_PACK

## L1：最小可用上下文

### 项目定位

Web Service 骨架示例。

### 当前状态

仅有分层目录和文档，无真实服务实现。

### 主要目录

```txt
src/routes/
src/controllers/
src/services/
src/repositories/
src/schemas/
```

### 禁止事项

- 不要把业务逻辑写在 route。
- 不要在 controller 中直接访问数据库。
- 不要引入依赖，除非任务明确要求。
