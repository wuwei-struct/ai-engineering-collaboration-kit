# Example 02：Electron App Skeleton

这是一个 Electron 桌面应用的 AI 协作文档骨架示例。

## 项目定位

演示如何为 Electron 项目定义 main / preload / renderer 边界，防止 AI 把业务逻辑都塞进 `main.js` 或 `preload.js`。

## 重点

- `src/main/main.js` 只做窗口创建、应用生命周期和 IPC wiring。
- `src/preload/preload.js` 只暴露安全桥接 API。
- `src/renderer/` 承载页面视图。
- `src/services/` 承载业务服务。
- `src/ipc/` 定义 IPC contract。
