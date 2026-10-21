# eval qwen adaptive lm eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_adaptive_lm_eval_20260517T140057_result.json`
- **Structured JSON:** [`62b571fc111c65ad916b.json`](../../sessions/62/62b571fc111c65ad916b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部评估完成。汇总对比结果：

## Qwen3-0.6B 下游评估对比：Adaptive vs Base

| Benchmark | Metric | Base (pre-trained) | Adaptive (batchsize16_nmin8) | Δ |
|-----------|--------|-------------------|------------------------------|-----|
| HellaSwag (10-shot) | acc_norm | 0.4678 | **0.4890** | +2.12% |
| ARC-Easy (25-shot) | acc | 0.7138 | 0.7075 | -0.63% |
| ARC-Easy (25-shot) | acc_norm | 0.7041 | **0.7121** | +0.80% |
| PIQA (5-shot) | acc | 0.6692 | **0.6828** | +1.36% |
| PIQA (5-shot) | acc_norm | 0.6719 | **0.6899** | +1.80% |
| WinoGrande (5-shot) | acc | 0.5580 | 0.5572 | -0.08% |

**结论**：Adaptive weighting fine-tuning 在大多数 benchmark 上略有提升（HellaSwag +2.1%，PIQA +1.8%，ARC-Easy acc_norm +0.8%），WinoGrande 基本持平，无明显退化。

### 文件路径
- Adaptive 结果：`/root/autodl-tmp/provenance_weight_training/output/eval/qwen_adaptive_*/`
- Base 结果：`/root/autodl-tmp/provenance_weight_training/output/eval/qwen_base_*/`
- 日志：`/root/eval_adaptive.log`, `/root/eval_base.log`

### 备注
- 服务器上无 Qwen3-0.6B uniform_seed42 checkpoint（仅有 llama3b_uniform_seed42）
- `batchsize16_nmin8_seed42` 即任务中的 "adaptive_fix_seed42"（确认为 Qwen3ForCausalLM + adaptive weighting）
- 用 base Qwen3-0.6B 作为对比 baseline

---
