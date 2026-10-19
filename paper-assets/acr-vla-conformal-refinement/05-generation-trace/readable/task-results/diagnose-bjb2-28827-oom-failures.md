# diagnose bjb2 28827 oom failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb2-28827-oom-failures_20260519T165209_result.json`
- **Structured JSON:** [`825a8c56d2d92cd32ba5.json`](../../sessions/82/825a8c56d2d92cd32ba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集完所有可获取的诊断信息。

---

## 诊断报告：SIGKILL (EXIT_CODE=137) 失败分析

### 一、失败原因判断：**平台级外部 kill，非 OOM**

依据：
- **内存充裕**：服务器总内存 1TB，当前仅用 113GB，可用 840GB — 不存在系统内存不足的条件
- **无 OOM 日志**：AutoDL 容器无 `/var/log/syslog` 和 `/var/log/kern.log`，`dmesg` 也不可用，但从内存状况看 OOM killer 可能性极低
- **两个进程几乎同时被杀**：分别运行在 cuda:1 和 cuda:3 上，两个独立进程同时收到 SIGKILL，指向外部统一 kill 行为（而非各自独立的资源耗尽）
- **GPU 显存无异常**：当前 GPU 0-4 全部 1MiB 空闲，不存在显存泄漏残留

**最可能原因：AutoDL 平台维护/实例级操作** — 可能是实例重启、资源回收、或平台调度导致进程被统一 kill。

### 二、进度

| 实验 | 总任务数 | 已完成任务 | 中断位置 | 进度 | 输出文件 |
|------|---------|-----------|---------|------|---------|
| eval-argmin-object-k5-seed44 | 10 | 9 | 第10个任务 rollout 8/10 | ~98% | **不存在**（未写入） |
| eval-obs-only-spatial-norm02-seed46 | 10 | 8 | 第9个任务完成后被杀 | 80% | **不存在**（未写入） |

两个实验的 JSON 输出文件均不存在 — 脚本在全部任务完成后才写入结果文件，中途被杀导致全部进度丢失。

### 三、当前服务器资源状况

| 资源 | 状态 |
|------|------|
| GPU | 6× RTX 4090 (24GB)。GPU 0-4 完全空闲；GPU 5 被 `calibrate_fmvd.py` 占用 (5.7GB) |
| 系统内存 | 1TB 总量，113GB 已用，840GB 空闲 |
| 根分区磁盘 | 30GB 中已用 13GB (43%) |
| 其他进程 | 正在下载 openvla-7b-finetuned-libero-object 模型（HF + wget 并行） |

### 四、是否可以安全重跑

**可以**。GPU 0-4 全部空闲，内存充裕。但需注意：
- GPU 5 正在运行 `calibrate_fmvd.py`，避免与其冲突
- 正在进行 openvla 模型下载，等下载完成后再跑 object benchmark 实验（它依赖 openvla 模型）

### 五、建议

- **不需要调整 batch size 或参数** — 这不是 OOM 问题，资源完全充足
- **建议为 evaluate.py 添加增量保存机制** — 当前脚本在全部任务完成后才写 JSON，一旦中途被杀就丢失全部结果。可以改为每完成一个 task 就追加写入，避免重复劳动
- 重跑前建议确认 AutoDL 实例无计划维护/重启

---
