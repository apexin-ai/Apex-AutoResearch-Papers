# eval alpha sweep restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_alpha_sweep_restart_20260517T015311_result.json`
- **Structured JSON:** [`4673054dcd48c179a7b9.json`](../../sessions/46/4673054dcd48c179a7b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Alpha sweep 已经全部完成了。所有 eval 文件都是今天 (May 17) 生成的，N=200，greedy：

| Alpha | Accuracy | 时间 |
|-------|----------|------|
| 0.0 | 70.0% | 04:07 |
| 0.3 | 73.0% | 04:49 |
| 0.5 | 74.0% | 05:31 |
| 0.7 | 73.5% | 06:13 |
| 1.0 | 75.5% | 06:56 |
| 2.0 | 75.5% | 07:43 |

路径：`/root/autodl-tmp/recovery_aware_struct_prune/outputs/alpha_ablation/eval_alpha_*.json`

α=0.5 已成功完成（148/200 correct, accuracy=74%）。实际 checkpoint 覆盖的是 α∈{0.0, 0.3, 0.5, 0.7, 1.0, 2.0}（而非原计划的 {0, 0.25, 0.5, 1, 2}）。N=200 比指定的 N=100 更充分。

需要我将结果注册到 registry 吗？

---
