# ops check both profiling status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_both_profiling_status_20260515T104213_result.json`
- **Structured JSON:** [`3e96274591ce4cbd4efe.json`](../../sessions/3e/3e96274591ce4cbd4efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果齐全。汇总如下：

---

## 实验 1: Pythia-1.4B profiling — **已完成** ✓

| 指标 | 值 |
|------|-----|
| Baseline PPL | 13.6347 |
| Top-5% concentration | 0.2439 (19/384 heads) |
| t1/t5 ratio | 1.94 |
| L0 dominance | 0.51x (L0 不突出) |
| CV | 1.2172 |
| Shape | **Spike** |
| 总耗时 | 25.7 min |
| 正 delta heads | 362/384 |

**Top-10 敏感 heads:**

| Rank | Head | delta(2bit) |
|------|------|-------------|
| 1 | L1H11 | 1.016355 |
| 2 | L12H14 | 0.784513 |
| 3 | L8H4 | 0.759118 |
| 4 | L11H2 | 0.632357 |
| 5 | L13H2 | 0.522849 |
| 6 | L17H10 | 0.502587 |
| 7 | L12H8 | 0.422504 |
| 8 | L15H2 | 0.403288 |
| 9 | L16H8 | 0.392855 |
| 10 | L11H10 | 0.369483 |

特征：Spike 模式——少量 head 贡献不成比例的 delta，但 concentration 偏低 (0.24)，spike 集中在中间层（L8-L17），L0 反而不显著。

---

## 实验 2: Qwen2.5-14B profiling — **运行中**

| 指标 | 值 |
|------|-----|
| 进度 | **336/384** (87.5%) |
| 已用时 | 141 min (2h21m) |
| ETA | **~20 min** |
| 当前位置 | L41H7 |
| PID | 315792 (存活) |

---

## GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | **0 MiB** / 97887 MiB | 0% (Pythia 已结束释放) |
| cuda:1 | RTX PRO 6000 Blackwell | **31101 MiB** / 97887 MiB | 92% (Qwen 运行中) |

Qwen 预计 ~20 分钟后完成，届时可提取结果。

---
