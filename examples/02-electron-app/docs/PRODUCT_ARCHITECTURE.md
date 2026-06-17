# PRODUCT_ARCHITECTURE

## 进程边界

- main：应用生命周期、窗口、IPC wiring。
- preload：安全桥接。
- renderer：用户界面。
- services：业务服务。
- ipc：契约与通道定义。

## 禁止

- 不得在 main 中写业务逻辑。
- 不得在 preload 中暴露不安全对象。
- 不得让 renderer 直接访问 Node 能力。
