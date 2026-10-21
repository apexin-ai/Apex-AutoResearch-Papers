# analysis exp 004 eval ckpt7500 ckpt6500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-eval-ckpt7500-ckpt6500_20260520T160426_result.json`
- **Structured JSON:** [`0395c1a5afd82a0cd67e.json`](../../sessions/03/0395c1a5afd82a0cd67e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Summary 文件与 log 一致。结果如下：

```
exp-004-eval-ckpt7500:
  ToF:        0.1657
  NoF:        0.8453
  SYCONScore: 0.2771
  Samples:    362 (valid=181, invalid=181)
  退出状态:   正常 (EXIT_CODE=0)

exp-004-eval-ckpt6500:
  ToF:        0.1492
  NoF:        0.8232
  SYCONScore: 0.2526
  Samples:    362 (valid=181, invalid=181)
  退出状态:   正常 (EXIT_CODE=0)
```

**趋势判断 — 存在异常：**

完整序列（含已知数据点）：

| Checkpoint | SYCONScore | ToF    | NoF    |
|------------|-----------|--------|--------|
| ckpt-6000  | 0.262     | —      | —      |
| **ckpt-6500** | **0.2526** | 0.1492 | 0.8232 |
| ckpt-7000  | 0.286     | —      | —      |
| **ckpt-7500** | **0.2771** | 0.1657 | 0.8453 |
| ckpt-8000  | 0.301     | —      | —      |

两个中间 checkpoint 的 SYCONScore 都**低于其左侧邻居**，而非落在两者之间：
- ckpt-6500 (0.2526) < ckpt-6000 (0.262)，差 -0.0094
- ckpt-7500 (0.2771) < ckpt-7000 (0.286)，差 -0.0089

趋势并非单调递增，而是呈**锯齿形**：每个 500-step 中间点都出现局部回落，然后在下一个 1000-step 点回升。这说明 SYCONScore 在训练过程中存在振荡，整体上升趋势仍在，但 500-step 粒度下不是平滑单调的。可能原因：学习率波动、数据 batch 排列效应、或 checkpoint 保存时恰好处于 loss landscape 的非稳定点。

---
