# TESTING

## 普通 PR 必跑

```bash
npm test
```

## 涉及中文文件必跑

```bash
python scripts/check_utf8.py .
```

## 说明

该示例项目没有 lint/typecheck/build 门禁。
