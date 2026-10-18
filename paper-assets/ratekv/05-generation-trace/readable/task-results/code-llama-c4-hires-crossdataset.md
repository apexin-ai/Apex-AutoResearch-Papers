# code llama c4 hires crossdataset

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-c4-hires-crossdataset_20260514T221727_result.json`
- **Structured JSON:** [`9cbe182d8fbd94da7b43.json`](../../sessions/9c/9cbe182d8fbd94da7b43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/run_llama_c4_hires_crossdataset.py`

**设计**：
- **Phase 1 (新做)**：C4 hires 2-bit profiling，64×2048 bf16 inline `patch_attention` 循环（同 `run_llama_hires_bf16_2bitonly.py` 套路）→ 保存 `llama_c4_hires_bf16_2bitonly_profiles.json`
- **Phase 2 (默认复用)**：C4 standard 4/8-bit profiles 从 `llama_c4_cross_dataset_results.json` 的 `c4_profiles` 字段读（16×512）；`--fresh-standard` 可强制重新 profile
- **Phase 3–4**：merge → `enforce_monotonicity` → `solve_mckp_constrained(budget=0.25, max_2bit=2, l0_exclude_2bit=True)`
- **Phase 5**：WT2 PPL（`evaluate_perplexity`）+ C4 PPL（自定义 forward pass）各跑 BF16 / MCKP / uniform-4bit 三种
- **Phase 6**：和 `llama_hires_constrained_results.json` 的 WT2 hires 参考对比（baseline 8.0922 / MCKP 8.5042 / uniform 8.4701 / delta -0.0341，FAIL）

**Flags**：
- `--device cuda:0`（默认；提醒不要用 cuda:1）
- `--reuse-hires`：跳过 Phase 1 复用已有 hires profiles
- `--fresh-standard`：不复用，重新 inline profile 4/8-bit

**服务器验证完成**：
- Model `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B`（symlink → `Meta-Llama-3___1-8B`）有完整 safetensors
- `c4_calibration_real.json` (371KB)、`llama_c4_cross_dataset_results.json`、`llama_hires_constrained_results.json`、`solver.py`/`eval_ppl.py`/`full_bitwidth_profiler.py` 都存在
- 架构：32L × 8KV = 256 heads，GQA 4:1

未提交运行，等 Mistral 完成后再提交。

---
