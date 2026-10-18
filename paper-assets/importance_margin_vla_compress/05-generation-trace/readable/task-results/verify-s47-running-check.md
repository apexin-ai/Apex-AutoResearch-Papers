# verify s47 running check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_s47_running_check_20260529T032617_result.json`
- **Structured JSON:** [`daabd67932928ee68f5b.json`](../../sessions/da/daabd67932928ee68f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 6 个实验存活，汇总如下：**

| # | 服务器 | 实验 | 存活 | 进度 | GPU 利用率 | GPU 显存 |
|---|--------|------|------|------|-----------|----------|
| 1 | cqa1 cuda:0 | attn k=0.95 s47 v3 | **Y** (PID 771290, 3min) | 刚启动，PRUNE-DIAG 输出，T0 未开始 | 22% | 19.7/24.6 GB |
| 2 | cqa1 cuda:1 | attn k=0.9 s47 | **Y** (PID 746590, 35min) | T1 ep10 (T0 done SR=38%) | 22% | 10.6/24.6 GB |
| 3 | cqa1 cuda:2 | random k=0.9 s47 | **Y** (PID 752199, 28min) | T0 ep40 (4/40=10%) | 34% | 10.5/24.6 GB |
| 4 | cqa1 cuda:3 | random k=0.85 s47 | **Y** (PID 746920, 35min) | T0 done SR=50%, 进入 T1 | 22% | 10.5/24.6 GB |
| 5 | w41 cuda:0 | attn k=0.5 s47 | **Y** (GPU 活跃) | T3 ep20 (累计 97/150=64.7%) | 29% | 10.6/97.9 GB |
| 6 | w38 cuda:0 | attn k=0.85 s47 | **Y** (GPU 活跃) | T3 ep40 (累计 53/150=35.3%) | 49% | 10.6/97.9 GB |

注意：cqa1 cuda:0 的 v3 刚启动 3 分钟，显存占用较高（19.7GB vs 其他 ~10.5GB），可能是模型加载阶段。w41 和 w38 进度最快，已到 T3（第4个 task）。

---
