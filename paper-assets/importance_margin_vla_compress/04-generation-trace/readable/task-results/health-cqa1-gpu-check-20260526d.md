# health cqa1 gpu check 20260526d

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_health_cqa1-gpu-check-20260526d_20260526T221154_result.json`
- **Structured JSON:** [`ca91152f1bfa6fcf409c.json`](../../sessions/ca/ca91152f1bfa6fcf409c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在正常推进。汇总：

```
GPU 0: 正常  Util=71%  Mem=15964/97887MiB  Temp=51°C  PID=499267  运行1h24m  CPU=696%
       任务: attention_prune k=0.75 libero_goal  日志: Task 4/10 Ep40/50 sr=13/40 (2.3 eps/min)

GPU 1: 正常  Util=70%  Mem=16212/97887MiB  Temp=53°C  PID=397225  运行6h14m  CPU=718%
       任务: attention_prune k=0.5 libero_10   日志: Task 7/10 Ep40/50 sr=5/40 (0.9 eps/min)

GPU 2: 空闲  无进程
GPU 3: 空闲  无进程
```

**结论：无卡死。** 但实际只有 2 张 GPU 在跑（GPU 0、1），GPU 2 和 GPU 3 完全空闲——任务描述中提到的 4 个进程（PID 617566/617728/582964/732826）已不存在，可能已完成或被终止。当前 2 个实验都在正常推进，利用率 70%+ 属于健康范围。

---
