# analysis freeform deep analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_freeform_deep_analysis_20260515T102907_result.json`
- **Structured JSON:** [`2011fc58c435e7c2c616.json`](../../sessions/20/2011fc58c435e7c2c616.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**RE LP Selection Flip**:
- 全部 7 种 relation type 都呈现 flip，不是单一类型驱动。PART-OF (+6.52pp) 和 HYPONYM-OF (+4.45pp) 翻转最大
- Free-form 选择性地在 RE-difficult instances 上放大 LP variance（ratio 1.06），在 easy instances 上压缩（0.86），Mann-Whitney p < 0.0001
- Constrained 模式 LP selection 的 win/loss 不对称（36:59），free-form 修正为 45:45，直接解释 gap 翻转
- 31 个 flip instances 是 relation-dense（3.3 gold rels，2× baseline），constrained 下 LP variance 被压缩

**Non-Tied 重叠度**:
- Jaccard = 0.472，虽然 tied fraction 只差 2pp，但 non-tied 集合成员大洗牌
- 87 个 instances 在 free-form 下新获得 LP 区分度（range 从 0.032→0.098），76 个失去（0.111→0.031）
- 两种 decoding 模式仅共享 ~24% 的 LP range variance

报告已注册为 `art_20260515_833ab1`。

---
