# code exp 008 seed3 launch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-seed3-launch_20260524T220831_result.json`
- **Structured JSON:** [`426bd6c8532c5318c8e0.json`](../../sessions/42/426bd6c8532c5318c8e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动并运行中。

**汇总：**

| 步骤 | 状态 |
|------|------|
| Eval 进程 (seed2) | 已终止，无已保存结果（仅完成 ckpt-500 的 80/362 pairs） |
| cuda:0 | 已释放并被 seed3 训练占用 |
| exp-008-seed3 训练 | 已启动 (PID 726631)，step=10，loss=1.9369，S(t)=0.43 |
| Registry | exp-008-seed3 → RUNNING，spec 已写入 |

seed2 的 eval 需要后续重跑（4 个 checkpoint 均未完成评估）。

---
