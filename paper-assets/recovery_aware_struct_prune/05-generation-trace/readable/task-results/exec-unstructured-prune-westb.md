# exec unstructured prune westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_unstructured_prune_westb_20260517T052903_result.json`
- **Structured JSON:** [`b414c2d0ea53a1fafd00.json`](../../sessions/b4/b414c2d0ea53a1fafd00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

## 结果汇总

**Unstructured Pruning 完成**:
- Target sparsity: 20.0%
- Actual sparsity: **20.0430%** (1,307,865,434 / 6,525,288,448 zeroed)
- Magnitude threshold: 0.00555420
- Forward pass 验证通过
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20/` (15GB)

**Post-prune Eval 已启动**:
- tmux session: `eval_unstructured_20`
- GPU: cuda:1 (15076MiB 已占用)
- 评估: GSM8K, 1319 samples, greedy decoding, seed=42
- 日志: `/root/runs/recovery_aware_struct_prune/eval_unstructured_20.log`
- 结果将写入: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_unstructured_20_n1319.json`

cuda:0 未被占用（scoring_ablation 如之前所述）。

---
