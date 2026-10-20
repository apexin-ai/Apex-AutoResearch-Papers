# ssh check v7 and run evals

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_v7_and_run_evals_20260521T204119_result.json`
- **Structured JSON:** [`6c939cd8f63cc4abd496.json`](../../sessions/6c/6c939cd8f63cc4abd496.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v7 TG s123 训练状态：STILL_RUNNING**

- PID 245628 存活
- 当前进度：**Epoch 2, optimizer step ~2700 / 3000（90%）**
- epoch_0 和 epoch_1 checkpoint 已保存
- epoch_2 正在进行中

**剩余时间估算：**
- epoch_0 → epoch_1 间隔：7134 秒（~119 分钟），对应 1000 optimizer steps
- 速率：~7.1 秒/step
- 剩余 ~300 steps × 7.1 = **~2140 秒 ≈ 36 分钟**

**最新训练指标（step 2700 附近）：**
- L_NTP ≈ 0.85-1.05，L_GAR ≈ 0.0000-0.005，L_DIV ≈ 0.0000
- Gate mean ≈ 0.947，std ≈ 0.053，min ≈ 0.781，max ≈ 0.996
- Gate profile (step 2700): L5 最低(0.781)，L27 最高(0.996)

训练仍在运行，预计约 36 分钟后完成。完成后再提取完整 metrics 并启动 v8b SS s123 eval。

---
