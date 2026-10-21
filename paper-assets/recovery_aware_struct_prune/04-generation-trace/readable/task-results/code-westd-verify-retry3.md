# code westd verify retry3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-verify-retry3_20260515T134324_result.json`
- **Structured JSON:** [`1167ea8d3e02721bf0e2.json`](../../sessions/11/1167ea8d3e02721bf0e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### sft_alpha4_0_westd_retry — **已失败 (EXIT_CODE=2)**
- pid 37013 **不存在**，进程已退出
- 失败原因：`unrecognized arguments: --save_strategy no --overwrite_output_dir`
- `sft_recovery.py` 不支持 `--save_strategy` 和 `--overwrite_output_dir` 参数
- GPU 1 当前完全空闲 (0 MiB, 0% utilization)

### grasp_baseline_westd — **正常运行中**
- pid 34195 存在，实际 GPU 进程 pid 为 34206，在 GPU 0 上运行
- 显存占用：13070 MiB / 97887 MiB，GPU 利用率 90%
- 评测进度：66/1319 (5%)，每样本约 50.9s，预计还需约 17.7 小时
- 50 样本处 acc=0.0800, eos_rate=2.00%, avg_len=4019（accuracy 很低，eos_rate 极低说明模型几乎不停止生成）

### 异常进程
无异常残留进程。

### 需要处理
sft_alpha4_0_westd_retry 需要第 4 次重试——从 `sft_recovery.py` 的启动命令中移除 `--save_strategy no` 和 `--overwrite_output_dir` 这两个不支持的参数。

---
