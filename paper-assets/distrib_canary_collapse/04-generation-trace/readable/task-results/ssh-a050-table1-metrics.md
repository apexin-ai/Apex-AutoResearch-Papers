# ssh a050 table1 metrics

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a050_table1_metrics_20260517T065312_result.json`
- **Structured JSON:** [`313dc9ca01b7fa5bc8d9.json`](../../sessions/31/313dc9ca01b7fa5bc8d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## α=0.50 (3 seeds) drift mean±std

| Metric | Drift |
|--------|-------|
| Token entropy | −18.0 ± 0.5% |
| ECE | +822.6 ± 18.3% |
| Distinct-1 | −37.1 ± 0.4% |
| Distinct-2 | −50.4 ± 1.0% |
| Perplexity | +21.0 ± 0.1% |

## 原始值（验证用）

**gen_0 值三 seed 一致**（同一 base model）：
- token_entropy: 3.234195
- ece: 0.010805
- distinct_1: ~0.0982
- distinct_2: ~0.5148
- perplexity: 26.948959

**gen_10 值（per seed）：**

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| token_entropy | 2.6318 | 2.6707 | 2.6491 |
| ece | 0.1019 | 0.0971 | 0.1001 |
| distinct_1 | 0.0616 | 0.0624 | 0.0614 |
| distinct_2 | 0.2513 | 0.2617 | 0.2525 |
| perplexity | 32.644 | 32.633 | 32.578 |

注：gen_0 的 token_entropy/ece/perplexity 三 seed 完全相同（共享初始模型），distinct_1/distinct_2 有微小差异（来自生成采样的 seed 不同）。跨 seed 方差很小，结果稳定。

---
