# ssh consolidate eval metrics

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_consolidate-eval-metrics_20260519T083501_result.json`
- **Structured JSON:** [`c474cc64d80bd8a4883c.json`](../../sessions/c4/c474cc64d80bd8a4883c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Let me compile the comprehensive table.

## 汇总结果

### 数据源说明
- **cqa1**: `/root/autodl-tmp/exp001/eval_results/` (aligned eval, MCQ format)
- **westd**: `/root/autodl-tmp/exp001/eval_results_14b/`, `eval_results_cross_family/`, `eval_vllm/`
- Benchmark 顺序已通过 `head` 确认文件头验证
- cqa1 aligned eval 包含 MMLU(14042)/GSM8K(1319)/ARC(1172)/HumanEval(164)
- westd 14B/Phi-4 eval 包含 MMLU/ARC

---

### Qwen2.5 Dose-Response 主表 (aligned eval)

**0.5B (seed=42)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .398 | .369 | .469 | YES |
| d005 | .326 | .362 | .329 | YES |
| d025 | .280 | .366 | .325 | YES |
| d100 | .233 | .365 | .294 | YES |

**0.5B (seed=123)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .422 | .341 | .497 | YES |
| d005 | .300 | .368 | .298 | YES |
| d025 | .347 | .353 | .406 | YES |
| d100 | .306 | .380 | .367 | YES |

**1.5B (seed=42)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .585 | .654 | .772 | YES |
| d005 | .585 | .648 | .769 | YES |
| d025 | .590 | .654 | .769 | YES |
| d100 | .593 | .650 | .769 | YES |

**1.5B (seed=123)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .585 | .654 | .758 | YES |
| d005 | .587 | .648 | .757 | YES |
| d025 | .588 | .655 | .758 | YES |
| d100 | .596 | .644 | .782 | YES |

**3B (seed=42, alpha=32)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .631 | .141 | .824 | YES |
| d005 | .631 | .415 | .825 | YES |
| d025 | .624 | .682 | .823 | YES |
| d100 | .636 | .704 | .821 | YES |

**3B (seed=123)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .633 | .181 | .833 | YES |
| d005 | .632 | .631 | .824 | YES |
| d025 | .637 | .525 | .834 | YES |
| d100_a32 | .633 | .707 | .825 | YES |

**7B (seed=42, cqa1 aligned)**

| Dosage | MMLU | ARC | item_data |
|--------|------|-----|-----------|
| d000 | - | .896 | YES (ARC only) |
| d005 | .692 | .897 | YES |
| d025 | .700 | .899 | YES |
| d050 | .705 | .899 | YES |
| d100 | .710 | .893 | YES |

**7B (seed=123, cqa1 aligned)**

| Dosage | MMLU | ARC | item_data |
|--------|------|-----|-----------|
| d000 | .698 | .899 | YES |
| d005 | .693 | .899 | YES |
| d025 | .703 | .899 | YES |
| d050 | .703 | .899 | YES |
| d100 | .707 | .897 | YES |

**7B (westd eval_vllm, lm-eval-harness format)**

| Dosage | Seed | MMLU | ARC (acc) | item_data |
|--------|------|------|-----------|-----------|
| d000 | s42 | .719 | .473 | YES |
| d000 | s123 | .720 | .457 | YES |
| d005 | s42 | .719 | .460 | YES |
| d005 | s123 | .721 | .464 | YES |
| d025 | s42 | .725 | .456 | YES |

> 注意：eval_vllm ARC 分数 (~0.46) 远低于 aligned eval (~0.90)，因为使用了不同评估格式 (lm-eval-harness acc vs 自定义 MCQ acc)

**14B (seed=42, westd)**

| Dosage | MMLU | ARC | item_data |
|--------|------|-----|-----------|
| d000 | .746 | .935 | YES |
| d005 | .754 | .931 | YES |
| d025 | .758 | .928 | YES |
| d050 | .769 | .928 | YES |
| d100 | .765 | .931 | YES |

---

### Cross-Family 模型

**Phi-4 (seed=42, westd)**

| Dosage | MMLU | ARC | item_data |
|--------|------|-----|-----------|
| d000 | .775 | .939 | YES |
| d005 | .781 | .939 | YES |
| d025 | .784 | .940 | YES |
| d050 | .787 | .937 | YES |

**OLMo-2-7B (seed=42, cqa1)**

| Dosage | MMLU | ARC | item_data |
|--------|------|-----|-----------|
| d000 | .587 | .681 | YES |
| d005 | .582 | .682 | YES |
| d025 | .591 | .678 | YES |

**Llama-3.2-3B (seed=42, cqa1, benchmark 顺序: gsm8k/arc/mmlu)**

| Dosage | MMLU | GSM8K | ARC | item_data |
|--------|------|-------|-----|-----------|
| d000 | .455 | .192 | .601 | YES |
| d005 | * | * | * | YES |
| d025 | * | * | * | YES |
| d100 | * | * | * | YES |

> *Llama d005-d100 benchmark 顺序待确认（可能与 d000 不同，grep 返回 3 个 accuracy 值但未验证 key 名对应）

---

### 缺失清单

| Family | Scale | 缺失内容 |
|--------|-------|----------|
| Qwen2.5 | 0.5B | d050 两个 seed 都缺 |
| Qwen2.5 | 1.5B | d050 两个 seed 都缺 |
| Qwen2.5 | 3B | d050 两个 seed 都缺 |
| Qwen2.5 | 7B s42 | d000 缺 MMLU; 所有 dosage 缺 GSM8K |
| Qwen2.5 | 7B s123 | 所有 dosage 缺 GSM8K |
| Qwen2.5 | 14B | 所有缺 GSM8K; 无 s123 seed |
| Phi-4 | 14B | d100 缺; 无 s123 |
| OLMo-2 | 7B | d050/d100 缺; 无 s123; 缺 GSM8K |
| Llama-3.2 | 3B | d050 缺; 无 s123 |
| Gemma-2 | 9b | **全部缺** (checkpoint 已有) |

### Per-Item 数据总结

**所有已完成的 eval 都有 per-item 数据** (`item_responses.json` + `correctness_matrix.json` + `eval_results.json` 内 `per_item` 数组)。IRT 分析所需的 binary correct/incorrect 矩阵可直接从 `correctness_matrix.json` 或 `per_item` 字段构建。

**可用 respondent 数量 (IRT 视角)**:
- MMLU: 0.5B(8) + 1.5B(8) + 3B(8) + 7B(~18) + 14B(5) + Phi-4(4) + OLMo(3) + Llama(4) = **~58 respondents**
- ARC: 同上 ~58 respondents
- GSM8K: 0.5B(8) + 1.5B(8) + 3B(8) = **24 respondents** (7B/14B 缺 GSM8K aligned eval)

---
