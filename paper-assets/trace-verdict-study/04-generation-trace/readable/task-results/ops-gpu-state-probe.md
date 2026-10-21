# ops gpu state probe

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_state_probe_20260516T153611_result.json`
- **Structured JSON:** [`fb4315f08cfecc1abfba.json`](../../sessions/fb/fb4315f08cfecc1abfba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: [异常] | 进程=无 | 显存=49175/97887 MiB | 泄漏显存（nomarker OOM 崩溃后未释放）
GPU 1: [占用] | 进程=train_sft(vota) PID 279483 | 显存=36535/97887 MiB | 100% 利用率，正常训练中
```

- **codellama13b_vota_seed42**: 仍在跑（step 63/298，~21%，~1 it/s，预计还需 ~4 分钟完成当前 epoch）
- **exception_only_nomarker_seed42**: 已崩溃（CUDA OOM，EXIT_CODE=1，尝试分配 472 MiB 时 GPU 0 只剩 17.56 MiB）
- **nomarker checkpoint 残留**: 无（目录不存在，重跑无需清理）
- **loop_only_seed123**: 已完成（EXIT_CODE=0，eval 结果已保存）

**GPU 0 问题**: 49 GB 显存被泄漏占用（无进程持有），重跑 nomarker 前需要 `nvidia-smi --gpu-reset -i 0` 释放，或等 vota 训完后整机重置。

---
