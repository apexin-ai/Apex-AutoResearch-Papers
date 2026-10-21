# check olmo depth chain data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_olmo_depth_chain_data_20260516T152747_result.json`
- **Structured JSON:** [`0fac22e733d7d70ce6d1.json`](../../sessions/0f/0fac22e733d7d70ce6d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### OLMo depth chain 数据：**不存在**

服务器上没有任何 `olmo`、`exp_002`、`exp002` 相关文件。搜索了整个项目目录（含 `/root/autodl-tmp` 顶层），结果为空。

现有的 depth chain 数据集是：
- `data_exp016_qwen_base` — Qwen base
- `data/exp_018_llama8b` — LLaMA-8B
- `data_exp019_mistral7b` — Mistral-7B
- `data_exp019b_mistral_cross` — Mistral cross
- `data_exp020_pythia_*` — Pythia (greedy / nuc09 / t07 / t12)
- `data/exp_021_length_*` — 长度消融 (128/256/512)
- `data/exp_023_wiki` — Wiki 域
- `data/exp_024_arxiv` — ArXiv 域 (进行中)
- `data_exp022_cross_scorer/qwen_base__qwen_base` — cross-scorer

exp-002 的 OLMo-1B 数据需要重新生成或从其他位置恢复。

### exp-024 进度

已完成 depth 0-2（各 2200 行），depth 3-5 尚未生成。

### GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 0 MiB | 0% | 空闲 |
| cuda:1 | 0 MiB | 0% | 空闲 |
| cuda:2 | 3819 MiB | 70% | python (PID 48295) |
| cuda:3 | 4617 MiB | 72% | python (PID 50725) |

cuda:2 和 cuda:3 都在跑任务。

---
