# data plan 005 vota regen

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan_005_vota_regen_20260515T231831_result.json`
- **Structured JSON:** [`98716c543b3a84011c67.json`](../../sessions/98/98716c543b3a84011c67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部重新生成。汇总报告：

## 修复前后对比

### Bug 影响范围
- 1006 fail 样本中，仅 376 (37.4%) 在 `trace_raw` 有 exception 事件
- 全部 1006 (100%) 在 `test_results.error` 有错误信息
- **630 个 fail 样本的异常信息被遗漏**

### 修复内容
在 `format_sample` 中为 `exception_only` 和 `vota` 条件添加了 `test_results.error` fallback：当 `trace_raw` 无 exception 事件时，从 `test_results.error` 生成合成 exception 事件。

### 各条件变化

| 条件 | 受影响 | 变化样本数 | 说明 |
|------|--------|-----------|------|
| **exception_only** | 是 | 630 (123 test + 507 train) | Empty trace: 修复前含 fail 样本 → 修复后只剩 pass 样本 (50.9%) |
| **vota** | 是 | 630 (123 test + 507 train) | fail [ERROR] 覆盖: test 82→205 (39.6%→99.0%), empty: 122→0 |
| **ae_only** | 否 | 0 | 完全一致，不使用 exception |

### Token 长度分布（修复前 → 修复后）

| 条件 | mean | median | p75 | max |
|------|------|--------|-----|-----|
| exception_only | 376.5 → 377.1 | 297 → 299 | 445 → 445 | 1877 → 1879 |
| vota | 1502.7 → 1508.0 | 2047 → 2047 | 2048 → 2048 | 2048 → 2048 |

Token 长度几乎无变化，因为注入的 exception 文本很短（通常一行 `[ERROR] SyntaxError at line ?: ...`）。

### VOTA 2 个 fail 样本仍无 [ERROR]
205/207 (99.0%)，2 个样本有 trace exception 事件但格式可能不匹配 `_extract_exceptions` 提取模式，属于边缘情况。

### 产出文件
- `/root/autodl-tmp/trace-verdict-study-data/debugbench_{exception_only,vota}_{train,test}.jsonl` — 已重新生成
- `/root/autodl-tmp/trace-verdict-study-data/backup_pre_fix/` — 修复前备份

---
