# ops harvest 30476 eval results

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_30476_eval_results_20260518T055439_result.json`
- **Structured JSON:** [`e82b173fe66f88a825ea.json`](../../sessions/e8/e82b173fe66f88a825ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验 registry 均已更新为 DONE/success。

**汇总：**

| Experiment | Eval PPL (holdout) | Eval Loss | Tokens | Status |
|---|---|---|---|---|
| grid_b0_2_seed123 | 18.43 | 2.914 | 4,077,068 | DONE |
| grid_b0_2_seed456 | 18.34 | 2.909 | 4,077,068 | DONE |

对比 parent grid_b0_2_seed42 的 PPL 17.64：两个新 seed 的 final checkpoint PPL 均约 18.3-18.4，比 checkpoint-5500 时的 PPL 17.64 有所上升。之前 eval_all tmux 对 checkpoint-5500 的评估显示两个 seed 的 PPL 都是 17.64，与 seed42 一致，说明 checkpoint-5500 处 cross-seed 复现是成功的，但从 5500 继续训练到 final（6103 步）出现了轻微过拟合。

---
