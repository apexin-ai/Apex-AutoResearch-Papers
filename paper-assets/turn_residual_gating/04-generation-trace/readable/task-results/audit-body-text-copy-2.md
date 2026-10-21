# audit body text

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_body_text_20260525T203748_result.json`
- **Structured JSON:** [`e2fb02d7bb3ce46a78a5.json`](../../sessions/e2/e2fb02d7bb3ce46a78a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_body_text.md`。

**核心发现：~160 个定量声明中，~135 个与 Registry 一致，6 个问题（2 major + 4 minor），19 个需独立验证。**

### 2 个 Major 问题

1. **Table 1 IID 列数据存疑** — TG/LO 的 IID GAR-O 显示 0.50，但 Registry `phase2_4way_eval` 记录为 0.4866/0.4860（应舍入为 0.49）。IID PPL 显示 2.78 但 Registry 记录为 2.62–2.63（held-out 值为 2.78）。疑似 IID 列误用了 held-out 数据，或 IID eval 已重跑但 Registry 未更新。

2. **"≤1 pp" 应为 "≤2 pp"** — experiments.tex 称 "held-out GAR-ours differs by ≤1 pp"，实际各变体 IID→held-out 最大差异 1.7pp（TG），Table 精度下 UG 差 2pp。

### 4 个 Minor 问题

3. **~1.3× SS gap 偏高** — 多种子均值 gap = 1.245 ≈ 1.2×，非 ~1.3×（s42 单种子 1.29×）
4. **SS TF GAR 0.498±0.004** — 实际 0.499±0.003
5. **Fig 1 caption "85–90%" 未区分 base vs fine-tuned** — fine-tuned 仅 77–81%
6. **Llama SS "2 vs 3 epochs"** — Registry spec 写 epochs=3，需确认实际

### 跨章节一致性

所有跨章节出现的数字（~1.3×、7.8×、0.064、0.727、0.717 等）**内部完全一致**，无矛盾。

---
