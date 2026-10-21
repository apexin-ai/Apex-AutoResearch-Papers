# eval scp and submit next batch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_scp-and-submit-next-batch_20260522T104217_result.json`
- **Structured JSON:** [`24e53163f0e427e9e604.json`](../../sessions/24/24e53163f0e427e9e604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**没有可用的新 checkpoint 可以 eval。**

| 实验 | 状态 | 详情 |
|------|------|------|
| **ACT s2 (exp-004)** | 训练崩溃 | 磁盘满，checkpoint-2500 的 safetensors 被截断（421MB vs 正常 698MB），不可用。最后可用 checkpoint 仍是 2000 |
| **R3-only s2 (exp-003)** | 训练中 7329/8000 | 无新 checkpoint（最新仍是 7000，已传过） |

ACT s2 训练需要清理 29046 磁盘空间后重启才能产出更多 checkpoint。R3-only s2 预计还需 ~5 小时完成，checkpoint-7500 应该很快会出现。

---
