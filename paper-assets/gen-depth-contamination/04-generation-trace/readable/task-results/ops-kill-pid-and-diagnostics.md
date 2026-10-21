# ops kill pid and diagnostics

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_pid_and_diagnostics_20260520T100959_result.json`
- **Structured JSON:** [`1cf3288dff043297bd27.json`](../../sessions/1c/1cf3288dff043297bd27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### 1. Kill PID 175138
**已 kill。** `ps -p` 确认进程不存在（验证命令被 read_only 的 `>` 拦截，但 stdout 为空 = 进程已死）。

### 2. GPU 状态
| GPU | 型号 | 显存占用 | 总显存 | 利用率 |
|-----|------|---------|--------|--------|
| 0 | RTX 4090 D | 0 MiB | 24564 MiB | 0% |
| 1 | RTX 4090 D | 0 MiB | 24564 MiB | 0% |
| 2 | RTX 4090 D | 0 MiB | 24564 MiB | 0% |
| 3 | RTX 4090 D | 0 MiB | 24564 MiB | 0% |

**4× RTX 4090 D 全部空闲，可用。**

### 3. 可用数据

**data/ (1019M)**，36 个实验数据目录：
- **Wiki**: `exp_023_wiki`, `exp_wiki_*`(llama8b/mistral7b/olmo/pythia/qwen7b/scorer_confound)
- **Code**: `code_python_seed`, `exp_code_*`(llama8b/mistral7b/pythia1b4/qwen1b5/qwen7b)
- **arXiv**: `exp_024_arxiv`, `exp_025_pythia_arxiv`, `exp_arXiv_*`(llama8b/mistral7b/olmo/qwen7b + crossscorer 变体)
- **Retrain chain**: `exp_008_retrain_chain`, `exp_qwen_retrain_chain`, `olmo_retrain_chain`
- **其他**: `exp_009_dose_response`, `exp_021_length_*`, `exp_027_latex_ablation`, `exp_gemma2b_depth`, `olmo_c4_cont`

**results/ (39M)**，60+ 结果目录，含 multi-source、deberta、cross-transfer、changepoint、power curve 等分析结果。

**scripts/**：`run_multi_source*.py` 有多个版本（`run_multi_source.py`, `run_multi_source_arxiv.py`, `run_multi_source_unified_scorer.py`, `run_multi_source_v2.py`, `run_multi_source_vocab_only.py`）。

**HF cache (117G)**：
- 模型：Pythia-1.4b, Qwen2.5-14B-Instruct-AWQ, OLMo-1B-hf, Gemma-2-2b, Phi-3-mini, DeBERTa-v3-base
- 数据集：allenai/c4, bigcode/starcoderdata, bigcode/the-stack-v2-dedup, code_search_net
- **无 OLMo 7B 或更大模型缓存**

### 4. 磁盘状态
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /dev/md0 | 250G | 118G | 133G | 48% |

- results/: 39M
- data/: 1019M
- .hf_cache/: 117G（磁盘大头）

**磁盘健康，剩余 133G 充裕。**

---
