# fix exp003 logging

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp003-logging_20260518T164945_result.json`
- **Structured JSON:** [`59d0bd78679721ec0f47.json`](../../sessions/59/59d0bd78679721ec0f47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

---

### 产出总结

**1. exp-003 当前日志（修复前最后 30 行）**：每步只有 `d_syc not loaded; returning R3-only rewards` 警告和进度条，无任何 R3 数值。训练正常推进到 step 16。

**2. R3 日志缺失根因**：`dcgrpo_trainer.py` 的 `_DCRewardCallable.__call__` 方法中，当 `d_syc is None` 时（line 128），计算 R3 后直接 `return`，跳过了后续所有 reward 日志代码（原 lines 159-184）。

**3. 修复措施**：在 `d_syc is None` 分支的 `return` 前添加：
   - 每步记录 `reward/r3_mean` 和 `reward/combined_mean`
   - 每 10 步记录详细统计（mean/std/min/max），与 else 分支格式一致
   - 递增 `_reward_step` 计数器

**4. 需要重启**：已重启。
   - 旧 PID 69094 → 新 PID **70649**（cuda:1, tmux session: exp003）
   - exp-002（PID 69020, cuda:0）未受影响，日志正常记录 R1/R3

**5. 修复后日志样例**：
```
[step 0] reward/r3  mean=0.2551  std=0.4345  min=0.0008  max=0.9994
[step 0] reward/combined  mean=0.2551  std=0.4345
reward/r3_mean=0.2551
reward/combined_mean=0.2551
...
reward/r3_mean=0.5609
reward/combined_mean=0.5609
```

---
