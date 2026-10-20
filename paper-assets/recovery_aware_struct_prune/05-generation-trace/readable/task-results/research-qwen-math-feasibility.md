# research qwen math feasibility

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen_math_feasibility_20260520T042433_result.json`
- **Structured JSON:** [`2e61e3a72ed21426ab8d.json`](../../sessions/2e/2e61e3a72ed21426ab8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 中期评估报告

### 适配复杂度：**简单（零代码修改）**

| 检查项 | 结果 |
|--------|------|
| 架构兼容性 | 完全一致：Qwen2ForCausalLM, 28层, 28头, 4 KV头, hidden=3584, intermediate=18944 |
| prune.py | 通用 AutoModel + `model.model.layers[i]` 命名，兼容 |
| cka_overlap.py | 通用 hook 机制，兼容 |
| importance_score.py | 通用 gradient-based scoring，兼容 |
| rasp_scoring.py | 纯 tensor 数学，模型无关 |
| sft_recovery.py | 通用 SFTTrainer + chat_template，兼容 |
| train_grpo_v5.py | 通用 GRPOTrainer + monkey-patch，兼容 |
| eval_gsm8k.py | 多级 answer extraction (boxed/####/数字)，兼容 |
| 硬编码路径 | 核心 pipeline 无硬编码，全部通过 `--model_path` 传入 |

### 阻塞项：磁盘空间不足

| 项目 | 大小 |
|------|------|
| 数据盘总量 | 250 GB |
| 当前已用 | 230 GB (含正在下载的 6 GB) |
| 下载完成后剩余 | **~6 GB** |
| 完整 pipeline 需要 | **~60 GB** (2 pruned + 2 SFT + 2 GRPO @ ~12 GB each) |
| **缺口** | **~54 GB** |

### 可清理候选项（按 D005 决策，25% sparsity 已被放弃）

| 目录 | 大小 | 理由 |
|------|------|------|
| `pruned_rasp_25` | 11 GB | D005 放弃 25% sparsity |
| `sft_rasp_25` | 11 GB | 同上 |
| `grpo_rasp_25` | 11 GB | 同上 |
| `pruned_standard_25` | 11 GB | 同上 |
| `sft_standard_25` | 11 GB | 同上 |
| `pruned_random_20` | 12 GB | Random baseline，结果已记录 |
| `sft_random_20` | 12 GB | 同上 |
| `sft_gradient_20` | 12 GB | Gradient baseline SFT |
| **合计** | **~91 GB** | |

清理上述即可腾出足够空间。需要你确认哪些可以删除。

---
