# check gpu status and mistral

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_and_mistral_20260515T144742_result.json`
- **Structured JSON:** [`f6ce3e26cfa83505ae4c.json`](../../sessions/f6/f6ce3e26cfa83505ae4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**GPU 状态**
| GPU | 型号 | 显存 | 利用率 | 进程 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 0MiB | 100% | 无 |
| 1 | RTX PRO 6000 Blackwell (96GB) | 0MiB | 0% | 无 |

GPU 0 显示 100% utilization 但 0MiB 显存且无进程，可能是刚结束任务的残留状态或驱动异常，实际应为空闲。GPU 1 完全空闲。**两张卡无实验进程占用。**

**Python 进程**：无实验进程运行。仅有系统服务（jupyter-lab、tensorboard、autopanel、supervisord）。

**tmux session**：存在 `gemma2_9b_full_pipeline` session（00:50 创建），但内部无活跃实验进程。

**Mistral hires 结果**：
- **结果文件已完整**（`mistral_hires_bf16_2bitonly_results.json`，May 15 06:33）
- 全部 256 heads profiled，耗时 ~56 分钟
- baseline PPL = 5.870
- Top-5 sensitive heads 占总 delta 的 24.1%
- 最敏感 head：L2H5 (delta=0.324)，L12H1 (0.144)，L0H7 (0.140)
- 252/256 heads 有正 delta（几乎所有 head 量化到 2bit 都有损失）
- v3 日志显示只跑到 39/256 就停了，说明 v3 是后续重跑但被中断，**最终结果来自之前的完整运行**

---
