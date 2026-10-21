# audit condition consistency check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_condition_consistency_check_20260518T153742_result.json`
- **Structured JSON:** [`f643d060301a9bcedc65.json`](../../sessions/f6/f643d060301a9bcedc65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是完整结果。

---

## Condition 定义（train_sft.py）

| Condition 名 | 数据文件 | 截断逻辑 |
|---|---|---|
| `full_trace_tail` | `full_trace_tail_*.jsonl` | **动态**：trace tail 填满 2048 总 token 剩余空间，每条样本 budget 不同 |
| `full_trace_tail_256` | `full_trace_tail_256_*.jsonl` | **硬截断**：trace tail ≤ 256 tokens，超出 2048 总限再次截断 |
| `full_trace_tail_384` | `full_trace_tail_384_*.jsonl` | **硬截断**：trace tail ≤ 384 tokens |
| `full_trace_tail_512` | `full_trace_tail_512_*.jsonl` | **硬截断**：trace tail ≤ 512 tokens |
| `full_trace_tail_1024` | `full_trace_tail_1024_*.jsonl` | **硬截断**：trace tail ≤ 1024 tokens |
| `full_trace_head` | `full_trace_head_*.jsonl` | **动态**：trace head 填满 2048 总 token 剩余空间 |

注意：`full_trace_tail_2048` **不存在**（无 condition、无数据文件）。

---

## Condition 一致性对比表

以下基于 **log 文件中实际打印的 `Condition:`** 确认，不依赖 registry 中可能过时的 command。

### tail-256

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| Qwen-7B | `full_trace_tail_256_seed42` | `full_trace_tail_256` | ✓ |
| DeepSeek | `deepseek_full_trace_tail256_seed42` | `full_trace_tail_256` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_tail256_seed42` | `full_trace_tail_256` | ✓ |
| CodeLlama | `codellama13b_full_trace_tail256_seed42` | `full_trace_tail_256` | ✓ |

**一致** ✓

### tail-384

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| Qwen-7B | `qwen7b_full_trace_tail384_seed42` | `full_trace_tail_384` | ✓ |
| DeepSeek | `deepseek_full_trace_tail384_seed42` | `full_trace_tail_384` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_tail384_seed42` | `full_trace_tail_384` | ✓ |
| CodeLlama | `codellama13b_full_trace_tail384_seed42` | `full_trace_tail_384` | ✓ |

**一致** ✓（但 CodeLlama registry status=ALLOCATED，实际 checkpoint 已存在 May 18，registry 未更新）

### tail-512

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| **Qwen-7B** | **`full_trace_tail_seed42`** | **`full_trace_tail`（动态）** | **✗ 不一致** |
| Qwen-7B (补跑) | `full_trace_tail_512_seed42` | `full_trace_tail_512` | ✓ 已有正确版本 |
| Qwen-7B (新) | `qwen7b_full_trace_tail512_seed42` | PREPARING（未训练） | — |
| DeepSeek | `deepseek_full_trace_tail512_seed42` | `full_trace_tail_512` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_tail512_seed42` | `full_trace_tail_512` | ✓ |
| CodeLlama | `codellama13b_full_trace_tail512_seed42` | `full_trace_tail_512` | ✓ |

**不一致**：Qwen-7B 原实验 `full_trace_tail_seed42` 用了动态 `full_trace_tail`。已有补跑 `full_trace_tail_512_seed42` 用了正确的 `full_trace_tail_512`。

### tail-1024

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| Qwen-7B | `full_trace_tail_1024_seed42` | `full_trace_tail_1024` | ✓ |
| DeepSeek | `deepseek_full_trace_tail1024_seed42` | `full_trace_tail_1024` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_tail1024_seed42` | `full_trace_tail_1024` | ✓ |
| CodeLlama | `codellama13b_full_trace_tail1024_seed42_v3` | `full_trace_tail_1024` | ✓ |

**一致** ✓

### tail-2048（= dynamic `full_trace_tail`）

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| Qwen-7B | `full_trace_tail_seed42` | `full_trace_tail` | ✓ |
| DeepSeek | `deepseek_full_trace_tail2048_seed42` | `full_trace_tail` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_tail2048_seed42` | `full_trace_tail` | ✓ |
| CodeLlama | `codellama13b_full_trace_tail2048_seed42_v3` | `full_trace_tail` | ✓ |

**一致** ✓（全部使用动态 `full_trace_tail`，trace tail 填满 2048 总 token 预算）

### head-2048（= dynamic `full_trace_head`）

| Model | Experiment | Actual Condition | 一致？ |
|---|---|---|---|
| Qwen-7B | `qwen7b_full_trace_head2048_seed42` | `full_trace_head` | ✓ |
| DeepSeek | `deepseek_full_trace_head2048_seed42` | `full_trace_head` | ✓ |
| Qwen-1.5B | `qwen15b_full_trace_head2048_seed42` | `full_trace_head` | ✓ |
| CodeLlama | `codellama13b_full_trace_head2048_seed42` | `full_trace_head` | ✓ |

**一致** ✓

---

## 问题清单

| # | 问题 | 严重度 | 状态 |
|---|---|---|---|
| 1 | **Qwen-7B tail-512**：`full_trace_tail_seed42` 用了动态 `full_trace_tail` 而非硬截断 `full_trace_tail_512` | **高** | 已有补跑 `full_trace_tail_512_seed42`（condition 正确），在 budget curve 中替换即可 |
| 2 | `codellama13b_full_trace_tail384_seed42` registry status=ALLOCATED，但 checkpoint 已存在 | 低 | 需更新 registry |
| 3 | `qwen7b_full_trace_tail512_seed42` status=PREPARING，无命令 | 信息 | 不需要——`full_trace_tail_512_seed42` 已覆盖此需求 |
| 4 | Registry 中多个实验的 command 字段仍记录着已删除的 `train.py` 脚本 | 低 | 实际已用 `train/train_sft.py` 重跑，最终结果正确 |
| 5 | `codellama13b_full_trace_tail2048_seed42`(v1) 用了不存在的 `full_trace_tail_2048` condition | 已修复 | v3 已用正确的 `full_trace_tail` 替代 |

---

**结论**：除已知的 Qwen-7B tail-512 问题外，所有 budget point × 4 模型的 condition **一致**。唯一需要行动的是在 budget curve 图表中将 Qwen-7B 512 点替换为 `full_trace_tail_512_seed42` 的结果。

---
