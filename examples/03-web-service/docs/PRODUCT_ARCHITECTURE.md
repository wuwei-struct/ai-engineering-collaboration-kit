# PRODUCT_ARCHITECTURE

## 分层

- route：路由接线。
- controller：请求响应适配。
- service：业务规则。
- repository：数据访问。
- schema：输入输出结构。

## 禁止

- route 中不得写业务逻辑。
- controller 中不得写复杂业务规则。
- service 不得直接依赖 HTTP 框架对象。
- repository 不得处理 UI 或业务展示逻辑。
