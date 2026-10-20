# ssh westb checkpoint scan

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_checkpoint_scan_20260520T223907_result.json`
- **Structured JSON:** [`4269c18e6db040f13467.json`](../../sessions/42/4269c18e6db040f13467.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 扫描结果

### 磁盘
`/root/autodl-tmp`: 227G/250G used, **24G 可用**

### Eval 脚本
| 脚本 | 状态 |
|------|------|
| eval_gsm8k.py | ✓ |
| eval_mbpp.py | ✓ |
| eval_humaneval.py | ✓ |

### 数据集缓存
| 数据集 | 状态 |
|--------|------|
| GSM8K | ✓ 已缓存 |
| MBPP | ✗ 未缓存 |
| HumanEval | ✗ 未缓存 |

### 可用 Checkpoint（30 个目录）

**Pruned 模型（10）：**
`pruned_cka_only_20`, `pruned_cka_only_20_1p5b`, `pruned_cka_only_20_qwen_math`, `pruned_rasp_20`, `pruned_rasp_20_1p5b`, `pruned_rasp_rlvr_20`, `pruned_standard_20`, `pruned_standard_20_1p5b`, `pruned_standard_20_qwen_math`, `pruned_standard_25`

**SFT 模型（10）：**
`sft_cka_only_20`, `sft_cka_only_20_1p5b`, `sft_qwen_math_cka_only_20`(+final), `sft_rasp_20_1p5b`, `sft_rasp_rlvr_20`, `sft_standard_20_1p5b`, `sft_standard_20_qwen_math`(+final), `sft_standard_25`

**GRPO 模型（5）：**
`grpo_cka_only_20`, `grpo_cka_only_20_1p5b`, `grpo_cka_only_20_seed123`, `grpo_random_20`, `grpo_rasp_20_1p5b`

### 已有 Eval 结果 vs 缺口

**GSM8K（覆盖最全）：** 绝大部分模型已评估，缺口：
- `grpo_random_20` — 无 GSM8K 结果

**MBPP（仅 2 个）：**
- ✓ sft_cka_only_20_1p5b, sft_standard_20_1p5b
- ✗ 其余所有模型均未评估 MBPP

**HumanEval（仅 3 个）：**
- ✓ grpo_standard_20_1p5b, sft_rasp_20_1p5b, sft_standard_20_1p5b（均为 1.5B）
- ✗ 其余所有模型均未评估 HumanEval

### 立即可跑 vs 需额外准备

| 类别 | 条件 |
|------|------|
| **GSM8K eval — 立即可跑** | 脚本 ✓ + 数据集缓存 ✓，可离线跑 |
| **MBPP eval — 需下载数据集** | 脚本 ✓ 但无 `.arrow` 缓存，需联网下载 |
| **HumanEval eval — 需下载数据集** | 脚本 ✓ 但无 `.arrow` 缓存，需联网下载 |

---
