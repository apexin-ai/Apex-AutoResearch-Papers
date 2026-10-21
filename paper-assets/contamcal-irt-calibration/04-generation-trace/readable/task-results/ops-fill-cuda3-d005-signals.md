# ops fill cuda3 d005 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cuda3-d005-signals_20260516T203626_result.json`
- **Structured JSON:** [`8f35c0f61b0fd79b579a.json`](../../sessions/8f/8f35c0f61b0fd79b579a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认运行正常。S1 embedding 阶段正在编码训练数据（1404/12500 batches，~50 it/s）。

## 汇报

1. **Eval 依赖**：S1（embedding similarity）和 S2（Min-K%++）不依赖 eval 输出；S3 需要 `--original-eval-paths` 和 `--paraphrase-eval-paths`（eval_results.json），但未提供时会跳过或报警告，不影响 S1/S2/S4 运行。
2. **启动 PID**：859360（实际 GPU 进程 PID 859366）
3. **6 卡状态**：

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 11933 MiB | 0% | 已有进程 (825638) |
| 1 | 6917 MiB | 53% | 已有进程 (830115) |
| 2 | 7061 MiB | 58% | 已有进程 (853489) |
| 3 | 569 MiB | 8% | **Llama d005 ARC signals (859366)** ← 刚启动，正在 S1 embedding |
| 4 | 7013 MiB | 56% | 已有进程 (842929) |
| 5 | 8313 MiB | 84% | 已有进程 (831033) |

ARC 完成后会自动继续 GSM8K（同一 nohup bash 内顺序执行）。

---
