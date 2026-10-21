# check all experiments health

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-experiments-health_20260524T233413_result.json`
- **Structured JSON:** [`f328ba539806c956c4e5.json`](../../sessions/f3/f328ba539806c956c4e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

| exp_id | server | GPU | 进程状态 | 当前 seed | 当前 step | 预估剩余时间 |
|--------|--------|-----|---------|-----------|-----------|------------|
| exp_060_cartpole_baseline | bjb1-45299 | cuda:0 (39%, 5213MiB) | ✅ 正常训练 | s2 (s0,s1 已完成@112K) | **65000**/112K | ~72min (fps≈10.9) |
| exp_061_cartpole_civo_trigger | bjb1-45299 | cuda:1 (23%, 2751MiB) | ✅ 正常训练 | s2 (s0,s1 已完成@112K) | **20000**/112K | ~2.5h (fps≈10) |
| exp_062_cartpole_control | bjb1-40020 | cuda:0 (18%, 3564MiB) | ✅ 正常训练 | s1 (s0 已完成@112K) | **112000**/112K | s1 即将结束，s2 还需~3h |
| exp_066_timeseries_rssm_fidelity | bjb1-40020 | cuda:1 (12%, 757MiB) | ✅ 刚启动 | s0 | **5000**/60K | fps 待定，刚过 prefill |

补充说明：

- **实际步数为 112K/seed**（非预期的 105K），s0/s1 完成的 seed 均停在 112K
- **exp_060** s2 表现良好，eval_return@65K=462.3，civo/alert=0
- **exp_061** s2 刚开始不久（20K），train_return 在 147-174 范围
- **exp_062** s1 日志显示 train_return 从 181→251 在 112K 步，可能正在完成最后的环境交互，尚未创建 s2 目录
- **exp_066** 刚过 prefill，eval_return@5K=35.6，有 `torch.cuda.amp.autocast` 的 FutureWarning（不影响训练）

4 个实验均正常运行，无异常。

---
