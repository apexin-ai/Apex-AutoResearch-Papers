# exp qwen7b 8k spotcheck

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen7b_8k_spotcheck_20260515T130833_result.json`
- **Structured JSON:** [`c285d9e0370a9ba550ff.json`](../../sessions/c2/c285d9e0370a9ba550ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中。数据集已加载两次 = bf16 baseline 完成 + MCKP eval 进行中。Python stdout 缓冲导致部分结果未立即显示。

**当前状态**：
- Experiment: `qwen7b_8k_spotcheck` — **RUNNING** on cuda:1 (westd-37397)
- Registry: RUNNING
- GPU memory: 44.7GB / 96GB
- 3 次 eval（bf16 baseline / MCKP / uniform 4-bit），每次 ~36 chunks @ 8K tokens
- 预计总运行时间 30-45 分钟
- 输出: `/root/ratekv/artifacts/qwen7b_8k_spotcheck_results.json`
- 日志: `/root/ratekv/logs/qwen7b_8k_spotcheck.log`

---
