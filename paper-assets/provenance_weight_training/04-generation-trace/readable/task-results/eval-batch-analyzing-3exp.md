# eval batch analyzing 3exp

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_batch_analyzing_3exp_20260518T052241_result.json`
- **Structured JSON:** [`a1e8fd30a3308944ff51.json`](../../sessions/a1/a1e8fd30a3308944ff51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部更新完毕，均 DONE/success。

## 汇总

| 模型 | PPL | Loss | 对比参考 | 结论 |
|------|-----|------|----------|------|
| contamination_60_uniform_seed456 | 17.769 | 2.8775 | seed42: 17.766, seed123: 17.754 | success，三 seed 一致 |
| grid_b0_1_seed456 | 17.663 | 2.8715 | seed42: 17.657 | success，PPL 差 0.006 |
| grid_b0_1_seed123 | 17.646 | 2.8705 | seed42: 17.657 | success，PPL 差 0.011 |

训练参数: 6103 步，无 W&B 记录。所有 registry 已更新（metrics、checkpoint_path、log_path、conclusion=success、status=DONE）。

---
