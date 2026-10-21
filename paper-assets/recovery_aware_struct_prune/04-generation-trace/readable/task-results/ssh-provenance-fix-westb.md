# ssh provenance fix westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_provenance_fix_westb_20260523T112649_result.json`
- **Structured JSON:** [`67ed376b05292b47e877.json`](../../sessions/67/67ed376b05292b47e877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有更新完成。汇报如下：

---

## 任务 1: MATH-500 Standard 25% GRPO = 12.8%

**已确认**。文件路径：`/root/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_25_v2/results.json`
- accuracy=0.128, 64/500
- Registry `eval_math500_grpo_standard_25_v2` 的 checkpoint_path 和 log_path 已有，已补填 `result_path`

## 任务 2: 补填 3 个空 metrics

| exp_id | 结果 | 来源 |
|--------|------|------|
| `eval_gsm8k_grpo_random_20_seed123_v2` | accuracy=0.5072, 669/1319 | 从 spec 字段提取，已写入 metrics。**westb 无结果文件**，原始运行在 westd-32935 |
| `eval_gsm8k_sft_depth_first_20` | ~10%@50 (early-stopped) | spec note 提取。**westb 无文件**，原始运行在 westd-32935 |
| `eval_gsm8k_grpo_depth_first_20` | ~8%@50 (early-stopped) | spec note 提取。**westb 无文件**，原始运行在 westd-32935 |

三个 depth-first/random seed123 的 eval 均在 westd 上运行，westb 上未找到对应结果文件。

## 任务 3: 30% cliff CKA-only

Registry 已有两条记录：
- `eval_postprune_cka_only_30`: gsm8k_accuracy=**0.0%** (westd-11672, killed)
- `prune_eval_cka_only_30`: accuracy=**1.6%** (N=500 partial, westd-29022, killed)

**westb 上未找到 30% CKA-only 相关结果文件。**

## 任务 4: Qwen-Math 缺失值

| 指标 | 文件 (westb) | 数值 | Registry |
|------|-------------|------|----------|
| CKA Post-Prune | `results/gsm8k_postprune_cka_only_20_qwen_math_n200.json` | **1.0%** (2/200) | 新建 `eval_postprune_qwen_math_cka_only_20` |
| CKA Post-SFT | `results/eval_gsm8k_sft_qwen_cka_only_20.json` | **51.5%** (103/200) | 已有 `eval_gsm8k_sft_qwen_cka_only_20` |
| Standard Post-Prune | `results/gsm8k_postprune_standard_20_qwen_math_n200.json` | **18.5%** (37/200) | 新建 `eval_postprune_qwen_math_standard_20` |

---
