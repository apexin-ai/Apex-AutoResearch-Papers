# ssh check deepseek progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_deepseek_progress_20260515T133730_result.json`
- **Structured JSON:** [`aec7779b48b828eb451f.json`](../../sessions/ae/aec7779b48b828eb451f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 49.2 / 97.9 GB | 0% |
| 1 | 39.6 / 97.9 GB | 100% |

### 2. deepseek_no_trace_seed42 — **已完成**

PID 106822 已退出，训练和 eval 均完成。

| 指标 | 值 |
|------|-----|
| Accuracy | 73.4% |
| Majority baseline | 71.5% |
| Lift | +1.8pp (CI: [-0.9pp, +4.6pp]) |
| Pass F1 | 0.81 |
| Fail F1 | 0.54 |

Lift 置信区间跨零，统计上不显著。

### 3. deepseek_exception_only_seed42 (PID 107198) — **训练中**

- 进度：step **84/444**（19%），epoch 1 中段（epoch 1 共 148 steps）
- 速度：~27s/it（但波动大，12s-49s/it）
- 已用时间：~27 min
- 预计剩余：360 steps × ~25s ≈ **2.5 小时**（不含 eval 暂停）

### 4. vota checkpoint-148 eval — **意外仍在运行**

PID **110354** 在跑 vota checkpoint-148 eval，已运行 5:27，参数 `--gpu 0`。这就是之前说被 kill 的那个 eval——它**没死**，或者被重新启动了。占 GPU 0 约 49GB 显存（+ GPU 1 上 17GB）。

checkpoint-148 目录下**尚无** eval_results.json（eval 还在跑）。

### 5. deepseek_vota checkpoints

目录内容：`checkpoint-148`、`checkpoint-296`、`checkpoint-444`、`final`、`runs`——训练已全部完成，eval 正在逐个跑。

### 总结

- **no_trace**: 完成，lift 不显著
- **exception_only**: 训练中，~2.5h 剩余
- **vota epoch 1 eval**: 没被 kill 掉，正在跑（PID 110354），需要决定是让它跑完还是杀掉

---
