# train sft v2 eval

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft-v2-eval_20260514T092308_result.json`
- **Structured JSON:** [`07fc3915989972b88dd8.json`](../../sessions/07/07fc3915989972b88dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据清晰了。汇报如下：

---

## Sandbox 测试结果：50 样本，3 成功 (6%)

| 错误类型 | 数量 | 原因 | 可修？ |
|---------|------|------|-------|
| **IndentationError** | 22 (44%) | `_insert_probe` 缩进叠加 bug | **是** |
| **SyntaxError** | 13 (26%) | buggy_code 本身有语法错误，文件无法被 Python 解析 | **否**（插入式 probe 的固有限制） |
| **NameError: List** | 11 (22%) | buggy_code 用 `List[int]` 但没 `from typing import List` | **是** |
| **NameError: other** | 1 (2%) | 同上类似 | 可能 |
| 成功 | 3 (6%) | — | — |

### 根因分析

**Bug 1 — 缩进叠加 (22 samples)**：当 probe 注释不含 `LINE N` 格式（如 `# INSERT AFTER LINE: for j in range(...)`），`_parse_insertion_comment` 无法提取行号，返回 `target_line=None`。probe 落入 strategy 2（首个方法 def），此时 `body_indent + pl` 会在 probe 已有的缩进上再加一层缩进。

原因：`textwrap.dedent` 在 L120 应用于整个 probe 文本（含注释行），注释行缩进=0 导致 dedent 无效。注释行被 `_parse_insertion_comment` 移除后，剩余 probe 行仍保留原始缩进。

**Bug 2 — Missing typing import (11 samples)**：LeetCode 风格代码用 `List[int]` 但不含 import，独立执行时 NameError。

### 修复方案

**Fix 1** — `_insert_probe` L121 后，对 probe_lines 重新 dedent：
```python
if probe_lines:
    probe_lines = textwrap.dedent("\n".join(probe_lines)).strip().split("\n")
```

**Fix 2** — `execute_probe` 中 prepend `from typing import *`：
```python
instrumented = "from typing import *\n" + instrumented
```

修复后预期：50 - 13(不可修) = **37/50 (74%)** 可执行。

### 要继续修然后重测吗？SFT 训练不依赖 sandbox（只影响 eval），也可以先起 SFT。

---
