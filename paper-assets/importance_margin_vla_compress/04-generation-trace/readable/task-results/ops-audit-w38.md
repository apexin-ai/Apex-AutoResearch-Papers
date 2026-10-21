# ops audit w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-w38_20260527T165311_result.json`
- **Structured JSON:** [`b1901ff420534ebd8197.json`](../../sessions/b1/b1901ff420534ebd8197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 审计结果

```
GPU0: [运行中] PID=272022 OV Random k=0.95 Long seed42 v3     运行4h47m  Task 6/10 ep10  ~55%
GPU1: [运行中] PID=266221 OV Attn k=0.75 Long seed42 v3       运行4h54m  Task 6/10 ep20  ~56%
GPU2: [运行中] PID=433043 π0.5 Random k=0.7 Long seed43       运行1h07m  Task 4/10 ep10  ~32%
GPU3: [运行中] PID=390885 π0.5 Random k=0.95 Long seed43      运行2h00m  Task 7/10 ep10  ~62%
```

GPU0/GPU1 的"未注册任务"确认就是预期的 OV 实验，与 Director 报告一致。

## westd-41074 审计结果

```
GPU0: [运行中] PID=781023 π0.5 L2norm k=0.75 Long seed43      运行1h53m  Task 8/10 开始  ~70%
GPU1: [已完成] PID=756259 π0.5 Attn k=0.95 Long seed43        SR=77.2%  EXIT_CODE=0  ← GPU空闲
GPU2: [运行中] PID=840151 π0.5 Random k=0.75 Long seed43       运行1h11m  Task 4/10 ep30  ~35%
GPU3: [运行中⚠️] PID=821255 π0.5 L2norm k=0.7 Long seed43     运行1h23m  Task 4/10 ep40  ~35%
      [运行中⚠️] PID=816713 π0.5 L2norm k=0.95 Long seed43    运行1h26m  Task 6/10 ep30  ~55%
```

**关键发现：**

1. **GPU1 已空闲** — Attn k=0.95 seed43 已完成，SR=77.2%，结果存于 `eval_results/pi05_attention_k0.95_libero_10_seed43.json`。defunct 进程仍占 GPU 内存。

2. **GPU3 双实验冲突** — `cascade_gpu3.sh` 在原 L2norm k=0.7 仍在运行时就启动了 L2norm k=0.95（cascade 等的是旧 PID 608185 而非当前进程）。两个实验共享 GPU3，各用 ~10.8GB，内存够但互相争抢算力。

3. **可操作项**：GPU1 空闲可部署新实验；GPU3 的两个实验虽然在跑但会比预期慢（互相竞争）。

---
