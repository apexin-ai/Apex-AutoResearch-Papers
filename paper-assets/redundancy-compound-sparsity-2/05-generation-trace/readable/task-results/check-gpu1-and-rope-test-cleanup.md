# check gpu1 and rope test cleanup

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu1_and_rope_test_cleanup_20260512T173449_result.json`
- **Structured JSON:** [`accf083bef29dc8e4bfa.json`](../../sessions/ac/accf083bef29dc8e4bfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### GPU 1 占用者
**PID 44339** — `python analysis_heatmap.py --device cuda:0 --seq-len 4096`，运行 3 分 48 秒，占 GPU 1 仅 **740 MiB**（非 28.7 GB）。当前 GPU-Util 45%，正在活跃计算。

之前看到的 28.7 GB 占用已经消失。现在 GPU 1 几乎是空的（749 MiB / 97887 MiB）。

### GPU 0 占用者
**PID 40063** — `python analysis_gamma_sweep.py --model ... --gpu 0`，运行 1 小时 2 分钟，占 GPU 0 **31.7 GB**。

### carc_generate_rope_test 状态
- **PID 18305 已不存在**
- 日志显示正常完成：生成了 100 tokens (14.0 tok/s)，evictions=0，**EXIT_CODE=0**
- 状态：**已正常完成**，可以在 registry 中标记为 COMPLETED

### analysis_heatmap
- **正在 GPU 1 上运行**（PID 44339），刚启动约 4 分钟
- 脚本存在于 `/root/carc/analysis_heatmap.py`

### 需要清理的进程
- **无**。两个正在运行的进程都是活跃的分析任务
- carc_generate_rope_test 已自然结束，无残留进程

---
