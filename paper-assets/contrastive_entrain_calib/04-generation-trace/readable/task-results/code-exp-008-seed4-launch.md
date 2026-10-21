# code exp 008 seed4 launch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-seed4-launch_20260525T043003_result.json`
- **Structured JSON:** [`e5479566381e3c4df948.json`](../../sessions/e5/e5479566381e3c4df948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### 任务 A：Eval 结果已收集

**Seed2（全部 5 checkpoint）：**

| Checkpoint | ToF | NoF | SYCONScore | Entropy |
|---|---|---|---|---|
| ckpt-500 | 0.2762 | 0.6796 | **0.3928** | 0.364 |
| ckpt-1000 | 0.1492 | 0.8840 | 0.2553 | 0.222 |
| ckpt-1500 | 0.1050 | 0.9392 | 0.1888 | 0.328 |
| ckpt-2000 | 0.0442 | 0.9724 | 0.0846 | 0.147 |
| final | 0.0442 | 0.9724 | 0.0846 | 0.147 |

**Seed3（3/5 checkpoint，剩余 2 个 eval 在 cuda:0 进行中）：**

| Checkpoint | ToF | NoF | SYCONScore | Entropy |
|---|---|---|---|---|
| ckpt-500 | 0.2541 | 0.7403 | 0.3784 | 0.454 |
| ckpt-1000 | 0.2873 | 0.6961 | **0.4067** | 0.175 |
| ckpt-1500 | 0.1878 | 0.8287 | 0.3063 | 0.142 |

两个 seed 趋势一致：SYCONScore 随训练步数下降，后期 checkpoint 模型退化（输出 gibberish）。ckpt-2000/final 指标相同（训练在 2000 步结束）。

### 任务 B：Seed4 训练已启动

- **GPU**: cuda:1, PID 2366, 不影响 cuda:0 上的 seed3 eval
- **tmux session**: `exp008_seed4`
- **配置**: seed=44, max_steps=2000, alpha=64, 4 modules (q/k/v/o), dropout=0
- **当前状态**: step 20, loss=1.97, 正常运行中
- **Registry**: exp-008-seed4 → RUNNING
- **Cron 监控**: 每 15 分钟检查一次（job ID: 8cbd7792）

---
