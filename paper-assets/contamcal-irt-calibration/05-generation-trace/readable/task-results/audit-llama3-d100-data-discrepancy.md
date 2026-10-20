# audit llama3 d100 data discrepancy

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_llama3-d100-data-discrepancy_20260522T133335_result.json`
- **Structured JSON:** [`89826fa0edaa965f08ba.json`](../../sessions/89/89826fa0edaa965f08ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed — LLaMA-3.1-8B has no d005 or d050 experiments. The task context even explicitly warns: "LLaMA-3 只有 s0 seed × 3 dosage (d000/d025/d100)，不要假设有 s42/s123 或 d005/d050". 

Now I have the complete provenance chain. Here's the report:

---

## 追溯报告：LLaMA-3.1-8B d100 MMLU 数据不一致

### 1. 52.81% 的来源（正确值）

| 属性 | 值 |
|------|-----|
| **数值** | 52.81% (7416/14042) |
| **Eval** | westd-29999, seed=0, MMLU 5-shot aligned MC format |
| **Checkpoint** | `/root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d100_s0` |
| **Registry** | `sft_llama3_d100_s0` (DONE, 2026-05-21T13:50) |
| **Decision** | D207 (2026-05-21 13:49 UTC) |
| **确认来源** | `worker_ops_urgent-d100-results-collect` 原始输出、`data_audit_table1.md`（64 项审计通过）、`llama3_taxonomy_validation.json`、`memory.md`、`cross_benchmark_consistency.md`、`results.tex` line 34 |

**完整 3-point 轨迹**: d000=53.50%, d025=52.75%, d100=52.81% → Δ=-0.69pp → **Immune**

### 2. 54.59% 的来源（错误值）

| 属性 | 值 |
|------|-----|
| **数值** | 54.59% |
| **出处** | `falcon3_algorithm1_classification.md`（art_20260522_1bdc0e）|
| **创建时间** | 2026-05-22T13:15:32（今天） |
| **创建者** | `worker_analysis_falcon3-algorithm1-classification_20260522T131404` |

**根因**: Worker 在跑 `profile_classifier.py` 做 7 家族跨家族对比时，需要每家族 5 dosage 数据点。LLaMA-3.1 实际只有 3 个 dosage (d000/d025/d100)，**worker LLM 幻觉填充了 5 个数据点**：

```python
# Worker 使用的数据（全部错误，除 d000）
'LLaMA-3.1 8B': {'d000': 53.50, 'd005': 53.98, 'd025': 54.61, 'd050': 54.23, 'd100': 54.59}

# 实际数据
d000: 53.50%  ✅ 匹配
d005: 不存在   ❌ 幻觉值 53.98%
d025: 52.75%  ❌ Worker 写 54.61%（差 +1.86pp，方向反转）
d050: 不存在   ❌ 幻觉值 54.23%
d100: 52.81%  ❌ Worker 写 54.59%（差 +1.78pp，方向反转）
```

Grep 确认 53.98/54.61/54.23 这三个值在项目中无任何其他来源——纯幻觉。

### 3. 差异原因

**Worker LLM 幻觉**。不是 eval 格式差异、不是不同 seed、不是不同 checkpoint。Worker agent 在构建跨家族对比表时，将 LLaMA-3.1 的下降轨迹（53.50→52.75→52.81）错误地替换为上升轨迹（53.50→53.98→54.61→54.23→54.59），凭空捏造了 2 个不存在的 dosage 数据点，并修改了 2 个已有数据点的数值。

### 4. 格式一致性

所有 7 家族应使用同一种 eval 格式（aligned MC, 5-shot）。其他 6 家族在 `falcon3_algorithm1_classification.md` 中的数据均正确：

| Family | 文件中 d100 | 已知正确值 | 匹配 |
|--------|-----------|----------|------|
| Phi-4 | 76.27 | 76.27 | ✅ |
| Qwen-14B | 60.07 | 60.07 | ✅ |
| Qwen-7B | 64.33 | 64.33 | ✅ |
| Gemma-2 | 65.62 | 65.62 | ✅ |
| OLMo-2 | 57.00 | 57.00 | ✅ |
| Falcon3 | 62.96 | 62.96 | ✅ |
| **LLaMA-3.1** | **54.59** | **52.81** | **❌** |

### 5. 正确值与分类

| | 论文 (results.tex) | falcon3 分析文件 | 正确值 |
|---|---|---|---|
| d000 | 53.50% | 53.50% | **53.50%** |
| d100 | 52.81% | 54.59% | **52.81%** |
| Δ | -0.69pp | +1.09pp | **-0.69pp** |
| 分类 | Immune | Benefit-sat | **Immune** |

**论文 `results.tex` 中的值是正确的。** `falcon3_algorithm1_classification.md` 中 LLaMA-3.1 行需要修正。

### 修复建议

`falcon3_algorithm1_classification.md` 第 30 行应从：
```
| LLaMA-3.1 8B | 53.50 | 54.59 | +1.09 pp | Benefit-sat | 0.570 |
```
改为：
```
| LLaMA-3.1 8B | 53.50 | 52.81 | −0.69 pp | Immune | — |
```
（注：LLaMA-3.1 只有 3 个 dosage，confidence 值需用 3-point 版 Algorithm 1 重算或标 N/A）

---
