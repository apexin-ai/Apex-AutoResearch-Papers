# research expand bugsinpy

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_expand_bugsinpy_20260514T150046_result.json`
- **Structured JSON:** [`018ae6124bfc8dc4cc05.json`](../../sessions/01/018ae6124bfc8dc4cc05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地和服务器文件一致。汇报结果：

---

## 结果汇报

### 1. BugsInPy 可用但未使用的项目/bug

| 项目 | 总 bug 数 | 已使用 | 可用余量 |
|------|----------|--------|---------|
| PySnooper | 3 | 0 | 3 |
| ansible | 18 | 0 | 18 (大仓库，慎用) |
| black | 23 | 2→4 | 19 |
| cookiecutter | 4 | 3 | 1 |
| fastapi | 16 | 3→4 | 12 |
| httpie | 5 | 2 | 3 |
| keras | 45 | 0 | 45 (大仓库，慎用) |
| luigi | 33 | 2→5 | 28 |
| matplotlib | 30 | 0 | 30 (大仓库，慎用) |
| pandas | 169 | 3 | 避免（仓库过大） |
| sanic | 5 | 2 | 3 |
| scrapy | 40 | 2→5 | 35 |
| spacy | 10 | 0 | 10 |
| thefuck | 32 | 3 | 29 |
| tornado | 16 | 2→5 | 11 |
| tqdm | 9 | 2 | 7 |
| youtube-dl | 43 | 2→5 | 38 |

### 2. 选中的 15 个新候选及理由

| # | 候选 | 选择理由 |
|---|------|---------|
| 1 | scrapy#3 | redirect middleware URL scheme 处理链，涉及 urljoin + urlparse 多层调用 |
| 2 | scrapy#4 | contract errback 回调链，exc_info 元组排序 bug |
| 3 | scrapy#7 | form request URL 提取管道，多函数调用链 |
| 4 | tornado#4 | StaticFileHandler range 请求处理，复杂多分支逻辑 |
| 5 | tornado#5 | PeriodicCallback 定时器循环更新逻辑，含时钟回退处理 |
| 6 | tornado#7 | IOLoop.run_in_executor 跨线程 future 链接 |
| 7 | luigi#5 | inherits/requires 装饰器继承链，涉及元类操作 |
| 8 | luigi#10 | worker 待处理任务过滤，scheduler 循环中的状态管理 |
| 9 | luigi#14 | scheduler 失败检测状态机，含 disable_failures 逻辑 |
| 10 | youtube-dl#5 | unified_timestamp 多格式日期解析管道，循环匹配 |
| 11 | youtube-dl#10 | js_to_json 正则替换管道，多步文本处理 |
| 12 | youtube-dl#20 | HTML 元素属性提取，正则迭代匹配 |
| 13 | black#5 | bracket_split_build_line 尾逗号检测循环 |
| 14 | black#14 | future imports 递归 AST 子节点遍历 |
| 15 | fastapi#5 | 递归模型字段克隆链 (create_cloned_field) |

### 3. 验证结果

| 候选 | 状态 | 详情 |
|------|------|------|
| scrapy#3 | **SUCCESS** | commit be2e910, 293 Python files |
| tornado#5 | **SUCCESS** | commit 2d4053d, 122 Python files |
| luigi#5 | **SUCCESS** | commit 45b5711, 216 Python files |

`bugsinpy_setup.py` 已更新为 45 个候选（本地 + 服务器同步）。注意：服务器上 `_checkout_version` 使用全量 clone，在 AutoDL 上需要先 `source /etc/network_turbo` 启用加速，否则会超时。

---
