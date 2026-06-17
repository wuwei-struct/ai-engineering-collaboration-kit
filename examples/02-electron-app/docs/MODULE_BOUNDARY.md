# MODULE_BOUNDARY

## 中央入口文件

- `src/main/main.js`：只做 app lifecycle / window / IPC wiring。
- `src/preload/preload.js`：只做安全桥接。
- `src/renderer/App.js`：只做 renderer 入口。

## 新能力位置

- 业务服务：`src/services/`
- IPC 契约：`src/ipc/`
- 页面视图：`src/renderer/views/`
- UI 组件：`src/renderer/components/`

如果任务需要新增业务能力，但只允许修改 `main.js`，必须 STOP。
