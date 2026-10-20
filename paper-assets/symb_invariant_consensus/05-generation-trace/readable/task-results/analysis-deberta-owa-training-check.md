# analysis deberta owa training check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deberta-owa-training-check_20260522T163802_result.json`
- **Structured JSON:** [`82ca33ce1bb919b481ba.json`](../../sessions/82/82ca33ce1bb919b481ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练状态：

| 项目 | 值 |
|------|-----|
| 进程 | PID 643576，运行中 |
| 当前进度 | **step 638 / 5,455**（11.7%） |
| 当前 epoch | 1/5（epoch 1 约完成 58%） |
| 速度 | ~1.25 s/step |
| GPU 显存 | 15,911 MiB，利用率 100% |
| 错误 | 无 |

**Eval 时间点**：`eval_strategy="epoch"`，首次 eval 在 epoch 1 结束时（step ~1,091），还需约 **9-10 分钟**。目前尚无 eval 指标。

**Loss**：`logging_steps=50` 但 loss 值被 tqdm 进度条的 `\r` 覆盖，日志文件中无法 grep 到。首次 eval 结束后会有 accuracy 输出。

**预计剩余时间**：(5455 - 638) × 1.25s ≈ **1 小时 40 分钟**。

---
