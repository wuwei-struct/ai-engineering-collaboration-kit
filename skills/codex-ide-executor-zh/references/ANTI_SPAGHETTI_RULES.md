# anti-spaghetti code 防屎山规则

## 1. 中央大文件规则

以下文件只允许做 wiring、初始化、路由接线、兼容委托、简单入口：

- `main.js`
- `index.js`
- `App.tsx`
- `renderer.ts`
- `preload.ts`
- `styles.css`
- `global.css`
- 巨大的 service / utils / store / component 文件

不得继续加入大段业务逻辑。

---

## 2. 新功能优先模块化

涉及以下能力时，优先新增独立模块：

- prompt
- schema
- parser
- builder
- service
- adapter
- action
- view
- store
- validator
- exporter
- importer
- renderer
- task
- worker
- formatter
- contract
- gateway
- repository
- bridge

---

## 3. 范围不足必须 STOP

如果当前允许路径过窄，会迫使新逻辑塞进中央大文件，必须 STOP。

报告格式：

```md
当前允许修改路径不足。继续执行会导致新业务逻辑被迫塞进中央大文件，破坏模块边界。

建议扩展允许路径：
- src/services/**
- src/parsers/**
- src/builders/**
- tests/**
```

---

## 4. 禁止事项

禁止：

- 复制粘贴扩散逻辑。
- 把多个职责混进一个函数。
- 为了小问题重写整个模块。
- 无测试的大范围重构。
- 将临时 hack 伪装成正式实现。
- 为了赶时间破坏已有模块边界。
