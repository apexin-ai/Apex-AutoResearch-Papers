# analysis exp 010a final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_010a_final_20260516T120029_result.json`
- **Structured JSON:** [`8974d348f12efabf84bd.json`](../../sessions/89/8974d348f12efabf84bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**exp_010a_cheetah_baseline_s1 — 完成**

| 指标 | 值 |
|------|-----|
| 最终 step | 524,000 |
| 最终 eval_return | **849.8** (step 515K) |
| 峰值 eval_return | **849.8** (step 515K) |
| 训练时长 | 13.18 小时 |
| 退出状态 | 正常 (EXIT_CODE=0) |
| Checkpoint | `latest.pt` (219MB) |
| W&B | 无 |

结果优秀——849.8 完全在 DreamerV3 参考水平（800-900@500K）内，作为 Cheetah Run 的 dt=1 baseline 非常扎实。学习曲线稳定上升，300K 后进入 700+ 区间，500K 附近稳定在 830-850。

---
