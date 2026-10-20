# monitor v5 eval progress

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_eval_progress_20260512T180557_result.json`
- **Structured JSON:** [`8bf4856ed8035650216f.json`](../../sessions/8b/8bf4856ed8035650216f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v5 评估进度报告

**进程状态**: PID 32154 存活，运行 2h15m

**Pipeline 阶段**:
- G0 训练 ✅ 完成（50m32s，1373 steps，10 个 checkpoint）
- G0 评估 🔄 进行中

**评估进度**: 正在评估 checkpoint **6/11**（checkpoint-912）
- 5 个 checkpoint 已完成
- 当前 spectral-rank 已算完，正在算 token entropy variance（02:06:36 开始）

**每个 checkpoint 评估耗时**: ~13.5 min（非常稳定，5 个间隔均为 13m28s±3s）

**预估剩余时间**:
- 完成 ckpt 6：~2-3 min
- 剩余 5 个 checkpoint：5 × 13.5 = ~68 min
- **G0 评估总剩余 ≈ 1h10m**

**注意**: Pipeline 配置了 3 个 generation（G0/G1/G2）。G0 评估完后可能还有 G1、G2 的训练+评估。如果 3 代结构一致，总剩余可能在 **~5-6h**。

**GPU**: 100% 利用率，29.7GB / 97.9GB 显存

**异常**: 无报错。有大量 `right-padding was detected` 警告，不影响正确性。

---
