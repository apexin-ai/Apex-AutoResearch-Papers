# ops analyze plan 001 done

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_analyze_plan_001_done_20260515T202613_result.json`
- **Structured JSON:** [`3ca6f235dfae699a5eba.json`](../../sessions/3c/3ca6f235dfae699a5eba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 摘要

**plan_001_flat_nli_seed43 训练成功完成**

| 指标 | 值 |
|------|-----|
| 状态 | EXIT_CODE=0, 正常完成 |
| 总步数 | 507 (3 epochs) |
| 训练样本 | 2,691 (flat-NLI scoring) |
| train_loss | 0.6751 → 0.6257 (min 0.5895) |
| token_accuracy | 0.8473 |
| Checkpoint | `/root/autodl-tmp/rsft_output_flat_nli_s43` (504MB LoRA adapter) |
| 基座模型 | Qwen3-4B, LoRA r=64 α=128 |

**与 seed=42 对比（训练指标）：**
- seed=42: final_loss=0.6238, token_acc=0.8528
- seed=43: final_loss=0.6257, token_acc=0.8473
- 高度一致，差异在噪声范围内

**尚无 eval 结果。** seed=42 的 eval 已有 rel_f1=0.4539。seed=43 需要单独跑 eval 才能得到 rel_f1/evi_f1，与 CED RSFT 3-seed mean (0.4596, σ=0.0127) 做统计对比。

---
