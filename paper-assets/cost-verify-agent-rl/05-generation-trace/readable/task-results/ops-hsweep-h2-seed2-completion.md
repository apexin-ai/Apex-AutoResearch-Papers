# ops hsweep h2 seed2 completion

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hsweep-h2-seed2-completion_20260518T024948_result.json`
- **Structured JSON:** [`5d2691d3cf174e93692b.json`](../../sessions/5d/5d2691d3cf174e93692b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。Cron 列表已为空，无需删除。

---

## 诊断报告

### 退出原因：正常完成
- 15/15 步全部完成 + final val + checkpoint 已保存
- 总耗时 12.14h (43689s)
- W&B run: `jhwyg4tc`

### Conclusion: **negative** — 未复现 seed1 的 catastrophic collapse

Seed2 与 seed1 行为**质性不同**：

| 指标 | Seed1 (终值) | Seed2 (终值) |
|------|------------|------------|
| val success | 0% | **9.375%** |
| val action_is_valid | 0.06% | **100%** |
| train success step 15 | 0% | **28.1%** |
| collapse onset | step 3-4 不可逆 | 无不可逆 collapse |

### Val 轨迹 (seed2)
- step 0: 0% success, 88.1% valid
- step 5: 0% success, 97.4% valid
- step 10: 0% success, 98.7% valid
- step 15: **9.375% success, 100% valid**, best@64=9.36, best@128=9.97

### 最终 train metrics (step 15)
- success=28.1%, pass@8=62.5%, action_is_valid=98.8%
- entropy=0.401, kl_loss=0.472, grad_norm=2.65

### ADV log
- 3000 行，可用于 sign misattribution 分析

### GPU 状态
- **bjb1 cuda:0,1 未空闲**。PID 977677/977678 (`actor_rollout_generate_sequences`) 仍占用 ~37.5GB/卡。可能属于另一个实验。

### 对论文的影响
Seed1 的 catastrophic action_is_valid collapse (→0.06%) 是 seed-dependent 现象，不能作为 h=2 的 robust finding 写入论文。h=2 确实造成严重学习困难（val 0% 持续到 step 10），但 seed2 表明这不是不可逆的。

---
