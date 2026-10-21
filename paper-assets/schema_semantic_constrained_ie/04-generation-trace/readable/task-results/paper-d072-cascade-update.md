# paper d072 cascade update

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d072_cascade_update_20260520T161337_result.json`
- **Structured JSON:** [`b55c6e43974fd002dacc.json`](../../sessions/b5/b55c6e43974fd002dacc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。汇总如下：

---

## 修改汇总

### 1. section5_scierc_draft.tex (8 处)
- **L104**: "eliminates or near-eliminates" → "eliminates"
- **L105**: DocRED 段落重写 — "0.76→0.01 (↓99%), 0.49→0.21 (↓57%)" → "0.56→0%, 0.49→0%" + R-F1 delta -0.10/+0.15
- **L106**: 删除 "lower Llama-DocRED reduction (57%)" 整句
- **L106(新)**: DR ≤ 0.21% → 0.09%
- **L108**: DR ≤ 0.21% → 0.09%
- **L109**: R-F1 44.23 → 43.60
- **L129-130**: Table 2 Qwen DocRED: 0.76/0.09/40.86/82.15/↓99% → 0.56/0.08/40.89/82.35, 0.01/0.27/40.56/81.43/↓99% → 0.00/0.22/40.79/81.87/↓100%
- **L138-139**: Table 2 Llama DocRED: 43.72/83.93 → 44.55/84.77, 0.21/0.21/43.78/83.94/↓57% → 0.00/0.26/44.70/84.71/↓100%
- **L143**: Caption DR ≤ 0.21% → 0.09%

### 2. abstract.tex (L6)
- "near-eliminates DR violations (DR ≤ 0.21%)" → "eliminates DR violations (DR ≤ 0.09%)"

### 3. section1_introduction_draft.tex (L22)
- "near-eliminates DR (≤ 0.21%)" → "eliminates DR violations (DR ≤ 0.09%)"

### 4. section3_violation_landscape.tex (L8)
- "near-eliminating DR violations" → "eliminating DR violations"

### 5. section4_composition_draft.tex (L31, L40)
- "DR 0.01--0.21%" → "DR ≤ 0.09%"
- "DR drops to ≤ 0.21%" → "≤ 0.09%"

### 6. section5_crossmodel_draft.tex (L59)
- "DR ≤ 0.21%" → "DR ≤ 0.09%"

### 7. section5_docred_draft.tex (L62, L71)
- "near-eliminates RV" → "eliminates RV"
- "0.01--0.21%" → "≤ 0.09%"

### 8. main.tex Limitations (L81)
- "DR ≤ 0.21%" → "DR ≤ 0.09%"

### 9. section7_conclusion_compressed.tex (L4)
- "DR ≤ 0.21%" → "DR ≤ 0.09%"

### 10. appendix_discussion.tex (9 处)
- **ft-ablation 表**: Qwen DocRED unc/Full S1、Llama DocRED unc/Full S1 四行全部更新至 d065 权威值
- **L269 caption**: max ΔR-F1 -0.30pp → -0.10pp
- **L275**: DR ≤ 0.21% → 0.09%
- **L276**: max R-F1 decrease -0.30pp → -0.10pp, 精简措辞
- **post-hoc 表 L328-329**: R-F1_cd 40.56→40.79 (Qwen), 43.78→44.70 (Llama)

### 11. appendix_beam_search.tex (L135)
- R-F1=44.23 → 43.60

---

## Grep 验证结果
- `0.21%` — **零命中** ✅
- `near-eliminat` — 仅废弃文件 `section5_docred_draft_9b84f1.tex` ✅
- 旧 DocRED 数字 (82.15/40.86/81.43/40.56/83.93/43.72/83.94/43.78) — **两处残余**:
  - `appendix_beam_search.tex:123` 的 43.72 是 SciERC beam 数据，非 DocRED ✅
  - `appendix_discussion.tex:255` 的 Qwen DocRED Semantic 中间行 (DR=0.21, E-F1=82.15) — **无 d065 权威数据，需后续补充**
- `0.76` — **零命中** ✅
- `44.23` — **零命中** ✅

---
