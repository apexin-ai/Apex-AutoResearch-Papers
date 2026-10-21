# monitor 30476 probe 25min

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_30476_probe_25min_20260517T131752_result.json`
- **Structured JSON:** [`f2adbd092688da6d17ec.json`](../../sessions/f2/f2adbd092688da6d17ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控完成

```
监控记录：
T+5min:  PID=存活(18m15s), step=517,  RSS=3.5MB, GPU=46505MiB/70%,  系统内存=82Gi/1Ti
T+10min: PID=存活(25m00s), step=684,  RSS=3.5MB, GPU=46505MiB/99%,  系统内存=72Gi/1Ti
T+15min: PID=存活(30m13s), step=829,  RSS=3.5MB, GPU=46505MiB/67%,  系统内存=74Gi/1Ti
T+20min: PID=存活(35m22s), step=972,  RSS=3.5MB, GPU=46505MiB/98%,  系统内存=73Gi/1Ti
T+25min: PID=存活(40m30s), step=1112, RSS=3.5MB, GPU=46505MiB/94%,  系统内存=77Gi/1Ti

最终判断：✓ 探针通过，可以提交其余 3 个实验
```

**关键观察：**
- 进程已稳定运行 40 分钟，远超之前 4 实验被杀的 ~20 分钟点
- step=1112 > 600（预期目标），训练速度稳定 ~2.1s/step
- GPU 内存恒定 46505MiB，系统内存在 72-82Gi 范围波动，无泄漏迹象
- 结论：之前的 SIGKILL 确为多卡并行导致，单卡运行无问题。可安全提交剩余 3 个实验（建议仍逐个提交到不同 GPU，避免同时 4 卡跑满）

---
