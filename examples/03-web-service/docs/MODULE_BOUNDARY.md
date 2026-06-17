# MODULE_BOUNDARY

## 路由层

`src/routes/` 只做 URL 与 controller 绑定。

## Controller 层

`src/controllers/` 只做请求解析、响应格式化和错误适配。

## Service 层

`src/services/` 承载业务规则。

## Repository 层

`src/repositories/` 承载数据访问。

## Schema 层

`src/schemas/` 定义输入输出结构。

跨层规则：

- route 不得直接调用 repository。
- controller 不得写复杂业务规则。
- service 不得依赖 HTTP request/response 对象。
