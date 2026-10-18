# infra check gpu status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-gpu-status_20260513T203129_result.json`
- **Structured JSON:** [`7d255378c3872f906756.json`](../../sessions/7d/7d255378c3872f906756.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. nvidia-smi 完整输出

```
Thu May 14 04:31:46 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |
| N/A   28C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   31C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

**GPU 0 和 1 均 0% 利用率，0MiB 显存占用，无 GPU 进程。**

### 2. tmux sessions

无 tmux session（`/tmp/.tmux*` 不存在）。

### 3. 进程状态

- **PID 131672, 131751（原始实验进程）**: **已死亡**，ps 中不存在。
- **PID 130821（当前活跃进程）**: 一个 `python3 -c` 正在用 CPU **流式下载 C4 calibration 数据**（占 82.6% CPU，14% 内存 ≈ 148GB RSS），从 03:52 开始已运行约 40 分钟。这不是实验进程，是数据准备。

### 4. 日志

**mvp_002.log** — **已崩溃**，错误：
```
IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes [0], [3584]
```
发生在 `torch._dynamo` / `vmap` / `autograd_function` 的嵌套调用链中，`torch.ops.aten.index(x, indices)` 时索引张量 shape `[0]` 与 `[3584]` 不匹配。EXIT_CODE=0。

**sanity_002.log** — **启动即失败**，错误：
```
run_mvp.py: error: unrecognized arguments: --output sanity_results.json
```
`run_mvp.py` 不接受 `--output` 参数，argparse 直接拒绝。

### 5. 本地日志

- `mvp_run.log` — 与 `mvp_002.log` 相同的 IndexError 崩溃。
- `mvp_sanity.log` — 与 `sanity_002.log` 相同的参数错误。

### 6. calibration 数据文件

```
-rw-r--r-- 1 root root 66K May 14 03:55 /root/ratekv/c4_calibration.json
```
**存在，66KB，生成于 03:55。** 但当前仍有一个 python3 进程在流式下载 C4（PID 130821），可能是重复执行或卡住。

---

### 总结

| 实验 | 状态 | 崩溃原因 |
|------|------|----------|
| mvp_002 | **死亡** | `IndexError: shape mismatch [0] vs [3584]`，torch vmap/dynamo 中索引张量 shape 不匹配 |
| sanity_002 | **启动失败** | `unrecognized arguments: --output`，run_mvp.py 不支持 `--output` 参数 |

两个实验均已终止，GPU 完全空闲。当前唯一活跃进程是 C4 calibration 数据下载（CPU-only，PID 130821）。

---
