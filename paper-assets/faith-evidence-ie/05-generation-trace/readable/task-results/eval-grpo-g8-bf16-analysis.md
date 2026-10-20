# eval grpo g8 bf16 analysis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grpo_g8_bf16_analysis_20260515T175617_result.json`
- **Structured JSON:** [`8bdb78fedf69bc251e3d.json`](../../sessions/8b/8bdb78fedf69bc251e3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。汇总如下：

## eval_grpo_g8_bf16 全部结果

| Metric | ckpt80 | ckpt90 | ckpt100 | 趋势 |
|--------|--------|--------|---------|------|
| **rel_f1** | 0.4456 | 0.4523 | **0.4549** | ↑ 单调递增 |
| ign_f1 | 0.4456 | 0.4523 | 0.4549 | ↑ |
| **evi_f1** | 0.8034 | 0.8052 | **0.8086** | ↑ 单调递增 |
| edcr | 0.6409 | 0.6414 | 0.6318 | ≈ 平稳 (微降) |
| format_ok | 984/985 | 983/985 | 985/985 | ✓ |
| truncated | 50 | 60 | 61 | - |
| pred_count | - | 10756 | 10701 | - |

## Forgetting Dynamics 结论

| 方法 | rel_f1 | vs SFT baseline |
|------|--------|-----------------|
| SFT baseline | 0.4057 | - |
| QLoRA GRPO (G=8) | 0.2167 | -46.6% (**catastrophic forgetting**) |
| **bf16 LoRA GRPO ckpt80** | 0.4456 | +9.8% |
| **bf16 LoRA GRPO ckpt90** | 0.4523 | +11.5% |
| **bf16 LoRA GRPO ckpt100** | 0.4549 | **+12.1%** |

**结论：success。** bf16 LoRA GRPO 三个 checkpoint rel_f1 单调递增，无任何 forgetting 迹象。step 80→100 不仅没有衰退，反而持续改善。这与 QLoRA GRPO 的 catastrophic forgetting (rel_f1 从 0.4057 暴跌至 0.2167) 形成鲜明对比，确认 forgetting 是 QLoRA 4-bit quantization 导致的，非 GRPO 算法本身的问题。

---
