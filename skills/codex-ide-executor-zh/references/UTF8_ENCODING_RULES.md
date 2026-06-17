# UTF-8 / 中文防乱码规则

所有项目默认 UTF-8。

修改任何含中文内容的文件时，必须显式保证 UTF-8。

---

## 1. 必须遵守

Python：

```python
Path("file.md").read_text(encoding="utf-8")
Path("file.md").write_text(content, encoding="utf-8")
```

Node.js：

```js
fs.readFileSync(file, "utf8")
fs.writeFileSync(file, content, "utf8")
```

PowerShell：

```powershell
Set-Content -Path file.md -Value $content -Encoding utf8
```

---

## 2. 禁止行为

禁止：

- 未指定编码的脚本写中文文件。
- 旧 PowerShell 5.1 默认编码写入中文文件。
- 不安全 shell 重定向覆盖中文文件。
- 复制乱码上下文继续修改。
- 在编码不明时批量替换中文。
- diff 中出现大量无关中文变化还继续编辑。

---

## 3. STOP 条件

发现以下情况必须停止：

- 中文乱码。
- mojibake。
- 异常字符。
- 文件编码不明。
- 中文 diff 大面积变化。
- 文案中出现不可解释的问号或替换字符。

---

## 4. 建议配置

`.editorconfig`：

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

`.gitattributes`：

```gitattributes
* text=auto eol=lf
*.md text working-tree-encoding=UTF-8
*.json text working-tree-encoding=UTF-8
*.js text working-tree-encoding=UTF-8
*.ts text working-tree-encoding=UTF-8
*.tsx text working-tree-encoding=UTF-8
*.html text working-tree-encoding=UTF-8
*.css text working-tree-encoding=UTF-8
```

---

## 5. 门禁

推荐运行：

```bash
python scripts/check_utf8.py .
```
