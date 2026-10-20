# code gpu check 047

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-check-047_20260517T064504_result.json`
- **Structured JSON:** [`95fbe38539405f5368df.json`](../../sessions/95/95fbe38539405f5368df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状态报告

### nvidia-smi 摘要

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| cuda:0 | 3 MiB / 32607 MiB | 0% | 无 |
| cuda:1 | 3983 MiB / 32607 MiB | 40% | python (PID 383837) |
| cuda:2 | 14671 MiB / 32607 MiB | 87% | python (PID 383838) |
| cuda:3 | 0 MiB / 32607 MiB | 0% | 无 |

进程为 `run_experiment_t07.py` 的 multiprocessing 子进程，`CUDA_VISIBLE_DEVICES=0,1,2`。cuda:0 当前空闲（可能刚释放完一个模型）。

### tmux session 状态

`multi_domain_t07` session 存在（创建于 13:54:55 UTC）。主进程正常运行中。

### 生成进度

| 文件 | 行数 | 状态 |
|------|------|------|
| mistral-7b_academic | 768 / 800 | 进行中 |
| mistral-7b_news | 800 / 800 | 完成 |
| pythia-1b_academic | 800 / 800 | 完成 |
| pythia-1b_code | 800 / 800 | 完成 |
| pythia-1b_news | 800 / 800 | 完成 |
| qwen3-1.7b_academic | 778 / 800 | 进行中 |
| qwen3-1.7b_news | 800 / 800 | 完成 |
| **mistral-7b_code** | 未出现 | 未开始 |
| **qwen3-1.7b_code** | 未出现 | 未开始 |

**总进度：5546 / 7200 行（77%）**

最新日志显示 `pythia-1b_code` 刚完成（800 records），GPU 已释放。当前 cuda:1/2 上在跑的应该是 mistral-7b 或 qwen3-1.7b 的剩余任务。剩余约 2 个文件未开始 + 2 个文件进行中，预计还需一段时间完成。

---
