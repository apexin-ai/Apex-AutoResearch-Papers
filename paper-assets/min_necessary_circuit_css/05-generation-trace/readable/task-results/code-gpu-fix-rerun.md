# code gpu fix rerun

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-fix-rerun_20260512T121133_result.json`
- **Structured JSON:** [`a26885ae9f30500d4aff.json`](../../sessions/a2/a26885ae9f30500d4aff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程持续运行中（PID 85098，3:44 elapsed）。日志缓冲导致新输出未刷到文件，但 EAP-IG 已完成，正在跑 Phase B（auto_circuit 方法，ACDC 是长时间任务）。

---

```
KILL: 成功 — PID 81244, 81322 均已终止
ROOT CAUSE: run_mvp.py 未设置 CUDA_VISIBLE_DEVICES，torch.device("cuda") 默认使用 cuda:0；config.py 无 GPU 配置
FIX: 在 run_mvp.py 最开头（import 之前）插入 os.environ["CUDA_VISIBLE_DEVICES"] = "5"；启动命令也传入 CUDA_VISIBLE_DEVICES=5 双重保险
RERUN: 成功启动 — PID=85098, 运行在 GPU-5 (UUID: GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263)
VERIFICATION: nvidia-smi 确认仅 GPU-5 有 PID 85098 的进程 (460 MiB)，其余 GPU 无我方进程
```

EAP-IG（Phase A）已完成（4/4 batches, ~10s），目前正在执行 Phase B（edge_pruning + ACDC）。ACDC 耗时较长，整个 MVP 可能需要 30-60 分钟完成。

---
