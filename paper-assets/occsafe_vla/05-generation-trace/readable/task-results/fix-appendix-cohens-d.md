# fix appendix cohens d

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_appendix-cohens-d_20260527T043352_result.json`
- **Structured JSON:** [`72ef55297243331ccab6.json`](../../sessions/72/72ef55297243331ccab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**v1 per-seed CARs (来源: registry, at_50000_50r)**

| 条件 | exp_id | s0 | s1 | s2 | mean |
|------|--------|-----|-----|-----|------|
| Vanilla | mvp_vanilla_s{0,1,2} | 0.788 | 0.766 | 0.786 | 0.780 |
| Detach BN | ablation_occ_detach_s{0,1,2} | 0.746 | 0.744 | 0.748 | 0.746 |

**正确的 Cohen's d = -3.90**（pooled SD = 0.0087）

原文报告 d ≈ -0.04 确实是计算错误，偏差约 100 倍（可能小数点错位）。Reviewer 怀疑合理。

**修改状态：段落已不存在，无需修改。** appendix.tex 中已无任何包含 "d ≈ -0.04" 的文本，L69 附近的统计段落已被 D067 修复中重写，当前版本只描述统计方法（paired t-test + Cohen's d），不再报告具体数值。

---
