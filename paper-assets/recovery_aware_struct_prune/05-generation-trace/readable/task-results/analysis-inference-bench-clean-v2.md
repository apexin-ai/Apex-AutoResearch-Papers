# analysis inference bench clean v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inference_bench_clean_v2_20260519T015704_result.json`
- **Structured JSON:** [`f44be37b6d2862bad6d7.json`](../../sessions/f4/f44be37b6d2862bad6d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析摘要

**实验状态：成功完成，无异常（无 OOM、无 GPU contention、进程正常退出）。**

### 指标表格

| Model | Params | TPS | Speedup | First-token (ms) | Per-token (ms) |
|---|---|---|---|---|---|
| Dense (original) | 7.62B | 72.0 | 1.00x | 20.1 | 13.9 |
| CKA-only 20% pruned | 6.16B (−19%) | 58.3 | **0.81x** | 16.4 (−18%) | 16.7 (+20%) |
| Standard 20% pruned | 6.16B (−19%) | 58.2 | **0.81x** | 16.4 (−18%) | 16.7 (+20%) |

### 核心结论

1. **Pruned 模型没有 TPS speedup**：减少 19% 参数，TPS 反而慢 19%。原因是非均匀 MLP（intermediate_size 范围 8128~18944），irregular tensor shapes 导致 GPU kernel 效率低。
2. **Prefill 有加速**：首 token 延迟从 20.1ms 降到 16.4ms（−18%），因为模型更小，前向传播确实更快。
3. **Per-token generation 更慢**：13.9ms → 16.7ms（+20%），non-uniform 结构在 autoregressive decoding 中无法被 cuBLAS 高效处理。
4. **CKA-only vs Standard 无速度差异**：58.28 vs 58.25 TPS，两者结构相同（同为 20% 剪枝率），剪枝策略不影响推理速度。
5. **Pruned 模型生成更少 token**：7.6K / 7.1K vs 12.7K，pruned 模型在 GSM8K 上更早触发 EOS。

### 对论文的影响

不能用 naive HuggingFace 推理声称 inference speedup。参数减少和内存节省是实际的（−19% params），但 TPS 加速需要 uniform pruning 或 custom sparse kernels。论文中应报告 parameter efficiency 和 memory reduction，推理速度如需声称需额外工程优化（如 padding to uniform size 或 sparse GEMM）。

---
