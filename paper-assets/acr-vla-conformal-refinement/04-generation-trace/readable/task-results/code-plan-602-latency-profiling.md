# code plan 602 latency profiling

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_602-latency-profiling_20260519T160742_result.json`
- **Structured JSON:** [`6ab70d0815fc1b981730.json`](../../sessions/6a/6ab70d0815fc1b981730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Profiling 完成。完整结果：

### 论文级 Latency Table（RTX 4090）

| Component | K=1 | K=5 | K=10 | K=20 |
|---|---|---|---|---|
| **VLA Sampling (batched)** | 180.0ms | 182.3ms | 162.3ms | 167.4ms |
| VLA Sampling (sequential) | 177.0ms | 891.7ms | 1638.9ms | 3245.8ms |
| CGS Features | - | 6.6ms | 6.3ms | 6.2ms |
| CRM Forward | 0.25ms | 0.25ms | 0.25ms | 0.25ms |
| Argmin Selection | - | 0.03ms | 0.03ms | 0.03ms |
| **Full Pipeline (batched)** | ~210ms | 216.0ms | **200.7ms** | **199.7ms** |

### 关键发现

1. **Batched sampling 近乎常数时间** — K=1→K=20 仅 ~180ms，因为 KV cache 扩展后 GPU 并行计算
2. **CRM overhead 极小** — 仅 0.25ms（MLP forward），加上 CGS 也只有 ~6.5ms，占 full pipeline 的 3.2%
3. **Sequential sampling 线性增长** — batched 比 sequential 快 20× (K=20)
4. **内存开销可控** — CRM 仅 1.8MB；K=20 peak 1085MB（VLA 本身 884MB）

JSON 结果已保存在 `bjb1-18228:/root/acr-vla-conformal-refinement/logs/latency_profile.json`。

---
