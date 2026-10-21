# ops verify gs8 killed and act256 progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gs8-killed-and-act256-progress_20260525T210155_result.json`
- **Structured JSON:** [`474333da9867e416d6ee.json`](../../sessions/47/474333da9867e416d6ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已终止。汇总结果：

```
cuda:1 状态: 已清理。原有 gs8 进程 (PID 14497, run_exp002v3_gs8.py, 运行 1m37s) 已 kill。
exp-act-256-v2: 当前 step 1840/8000, 最新 checkpoint-1500, 预估剩余时间 ~42h
```

详细说明：
- **cuda:0**: exp-act-256-v2 (PID 2117) 正常运行，已跑 3h33m，GPU 利用率 41%，显存 24GB/98GB
- **cuda:1**: 已释放（gs8 进程已杀），无 gs8 相关 tmux session
- **exp-act-256-v2 进度**: step 1840/8000，每 10 步约 70s，剩余 6160 步 ≈ 43080s ≈ 12h。checkpoint 每 500 步保存，已有 500/1000/1500 三个

修正预估：按 elapsed 12791s 完成 1840 步，每步 ~6.95s，剩余 6160 步 × 6.95s ≈ **~11.9h**。

---
