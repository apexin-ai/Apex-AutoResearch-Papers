# check westb status and utilize

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_status_and_utilize_20260519T174512_result.json`
- **Structured JSON:** [`33834a14dae6ac929e90.json`](../../sessions/33/33834a14dae6ac929e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry updates complete. Here's the summary:

## westb-23072 实验状态

### 已完成（4 个）

| 实验 | 指标 | 状态 |
|------|------|------|
| **eval_gsm8k_grpo_cka_only_20_seed123** | GSM8K acc=**64.22%** (847/1319), eos_rate=99.1% | DONE ✅ (刚注册) |
| **eval_humaneval_sft_cka_only_20_1p5b_2048** | pass@1=**0.61%** (1/164) | DONE ✅ (已在registry) |
| **eval_humaneval_grpo_cka_only_20_1p5b_2048** | pass@1=**0%** (0/164) | DONE ✅ (已在registry) |
| **eval_humaneval_sft_standard_20_1p5b_2048** | pass@1=**0.61%** (1/164) | DONE ✅ (已在registry) |

额外完成：
| **eval_humaneval_grpo_standard_20_1p5b_2048** | pass@1=**0.61%** (1/164) | DONE ✅ (已在registry) |

### 当前运行中

- **GPU 0** (PID 909411): `eval_humaneval_sft_rasp_20_1p5b_2048` — 评估 SFT RASP 1.5B HumanEval，log 显示已过 45%+。Registry 状态为 DONE/failed（上一次失败后被重新启动），无法回退到 RUNNING。
- **GPU 1**: 空闲

### GSM8K seed123 可复现性

seed123: 64.22% vs seed42: 64.37% — 差异仅 0.15pp，CKA-only GRPO 优势在不同 seed 下高度稳定。

### 1.5B 模型可用性

westb-23072 上已有完整 1.5B 模型集：
- `grpo_rasp_20_1p5b` ✅ — `eval_humaneval_grpo_rasp_20_1p5b_2048` 所需模型已就绪（registry 状态 PREPARING）
- `grpo_cka_only_20_1p5b`, `grpo_standard_20_1p5b`
- `sft_rasp_20_1p5b`, `sft_cka_only_20_1p5b`, `sft_standard_20_1p5b`

GPU 1 空闲，可立即启动 `eval_humaneval_grpo_rasp_20_1p5b_2048`。

---
