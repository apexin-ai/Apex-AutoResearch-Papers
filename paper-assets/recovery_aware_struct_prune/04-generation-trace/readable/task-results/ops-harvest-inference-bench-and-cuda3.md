# ops harvest inference bench and cuda3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_inference_bench_and_cuda3_20260519T021419_result.json`
- **Structured JSON:** [`78c8723c2736e838a25b.json`](../../sessions/78/78c8723c2736e838a25b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成，`EXIT_CODE=0`。结果：

| Model | Params | tok/s | Speedup | TTFT (mean) | Per-token latency (mean) |
|---|---|---|---|---|---|
| **Dense (original)** | 7.62B | 72.0 | 1.00x | 20.1ms | 13.9ms |
| **pruned_cka_only_20** | 6.16B | 58.3 | 0.81x | 16.4ms | 16.7ms |
| **pruned_standard_20** | 6.16B | 58.2 | 0.81x | 16.4ms | 16.7ms |

关键发现：

- 两个剪枝模型参数量一致（6.16B，削减 19.1%），throughput 和 latency 也几乎相同
- **剪枝后 throughput 反而下降了 19%**（72.0 → 58.3 tok/s），speedup 为 0.81x 而非 >1.0x
- TTFT 改善了 18%（20.1ms → 16.4ms），说明 prefill 阶段参数减少确实有加速
- 但 per-token latency 反升（13.9ms → 16.7ms，+20%），这是 throughput 下降的根因

throughput 下降大概率因为 **non-uniform MLP**（intermediate_size 范围 8128–18944）导致 GPU kernel 效率低。非均匀结构无法充分利用 tensor core 对齐，实际推理反而变慢。这在结构化剪枝中是已知问题，论文中需要讨论或考虑使用 uniform pruning ratio。

---
