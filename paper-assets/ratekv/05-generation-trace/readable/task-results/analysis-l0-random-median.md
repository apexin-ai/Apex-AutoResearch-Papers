# analysis l0 random median

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_l0_random_median_20260514T072537_result.json`
- **Structured JSON:** [`38ee3f887317791d86ed.json`](../../sessions/38/38ee3f887317791d86ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已获取。计算 median：

**Qwen2.5-7B — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 11.4860 |
| seed_1 | 11.6153 |
| seed_2 | 11.3251 |
| seed_3 | 11.5151 |
| seed_4 | **12.5147** (离群) |

- **Mean ± Std**: 11.691 ± 0.422
- **Median**: **11.5151** (seed_3)

---

**Llama-3.1-8B — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 9.4845 |
| seed_1 | 10.4884 |
| seed_2 | 9.9406 |
| seed_3 | 10.0381 |
| seed_4 | **12.4441** (离群) |

- **Mean ± Std**: 10.479 ± 1.033
- **Median**: **10.0381** (seed_3)

---

**Mistral-7B-v0.3 — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 7.5233 |
| seed_1 | 7.6099 |
| seed_2 | 7.4134 |
| seed_3 | 7.5860 |
| seed_4 | 7.6692 |

- **Mean ± Std**: 7.560 ± 0.087
- **Median**: **7.5860** (seed_3)

---

**汇总对比表（所有方法）：**

| Method | Qwen2.5-7B | Llama-3.1-8B | Mistral-7B-v0.3 |
|--------|-----------|-------------|-----------------|
| BF16 baseline | 9.811 | 8.092 | 7.035 |
| Uniform 4-bit | 15.445 | 8.469 | 7.131 |
| Naive heuristic | 12.230 | 9.941 | 7.481 |
| **L0-random mean±std** | **11.691 ± 0.422** | **10.479 ± 1.033** | **7.560 ± 0.087** |
| **L0-random median** | **11.515** | **10.038** | **7.586** |
| MCKP | 10.913 | 8.450 | 7.323 |

seed_4 对 Qwen 和 Llama 影响明显：median 比 mean 分别低 0.176 和 0.441，Mistral 无离群值（median 与 mean 基本一致）。

---
