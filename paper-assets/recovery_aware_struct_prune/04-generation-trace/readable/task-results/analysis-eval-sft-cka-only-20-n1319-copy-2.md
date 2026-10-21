# analysis eval sft cka only 20 n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_sft_cka_only_20_n1319_20260517T234622_result.json`
- **Structured JSON:** [`d1ea86f3ef336d8f047e.json`](../../sessions/d1/d1ea86f3ef336d8f047e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: eval_sft_cka_only_20_n1319

| 指标 | 值 |
|------|-----|
| **GSM8K Accuracy** | **63.91% (843/1319)** |
| Standard Error | ±1.32% |
| EOS Rate | 99.01% (1306 natural / 13 truncated) |
| Avg Response Length | 198.1 tokens |
| Evaluation Time | ~4h 22min |

**关键路径:**
- Log: `/root/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log`
- Results JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20_n1319.json`
- Checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20`

**对比分析:**

| Method | Post-Prune | Post-SFT (N=1319) |
|--------|-----------|-------------------|
| Standard 20% | ~30% | ~59% |
| RASP 20% | ~35% | ~61% |
| CKA-only 20% | 38.5% | **63.9%** |
| Unpruned | — | ~73.6% |

CKA-only 20% post-SFT 达到 63.9%，高于 RASP (~61%) 和 Standard (~59%)。N=200 pilot 显示 64.0%，与 N=1319 完全吻合。结论：CKA-only 不仅 post-prune accuracy 最高，post-SFT 恢复后仍保持优势（+2.9% over RASP, +4.9% over Standard），SFT 没有完全均衡化不同 scoring method 的差异。

未发现 W&B run_id（log 中无 wandb 相关输出）。

---
