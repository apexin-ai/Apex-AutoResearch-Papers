# ssh full status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_check_20260522T210649_result.json`
- **Structured JSON:** [`fd565437029ad7ae1432.json`](../../sessions/fd/fd565437029ad7ae1432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### autodl-8gpu

| GPU | 实验 | 状态 | 进度 | GPU利用率 | 预估剩余 |
|-----|------|------|------|-----------|----------|
| cuda:0 | refit exp-003b | **运行中** | sampling 5700/8000 (71%), 4.30 it/s, acc.prob=0.97 | 76%, 667 MiB | **~9 min** |
| cuda:1 | exp-006 full | **运行中** | [20/31] judge组合, sampling 1560/3000 (52%), 5.41 it/s | 68%, 863 MiB | 当前组合~4.5min，整体还剩~11个组合，**~2-3 hr** |
| cuda:2 | W7 ablation | **运行中** | [9/20] seed=8, 正在跑 full_gmfrm（第1/4变体）| 68%, 2749 MiB | 每seed~19min, 剩~11 seeds, **~3.5 hr** |
| cuda:3 | — | **空闲** | — | 0%, 0 MiB | — |

**额外发现：**
- **exp-005**: 已完成，tmux session 仍在。结论：joint_gmfrm 和 joint_gmfrm_003b 的 c_n 接近 MVP-002 (strong)，sequential 接近 MVP-001 (weak)
- **Qwen2.5-7B responses**: 已完成，500 条，文件 1.67MB (`qwen2.5-7b.jsonl`)

---

### rtx6000-4x

| GPU | 实验/任务 | 状态 | 进度 | GPU利用率 | 预估剩余 |
|-----|-----------|------|------|-----------|----------|
| cuda:0 | exp-009 OVB | **运行中** | Part A 已完成 (70078s). Part B: [10/50] seeds, ~195s/seed | 68%, 74.6 GB | **~2.2 hr** |
| cuda:1 | vllm-mistral + judge-mistral | **运行中** | judge collect [5460/8742], 0.2 items/s | 96%, 90.2 GB | **~5.2 hr** |
| cuda:2 | vllm-llama + judge-llama | **运行中** | judge collect [1980/8311], 0.1 items/s | 100%, 91.0 GB | **~20.8 hr** |
| cuda:3 | judge-qwen (via API?) | **运行中** | judge collect [8030/8534], 0.3 items/s | 97%, 90.0 GB | **~33 min** |

**Judge collection 详情：**
- **qwen2.5-72b**: 8030/8534 → 即将完成 (~33 min)
- **mistral-large-2**: 5460/8742 → ~5.2 hr
- **llama-3.3-70b**: 1980/8311 → 最慢，~20.8 hr（速度仅 0.1 items/s）

**注意：** llama judge 速度异常慢（0.1 items/s vs qwen 的 0.3 items/s），可能受 vllm 推理或 8192 max-model-len 限制。exp009 结果目录尚未创建，输出可能在内存中或运行结束后统一写入。

---
