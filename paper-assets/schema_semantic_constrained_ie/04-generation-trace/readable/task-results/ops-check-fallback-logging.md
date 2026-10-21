# ops check fallback logging

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_fallback_logging_20260514T032110_result.json`
- **Structured JSON:** [`ef6053bafea029bb7761.json`](../../sessions/ef/ef6053bafea029bb7761.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## 检查结果

### 1. 方案 A（try-except AssertionError）— `run_constrained_extraction.py`

有日志。三处 except 分支都用了 `warnings.warn()`：

| 行号 | 内容 |
|------|------|
| L435-438 | `except AssertionError:` → `warnings.warn("XGrammar accept_token assertion failed — falling back to grammar-only")` |
| L480-482 | `except AssertionError:` → `warnings.warn("XGrammar assertion failed in S2 Pass 1 — falling back to grammar-only")` |
| L539-541 | `except AssertionError:` → `warnings.warn("XGrammar assertion failed in S2 Pass 2 — falling back to grammar-only")` |

### 2. 方案 B（skip semantic masking）— `type_mask_processor.py`

**无任何日志。** `_apply_type_mask` 中 L368-369 的跳过分支（`if not any_allowed_valid: return logits`）是静默返回，没有 print/logging/warning。文件中不存在任何 `print`、`logging`、`warn` 调用。

### 3. 当前实验进度

- **105/998**（~10.5%）
- 进程 PID 157042 运行中，elapsed 5m06s
- GPU 占用 16878 MiB

### 4. 日志中 fallback/skip/WARNING 出现次数

全部为 **0**。日志内容只有启动信息（模型加载、参数打印），没有任何 warning 输出。

### 5. 结论

- 方案 A 的 fallback 有 `warnings.warn()` 会输出到 stderr（重定向到了日志），但目前 105 样本内**零次触发**
- 方案 B 的跳过完全静默，即使触发了也无法从日志观察到
- 建议在 ~300/998 时再检查一次日志中 warning 数量，确认方案 A 的 fallback 频率

---
