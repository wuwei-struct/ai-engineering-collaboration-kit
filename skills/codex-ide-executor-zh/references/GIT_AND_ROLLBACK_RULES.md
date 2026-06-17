# Git 与回滚规则

## 1. 执行前建议检查

```bash
git branch --show-current
git rev-parse --short HEAD
git status --short
```

如果任务要求干净工作区，但当前不干净，必须 STOP 并报告。

---

## 2. 提交前检查

```bash
git diff
git status --short
```

不得提交：

- 密钥。
- `.env`。
- 构建产物。
- `node_modules`。
- `dist`。
- 缓存文件。
- 临时文件。
- 无关格式化。
- 无关大改。
- 乱码文件。

---

## 3. 破坏性命令限制

未经明确授权，不得执行：

```bash
git reset --hard
git clean -fd
git push --force
```

可以在 ExecutionReport 中给出回滚建议，但不要擅自执行破坏性命令。

---

## 4. 回滚说明示例

```bash
git restore <file>
git restore .
git revert <commit>
```

如果本次修改涉及多个文件，应列出可回滚文件和风险。
