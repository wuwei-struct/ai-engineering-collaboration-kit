# TESTING

## 必跑

```bash
python scripts/check_utf8.py .
```

## 修改结构后运行

```bash
python scripts/validate_project_structure.py .
```

## 发布前检查

- README 可读。
- SELF_DIAGNOSIS 可读。
- QUICK_START 可执行。
- docs/02-agent-execution-spec.zh-CN.md 与 Skill 内容一致。
- templates 齐全。
- scripts 可运行。
- examples 不含敏感信息。
