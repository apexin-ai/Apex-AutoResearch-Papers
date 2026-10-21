# writing introduction

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_introduction_20260515T155411_result.json`
- **Structured JSON:** [`42c3eca1d05b85042962.json`](../../sessions/42/42c3eca1d05b85042962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§1 Introduction 已写入 `section_introduction.tex`，约 890 words。

**结构**：
1. **Hook** (¶1): 递归反馈循环在 web 语料中自发形成，depth 决定数据质量——1st-gen 可用，deeply recursive 驱动 collapse
2. **Gap** (¶2): Binary detectors 丢弃 ordinal 信息，model collapse 研究假设 depth 已知，EditLens 不处理递归链——当前工具无法诊断 depth
3. **Insight + mechanism** (¶3-4): p90_ppl top-2 in 9/9 cells, var_surprisal 7/9; RF 70-85% accuracy (chance 25%); end-to-end DeBERTa 58.3% / RoBERTa 59.5% << RF 78.2%
4. **四项贡献**：
   - C1: Task formalization + EDD metric + 180K benchmark (3×3×4)
   - C2: Depth Degradation Atlas — feature universality, strategy-dependent trajectories, EDD boundary (d3v4 AUC 0.750-0.784, d4v5 < 0.70)
   - C3: Cross-model 66.4% / cross-strategy 59.1% + temp09 d1v2 structural shift（z-score 不恢复）
   - C4: DCOL 6× failure + dual backbone negative result

所有关键数字、cross-reference labels、citation placeholders 均已嵌入。

---
