# diag exp 001 eval 05B d100 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_eval_05B_d100_v2_20260514T023914_result.json`
- **Structured JSON:** [`651bf828a801420a25d1.json`](../../sessions/65/651bf828a801420a25d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 失败根因：**系统 RAM（cgroup 内存限制）OOM，非 GPU OOM**

证据链：
1. **EXIT_CODE=137** = SIGKILL，是 Linux OOM killer 发出的。GPU OOM 会在 Python 层报 `CUDA out of memory` 错误，不会被 kernel 杀。
2. **cgroup 内存上限 480GB**（`memory.max = 515396075520`），当前已降到 126GB / 480GB。
3. 每次被杀的进度递减：v2 到 82%、v3 到 45%、v4 到 38%、v5 到 5% —— 说明并发进程越来越多，可用内存越来越少。
4. **d005 eval 成功通过了 MMLU**，目前在跑 GSM8K（37%）。它启动时间早（09:17），并发少。
5. d100 的多次重试都在 10:28-10:40 期间启动，此时同时有大量 eval 进程：d000_s42_v2/v3/v4/v5、d100_v2/v3/v4/v5、1.5B eval、3B eval 等，十几个进程共享 480GB cgroup 限制。

### 代码层面无问题

evaluate.py 的 MCQ 路径是逐条处理的（`compute_choice_logprobs` 一次一条），`per_item` 列表内存占用极小。`batch_size=8` 参数在 MCQ 评估中实际未使用。代码本身不存在内存泄漏。

### 当前服务器状态

| 资源 | 状态 |
|------|------|
| cgroup 内存 | 126GB / 480GB（充裕） |
| GPU 0 | 10055MiB / 24564MiB（被占用） |
| GPU 1 | 12620MiB / 24564MiB（被占用，两个进程） |
| **GPU 2** | **0MiB / 24564MiB（完全空闲）** |
| GPU 3 | 8957MiB / 24564MiB（被占用） |
| GPU 4 | 5829MiB / 24564MiB（被占用） |
| GPU 5 | 5829MiB / 24564MiB（被占用） |
| d100_s42 结果 | **空目录，无任何部分结果** |

### 建议修复方案

1. **现在重跑**：当前 cgroup 内存仅用 126GB，远低于 480GB 限制，有充足空间。
2. **指定 GPU 2**：`CUDA_VISIBLE_DEVICES=2` 使用空闲 GPU，避免与 device 0 上的进程共享显存。
3. **控制并发**：不要同时启动多个 eval 进程，串行执行或限制最多 2-3 个并发。
4. batch_size 不需要改 —— MMLU/ARC 的 MCQ 评估本身就是逐条推理的，batch_size 参数对这个路径无效。

---
