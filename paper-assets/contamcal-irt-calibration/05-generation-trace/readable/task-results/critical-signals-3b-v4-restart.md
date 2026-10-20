# critical signals 3B v4 restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_signals-3B-v4-restart_20260515T185856_result.json`
- **Structured JSON:** [`9ef17083a460debbd42f.json`](../../sessions/9e/9ef17083a460debbd42f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态已明确。汇报发现并提出行动方案：

## 当前状态

**cuda:3 已有 v4 信号计算在运行** (PID 617202, 02:57 启动)：
- 跳过 5 个已完成任务，剩余 7 个任务
- 当前在 task 1/7: d000_s42/mmlu
- 队列: d000/mmlu → d005/gsm8k → d005/mmlu → d025/mmlu → d100×3

**cuda:4 并非空闲** — PID 597179 在跑 d000_a32_s42 SFT (13.9GB, 自 00:51 运行)。用户要 kill 的 PID 597174 与实际 PID 597179 不同，进程未被成功 kill。

**Checkpoint 就绪状态：**
- d025_v3_s42: 空（cuda:5 仍在训练），但原始 d025_s42 (alpha=16) 可用 ✓
- d100_s42: 原始 checkpoint (alpha=16) 存在 ✓
- d100_a32_s42: 空（cuda:1 仍在训练）

**信号完成度：**
| Dosage | mmlu | gsm8k | arc |
|--------|------|-------|-----|
| d000 | 运行中 | ✓ | ✓ |
| d005 | 待跑 | 待跑 | ✓ |
| d025 | 待跑 | ✓ | ✓ |
| d100 | 待跑 | 待跑 | 待跑 |

## 提议行动

1. **Kill PID 597179** (cuda:4 上冗余的 d000_a32_s42 SFT，原始 d000_s42 已是 alpha=32)
2. **cuda:4 启动新 batch**: `--only d025 d100` 并行处理，避免与 cuda:3 的 v4 写入冲突
   - cuda:3 (v4): d000/mmlu → d005/gsm8k → d005/mmlu (~60-90min)
   - cuda:4 (新): d025/mmlu → d100×3 (~75-90min)
   - 总时间 ~90min（vs 顺序 ~150min）

确认后执行 kill + 提交。

---
