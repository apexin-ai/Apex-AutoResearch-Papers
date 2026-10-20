# analysis 1 7b repetition fair subset

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_1_7b_repetition_fair_subset_20260518T070802_result.json`
- **Structured JSON:** [`1cffbe39e49f951673ae.json`](../../sessions/1c/1cffbe39e49f951673ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Repetition rates**:
- No-evidence: 467/985 (47.4%) repetitive, 全部也被截断
- With-evidence: 215/985 (21.8%) repetitive

**Fair subset**: 排除两个模型中任一被截断或重复的文档后，剩 **439/985 docs (44.6%)**

**Evidence tax (Ign-F1)**:

| Subset | No-Evi | With-Evi | Tax |
|---|---|---|---|
| Full (985) | 0.3982 | 0.4786 | **-8.04pp** |
| Fair (439) | 0.5722 | 0.6334 | **-6.12pp** |

关键发现：
1. With-evidence 在所有子集上都优于 no-evidence（evidence helps at 1.7B）
2. 原始 -8.04pp gap 中约 24% (1.92pp) 来自截断率差异（no-evi 50.9% vs with-evi 31.9%），不是模型能力差异
3. **Corrected evidence tax = -6.12pp**
4. No-evidence 模型的重复几乎都伴随截断（rep => trunc），说明 1.7B 一旦开始重复就停不下来直到 max_new_tokens

注意：任务中提到的 "with-evi 0.3299" 与实际数据不符。实际 with-evidence SFT 的 ign_f1 = 0.4786。报告已保存到 `artifacts/1_7b_repetition_fair_eval.md`。

---
