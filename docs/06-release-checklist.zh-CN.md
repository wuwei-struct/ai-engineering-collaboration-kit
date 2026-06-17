# 发布前检查清单

本清单用于将一个采用 AI Engineering Collaboration Kit 的项目推进到可发布状态。

---

## 1. 文档检查

- [ ] README.md 已说明项目定位、运行方式、当前版本。
- [ ] AGENTS.md 已说明仓库规则、禁止事项、门禁、报告要求。
- [ ] docs/CONTEXT_PACK.md 已更新到当前状态。
- [ ] docs/MODULE_BOUNDARY.md 已记录关键模块边界。
- [ ] docs/TESTING.md 已说明必跑门禁。
- [ ] docs/PR_SUMMARIES.md 已记录最近重要变更。
- [ ] docs/NEXT_PHASE_PLAN.md 已说明发布后下一步。
- [ ] 代码变更对应的文档已同步更新。

---

## 2. 编码和中文检查

- [ ] `.editorconfig` 存在。
- [ ] `.gitattributes` 存在。
- [ ] 中文 Markdown / JSON / UI 文案保持 UTF-8。
- [ ] 已运行 `python scripts/check_utf8.py .` 或等效检查。
- [ ] diff 中没有异常乱码或 mojibake。
- [ ] 没有复制乱码上下文继续修改。

---

## 3. 代码结构检查

- [ ] 新业务逻辑没有继续塞进中央大文件。
- [ ] `main.js` / `index.js` / `App.tsx` / `styles.css` 等入口文件未异常膨胀。
- [ ] 新能力已放入合适模块。
- [ ] 没有无关重构。
- [ ] 没有大范围格式化。
- [ ] 没有复制粘贴扩散相同逻辑。
- [ ] 关键模块边界仍然清晰。

---

## 4. 安全检查

- [ ] 没有提交 `.env`。
- [ ] 没有提交密钥、token、cookie、private key。
- [ ] 没有打印或记录完整密钥。
- [ ] 没有未授权修改生产配置。
- [ ] 没有未授权修改 license / 权限 / 计费逻辑。
- [ ] 没有提交构建缓存、日志、临时文件。

---

## 5. 门禁检查

根据项目实际情况运行：

- [ ] lint
- [ ] typecheck
- [ ] test
- [ ] build
- [ ] contentCheck
- [ ] UTF-8 check
- [ ] smoke test
- [ ] export/import test
- [ ] license/permission test
- [ ] CI 通过或失败原因已记录

如果某个门禁无法运行，必须说明原因和后续运行命令。

---

## 6. Git 与回滚

- [ ] `git status --short` 已检查。
- [ ] `git diff` 已审查。
- [ ] 未提交无关文件。
- [ ] 未提交构建产物。
- [ ] 已创建发布前 commit。
- [ ] 已创建发布 tag。
- [ ] 已记录回滚方式。
- [ ] 必要时已创建本地备份。

---

## 7. ExecutionReport 检查

发布前最后一次 AI 执行报告应包含：

- [ ] 目标。
- [ ] 修改文件。
- [ ] 范围遵守情况。
- [ ] UTF-8 / 中文检查。
- [ ] anti-spaghetti 检查。
- [ ] 门禁结果。
- [ ] 未执行检查及原因。
- [ ] 风险与兼容性。
- [ ] 回滚方式。
- [ ] 下一步建议。
- [ ] 规则沉淀建议。

---

## 8. 发布判断

只有满足以下条件，才建议发布：

- 文档与代码一致。
- 门禁通过或失败原因可接受。
- 无乱码。
- 无密钥泄漏。
- 无超范围改动。
- 有清晰回滚方式。
- 发布后下一步明确。

发布前不要再做大重构。
