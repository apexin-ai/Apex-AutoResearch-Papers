# bugfix bootstrap loo gold empty

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_bootstrap_loo_gold_empty_20260514T194330_result.json`
- **Structured JSON:** [`0d591d653a1b5dc20b68.json`](../../sessions/0d/0d591d653a1b5dc20b68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

## 修复内容

**Bug**: `run_bootstrap_loo.py` 和 `run_loo_v2.py` 未过滤 gold_empty 实例，导致 CoNLL 的 697 个 gold 标签为空的实例（20%）稀释了相关性。

**修复**: 在两个脚本中添加 `filter_gold_nonempty()` 函数，加载数据后过滤 `gold.entities` 为空的实例。

**过滤效果**: CoNLL 3453→2756, SciERC 551→529

## 修复后结果

### Bootstrap CI (B=10000, N=8 vs N=16)

| Dataset | Signal | ρ_N8 | ρ_N16 | Δρ mean | 95% CI | 
|---------|--------|------|-------|---------|--------|
| Qwen_CoNLL | SJ | 0.439 | **0.450** | +0.011 | [-0.014, 0.035] |
| Qwen_CoNLL | EM | 0.452 | **0.461** | +0.009 | [-0.015, 0.032] |
| Qwen_SciERC | SJ | 0.362 | **0.428** | +0.065 | **[0.004, 0.128]*** |
| LLaMA_SciERC | SJ | 0.367 | 0.379 | +0.011 | [-0.042, 0.065] |

*唯一 95% CI 排除 0 的信号

### LOO-SJ Circularity Check

所有数据集 |Δρ(full - LOO)| < 0.01，无循环性问题。CoNLL SJ ρ 从修复前的 0.125 升至 0.436-0.450（修复前低 3-4 倍正是 bug 所致）。

---
