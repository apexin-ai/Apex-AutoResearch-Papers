# analysis edcr and 3seed prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_and_3seed_prep_20260515T115612_result.json`
- **Structured JSON:** [`35f8b1f300dce8cc33ca.json`](../../sessions/35/35f8b1f300dce8cc33ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成。结果：

## 任务 1：3-seed 汇总

2/3 seeds 已出 (s43 待出)：

| Metric | r1 (seed=42) | s44 (seed=44) | Mean±Std | SFT | Delta |
|--------|-------------|---------------|----------|-----|-------|
| Rel F1 | 0.4449 | 0.4655 | 0.4552±0.0146 | 0.4057 | **+0.0495** |
| Evi F1 | 0.8187 | 0.8087 | 0.8137±0.0071 | 0.7979 | +0.0158 |
| EDCR | 0.6565 | 0.6350 | 0.6458±0.0152 | 0.7118 | **-0.0660** |
| N Truncated | 213 | 189 | 201±17 | — | — |

脚本已 dry-run 通过，s43 结果出来后直接重跑即可。

## 任务 2：EDCR 证据分布分析

**关键发现 — EDCR 偏高的主因是 false positive triples，不是 evidence 选错：**

| 来源 | Citations | Distractors | 占比 |
|------|-----------|-------------|------|
| **False positive triples** | 14,874 | 14,874 (全部) | **90.1%** |
| Matched triples | 10,257 | 1,628 (EDCR=0.159) | 9.9% |

Matched triples 中 evidence 不匹配的分类 (n=1,297)：

| Type | Cases | 占比 | 含义 |
|------|-------|------|------|
| **B** (superset) | 948 | **73.1%** | 引用了所有 gold 句子 + 平均多引 1.26 句 |
| C (partial) | 273 | 21.0% | 部分重叠 |
| A (wrong) | 76 | 5.9% | 完全错误 |

**结论**：EDCR 高不是因为模型引用证据能力差。当关系预测正确时，evidence 质量很高 (EDCR 仅 0.159)。90% 的 distractor citations 来自关系本身就是 false positive——这些 triple 没有 gold evidence 可对标，所有引用全算 distractor。**降低 EDCR 的最有效手段是提高 relation precision（减少 FP），而非改善 evidence selection。**

产出文件：
- `/root/autodl-tmp/eval_results/3seed_summary.json`
- `/root/autodl-tmp/eval_results/edcr_analysis.json`（含 10 个典型案例）

---
