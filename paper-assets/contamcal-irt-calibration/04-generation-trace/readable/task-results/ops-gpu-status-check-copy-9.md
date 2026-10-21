# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T095734_result.json`
- **Structured JSON:** [`6e4efea8271dd47f2daa.json`](../../sessions/6e/6e4efea8271dd47f2daa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 状态总览:
cuda:0: 运行中  PID=325310  VRAM=8622/24564MiB  Util=54%  1.5B d100 eval (2h19m elapsed)
cuda:1: 运行中  PID=336750  VRAM=8622/24564MiB  Util=50%  1.5B aligned eval batch (39m elapsed)
cuda:2: 运行中  PID=332207  VRAM=3695/24564MiB  Util=36%  0.5B aligned eval batch (1h19m elapsed)
cuda:3: 运行中  PID=319555  VRAM=13341/24564MiB Util=100% 3B d100 SFT (3h03m elapsed)
cuda:4: 运行中  PID=335346  VRAM=21827/24564MiB Util=42%  3B d005 SFT (47m elapsed)
cuda:5: 运行中  PID=342935  VRAM=8985/24564MiB  Util=93%  3B d000 aligned eval (6m elapsed)

注: cuda:0 有额外进程 PID 336666 (2760MiB)，cuda:1 有额外进程 PID 338776 (2760MiB)

所有 6 个 PID 均在运行，无空闲 GPU。

各实验进度:
cuda:0  1.5B d100 eval        — 仍在运行（无日志路径，无法查进度）
cuda:1  1.5B aligned eval     — MMLU 已完成 → GSM8K 25% (333/1319, ~6.3s/it)
cuda:2  0.5B aligned eval     — MMLU 已完成 → GSM8K 66% (876/1319, ~5.1s/it)
cuda:3  3B d100 SFT           — 59% (2457/4159, ~4.3s/it), loss=1.17, token_acc=0.724
cuda:4  3B d005 SFT           — 21% (683/3177, ~3.9s/it), loss=1.10, token_acc=0.743
cuda:5  3B d000 aligned eval  — MMLU 87% (12281/14042, ~31it/s)

ETA 估算:
cuda:1  GSM8K 剩余 ~1h43m, 之后还有 arc_challenge + humaneval
cuda:2  GSM8K 剩余 ~38m, 之后还有 arc_challenge + humaneval
cuda:3  SFT 剩余 ~2h00m (完成约 19:58)
cuda:4  SFT 剩余 ~2h43m (完成约 20:40)
cuda:5  MMLU 剩余 ~1min, 之后还有 gsm8k + arc_challenge + humaneval (~2-3h)
```

---
