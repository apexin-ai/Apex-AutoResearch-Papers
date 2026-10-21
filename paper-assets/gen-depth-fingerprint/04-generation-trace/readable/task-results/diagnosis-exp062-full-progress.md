# diagnosis exp062 full progress

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_full_progress_20260521T112828_result.json`
- **Structured JSON:** [`b5008369c21057ce245d.json`](../../sessions/b5/b5008369c21057ce245d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_062 进度汇报

### GPU 状态
| GPU | 利用率 | 显存 | 运行模型 |
|-----|--------|------|----------|
| 0 | 91% | 13.0 GB | pythia-2.8b (topk) + llama-3.2-3b (greedy) |
| 1 | 41% | 3.9 GB | qwen3-1.7b (greedy) |
| 2 | 87% | 14.6 GB | mistral-7b-v0.3 (greedy) |
| 3 | 50% | 2.6 GB | pythia-1b (topk) |

### 各 generator × strategy 进度

| 模型 | greedy | topk | 备注 |
|------|--------|------|------|
| **olmo-2-1b** | **DONE** (4879 lines) | **DONE** (4641 lines) | 全部完成 |
| **pythia-2.8b** | **DONE** (4854 lines) | 882/995 seeds (89%) | topk ~19min 完成 |
| **pythia-1b** | **DONE** (4867 lines) | 198/995 seeds (20%) | topk ~60min 完成 |
| **qwen3-1.7b** | 834/996 seeds (84%) | 未开始 | greedy ~38min，topk ~4h |
| **llama-3.2-3b** | 437/995 seeds (44%) | 未开始 | greedy ~2.4h，topk ~4.4h |
| **mistral-7b-v0.3** | 427/996 seeds (43%) | 未开始 | greedy ~2.2h，topk ~3.8h |

**统计：12 组合中 4 完成 / 5 进行中 / 3 未开始**

### 已完成输出路径
- `/root/gen-depth-fingerprint/data/olmo-2-1b-greedy/generations_shard0.jsonl`
- `/root/gen-depth-fingerprint/data/olmo-2-1b-topk/generations_shard0.jsonl`
- `/root/gen-depth-fingerprint/data/pythia-2.8b-greedy/generations_shard0.jsonl`
- `/root/gen-depth-fingerprint/data/pythia-1b-greedy/generations_shard0.jsonl`

### 辅助进程
- `extract_after_pythia.sh` — 等待 pythia-2.8b topk 完成后自动提取特征
- `start_cuda3_chain.sh` — 等待 pythia-1b topk 完成后触发后续任务

### 预计全部完成时间

瓶颈在 GPU 0（llama + pythia 共享）。pythia-2.8b topk ~19min 后完成释放显存，llama 独占 GPU 0 后会加速。

保守估计：**全部 12 组合完成约需 6-7 小时**，即 **5 月 22 日凌晨 01:30 - 02:30 CST**。

---
