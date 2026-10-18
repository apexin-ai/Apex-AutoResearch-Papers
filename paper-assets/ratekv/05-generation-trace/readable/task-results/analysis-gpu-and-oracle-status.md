# analysis gpu and oracle status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu_and_oracle_status_20260514T114359_result.json`
- **Structured JSON:** [`5871d6773929c69211bd.json`](../../sessions/58/5871d6773929c69211bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### GPU 状态
两张 RTX PRO 6000 (96GB) **完全空闲**，GPU 利用率 0%，显存占用 0 MiB。无 Python/训练进程在运行。

### Oracle Comparison
**已完成**，结果在 `/root/ratekv/oracle_comparison_results.json`。

关键结果：
- **MCKP PPL**: 10.9131（budget=0.25）
- 28 层中 8 层有替代方案（54 次 PPL 评估，耗时 21.3 min）
- **Max gap**: 0.0183 PPL（layer 11）
- **Avg gap**: 0.0046 PPL
- 结论：**MCKP 接近最优**，per-layer exhaustive search 几乎找不到改进，验证了 additive distortion model 的有效性

### 活跃进程
仅有系统服务（supervisord, jupyter-lab, tensorboard, sshd, autopanel），无训练任务。

Registry 已更新为 `DONE/success`。GPU 空闲可用于下一个实验。

---
