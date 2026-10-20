# check all experiments status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-experiments-status_20260522T202624_result.json`
- **Structured JSON:** [`839c82d9eafe07bf4881.json`](../../sessions/83/839c82d9eafe07bf4881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已设置。汇总当前状态：

---

## 已完成实验评估结果

| 实验 | DR% | RV% | ET% | CF | R-F1 | E-F1 | Parse% | 状态 |
|------|-----|-----|-----|-----|------|------|--------|------|
| **70B LoRA SciERC unconstrained** | 1.5 | 0 | 0 | 0 | 44.73 | 64.86 | 100 | DONE |
| **70B LoRA SciERC beam4_s1 (full)** | 0 | 0 | 0 | 0 | 44.81 | 64.89 | 100 | DONE |
| **70B LoRA SciERC grammar_only** | 1.5 | 0 | 0 | 0 | 44.63 | 64.82 | 100 | DONE (negative) |
| **70B LoRA SciERC semantic_only** | **0.6** | 0 | 0 | 9 | **44.73** | 64.86 | 100 | DONE (new) |
| **70B LoRA SciERC full_s2** | **0** | 0 | 0 | 18 | **36.28** | 62.35 | 100 | DONE (negative) |
| **70B ZS SciERC unconstrained** | 6.4 | 0.6 | 0 | 0 | 11.23 | 35.22 | 100 | DONE (new) |

### 关键发现

- **semantic_only**: DR 从 1.5%→0.6%，R-F1 不变（44.73）。语义层单独贡献 DR 下降，无 F1 损失。
- **grammar_only**: DR 仍 1.5%，与 unconstrained 一致 → grammar 层对 DR 零贡献。conclusion 已修正为 negative。
- **full_s2**: DR=0% 但 R-F1 暴跌至 36.28（-8.5pp），E-F1 也降到 62.35。S2 模式过度约束导致 recall 大幅下降。

## GPU 使用状态

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| **westd-16980** | eval_70b_lora_docred_200_semantic_only (新启动) | eval_70b_lora_docred_200_grammar_only (新启动) |
| **westd-21461** | eval_70b_zs_docred_200_semantic_only (新启动) | eval_70b_lora_docred_200_beam4_s1 (160/200) |

## Registry 修复

- `eval_70b_lora_scierc_grammar_only` conclusion: success → **negative** (已修复)

## 新启动实验 (3个)

1. **eval_70b_lora_docred_200_semantic_only** — westd-16980 GPU 0, PID 983803
2. **eval_70b_lora_docred_200_grammar_only** — westd-16980 GPU 1, PID 984253
3. **eval_70b_zs_docred_200_semantic_only** — westd-21461 GPU 0, PID 78742

Cron 每 12 分钟轮询进度，完成后自动评估并更新 registry。

---
