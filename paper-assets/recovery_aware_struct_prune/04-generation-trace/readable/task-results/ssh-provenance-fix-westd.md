# ssh provenance fix westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_provenance_fix_westd_20260523T110636_result.json`
- **Structured JSON:** [`f2a34db35cfc6c0ce1c9.json`](../../sessions/f2/f2a34db35cfc6c0ce1c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1: MATH-500 Standard 25% GRPO = 12.8%
**westd-32935 上未找到结果文件。** 没有 `math500*grpo*standard*25*` 文件。

现有 25% standard 文件：
| 文件 | accuracy | n_total | 实际是什么 |
|------|----------|---------|-----------|
| `eval_grpo_standard_25.json` | 63.5% | 200 | qwen_math eval |
| `eval_grpo_standard_25_n1319.json` | 51.1% | 1319 | GSM8K eval |
| `eval_postprune_standard_25.json` | 16.0% | 100 | post-prune (无recovery) |

Registry 中 `eval_math500_grpo_standard_25_v2` **已有** accuracy=0.128, n_correct=64, n_total=500。原始 `eval_math500_grpo_standard_25` 状态为 killed。该结果文件可能在 westb-23072。

---

### 任务 2: 补填 3 个空 metrics
**三个结果文件均未在 westd-32935 上找到：**
- `eval_gsm8k_grpo_random_20_seed123_v2` — 无 GSM8K random 文件（只有 `eval_math500_grpo_random_20_v2.json`）
- `eval_gsm8k_sft_depth_first_20` — 无任何 depth_first 文件
- `eval_gsm8k_grpo_depth_first_20` — 同上

Registry 确认这三个条目 status=DONE, conclusion=success，但 metrics 为空。结果文件可能在 westb-23072。

---

### 任务 3: 30% cliff CKA-only 核实
**无 CKA-only 30% recovery 结果文件。** 找到的 30% 文件均为 post-prune（recovery 前）：

| 文件 | accuracy | n_total |
|------|----------|---------|
| `eval_postprune_rasp_30.json` | 0.0% | 200 |
| `eval_postprune_standard_30.json` | 4.0% | 200 |

- 这些都是 N=200，不是 N=100
- 整个服务器上 N=100 的文件只有 3 个（`eval_postprune_rasp_25`、`eval_postprune_standard_25`、`eval_sft_grasp_20_greedy`），均与 30% CKA-only 无关

---

### 任务 4: Extended training 300 步 GSM8K eval
**是真实的 300 步 GSM8K eval，不是复用 100 步的值。**

| 文件 | accuracy | n_correct | n_total | model_path |
|------|----------|-----------|---------|------------|
| `eval_gsm8k_grpo_standard_20_extended_300.json` | 59.29% | 782 | 1319 | `grpo_standard_20_extended_300/` |
| `eval_gsm8k_grpo_cka_only_20_extended_300.json` | 64.37% | 849 | 1319 | `grpo_cka_only_20_extended_300` |

日志确认 2026-05-19 从 `grpo_standard_20_extended_300/` 加载模型、实际运行 GSM8K 1319 道题。

---
