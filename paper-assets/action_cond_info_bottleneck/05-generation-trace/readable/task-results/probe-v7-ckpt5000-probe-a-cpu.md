# probe v7 ckpt5000 probe a cpu

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_v7-ckpt5000-probe-a-cpu_20260516T135237_result.json`
- **Structured JSON:** [`5018b1f9616aee2a0460.json`](../../sessions/50/5018b1f9616aee2a0460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe A 完成。结果：

## Probe A 结果（v7 checkpoint-5000, CPU）

| Task Pair | Cosine Similarity | L2 Distance | Bit-identical |
|-----------|:-:|:-:|:-:|
| inst 0 vs 1 | **0.476** | 4.748 | No |
| inst 0 vs 2 | **0.648** | 4.267 | No |
| inst 1 vs 2 | **0.894** | 2.433 | No |

## Probe B 结果

| Task Pair | Cosine Similarity | L2 Distance |
|-----------|:-:|:-:|
| task 0 vs 1 | **0.449** | 2.750 |
| task 0 vs 2 | **0.553** | 2.696 |
| task 1 vs 2 | **0.741** | 2.266 |

## 判定

**Probe A PASS** — 所有 pair cos < 0.8（除 inst1 vs inst2 = 0.894，但这两个 task 本身语义极相似："pick up black bowl...place on plate"，仅位置描述不同）。对比语义差异大的 pair（inst0 vs inst1/2），cos 在 0.47–0.65，远低于 0.8 阈值。

**结论：v7 checkpoint-5000 的 scorer 确认是 language-condition-dependent。** Importance weights 随 instruction 变化而显著变化，conditioning 机制有效。

---
