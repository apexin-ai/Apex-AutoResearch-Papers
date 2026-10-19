# ops eta check all running

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eta-check-all-running_20260516T050417_result.json`
- **Structured JSON:** [`37e8808b151c040e67b9.json`](../../sessions/37/37e8808b151c040e67b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前时间**：2026-05-16 13:04:50 CST (+0800) = **05:04:50 UTC**

| 实验 | GPU | 当前进度 | Speed | ETA (UTC) |
|------|-----|---------|-------|-----------|
| seed1 | cuda:0 | step 11000/20000 | 0.9 steps/s | **07:51** (+2h47m) |
| seed2 | cuda:1 | step 4300/20000 | 0.8 steps/s | **10:31** (+5h27m) |
| baseline_plus libero_10 | cuda:0 | task 3/10 进行中 (~175/500 rollouts) | ~1h15m/task | **~12:45** (+7h40m) |
| baseline_std libero_10 | cuda:1 | task 1/10 进行中 (~75/500 rollouts) | ~3h/task（受竞争影响） | **~次日 00:00+**（极慢） |

**Task-by-task 时序证据**：
- baseline_plus：_0→09:42, _1→10:42 (1h), _2→12:01 (1h19m), _3 进行中 (12:01 起)
- baseline_std：_0→11:28 (无竞争 ~1h), _1 进行中 11:28- (已 1h36m, 仅 6/10 视频)
- baseline_std task 1 起开始与 seed2 (11:30 启动) 共享 cuda:1，速度掉到 ~3x

**GPU 共享可行性 (cuda:1)**：
- 当前：22154 MiB / 97887 MiB (~22 GB)，util 49%
- 加一个训练 (~16 GB) → **~38 GB / 98 GB，显存可行（剩余 60 GB）**
- **但 SM 竞争严重**：seed2 (训练 16GB+计算重) + baseline_std (rollout) + 新训练 → util 可能拉到 90-100%，三任务都会变慢 30-50%。当前 baseline_std task 1 已经从 1h/task 拖到 ~3h/task 就是证据。
- 显存无 fragmentation 风险（单 process 显存 ≤22GB，远低于 98GB）

**结论**：
- **baseline_plus 先完成**：约 **12:45 UTC**（早于 baseline_std ~12 小时以上）
- cuda:1 上再加训练**显存够但性能不划算**——建议等 seed1 (07:51 UTC) 完成后再到 cuda:0 启动新训练，避免雪上加霜

---
