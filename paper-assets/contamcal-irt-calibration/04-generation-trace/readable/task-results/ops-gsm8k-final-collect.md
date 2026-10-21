# ops gsm8k final collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-final-collect_20260521T145430_result.json`
- **Structured JSON:** [`70ad38073d6055f1034f.json`](../../sessions/70/70ad38073d6055f1034f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程仍在运行，进度接近完成：

| Dosage | PID    | 进度        | 预计剩余时间 |
|--------|--------|-------------|-------------|
| d000   | 528870 | 563/660 (85%) | ~9 min     |
| d025   | 529276 | 559/660 (85%) | ~9 min     |
| d100   | 529683 | 554/660 (84%) | ~9 min     |

速率约 5.3s/it，总 660 items。三个都还需约 **9-10 分钟**完成。所有 4 个 GPU 均在使用中（91-95% utilization，18-19GB VRAM）。

结果文件尚未生成（目录为空），需要等进程结束后才会写出 eval_results.json。

---
