# diagnose eval pi05 l2norm k09 long seed42 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k09_long_seed42_strict_cqa1_20260527T141454_result.json`
- **Structured JSON:** [`cdbd26627e4cdef1048c.json`](../../sessions/cd/cdbd26627e4cdef1048c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际上已成功完成，不是失败。**

### 根因：日志路径不匹配

Cron 监控查找的路径是 `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_long_seed42_strict_cqa1.log`，但实际日志写入了 `/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_l2norm_k09_long_seed42_strict_cqa1.log`（项目根目录）。Cron 找不到日志文件，误判为进程未启动/失败。

### 实验结果

实验于 **18:26 启动，21:59 完成**（约 3.5h），结果：

> **LIBERO-10 l2norm k=0.9 seed42 SR=80.0%**

各 task 成绩：96%, 96%, 94%, 100%, 82%, 96%, 6%, 92%, 44%, 94%

结果已保存至 `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_10_seed42.json`

### GPU 状态

4 卡全部在用，无空闲：
- **GPU 0**: PID 300492 (python)
- **GPU 1**: PIDs 328563 + 330514 (2 个 python)
- **GPU 2**: PID 274739 — l2norm k=0.7 long seed42 (运行中)
- **GPU 3**: PID 386864 — l2norm k=0.9 long **seed43** (刚启动，正在跑)

### 磁盘

根分区 30% (22GB free)，无磁盘问题。

### 结论

无需重跑——seed42 实验已完成，结果 80.0% SR。Cron 误报是因为日志路径写到了项目目录而非 `~/runs/` 监控目录。

---
