# code fix compile val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-compile-val-sweep_20260515T164826_result.json`
- **Structured JSON:** [`dcd4f35ca328fe997422.json`](../../sessions/dc/dcd4f35ca328fe997422.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 项修复全部完成，dry-run 验证通过：

**1. CSV 加 `seq_length` 列** — 每行有 `seq_length`（PREV_RESULTS=8192，scanned 从 JSON `config.max_seq_length` 读取，fallback 规则 step≤1600→8192, ≥1800→2048）

**2. Top-3 按 `seq_length` 分组** — 分别输出：
- `Top-3 (seq_length=8192)`: #1 ckpt-1000 88.23%, #2 ckpt-1200 87.76%, #3 ckpt-1600 86.75%
- `Top-3 (seq_length=2048)`: #1 ckpt-1800 82.99%（当前仅 1 个 ckpt）

**3. Unparseable rate 监控** — CSV 新增 `n_cls_unparseable` + `unparseable_rate` 列。ckpt-1800 unparseable rate = 20.17% (1883/9335)。当前仅 1 个有数据的 ckpt，后续 ckpt 完成后会自动触发 >5pp 差异 WARNING。

---
