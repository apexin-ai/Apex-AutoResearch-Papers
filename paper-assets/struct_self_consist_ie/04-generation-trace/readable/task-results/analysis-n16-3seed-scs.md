# analysis n16 3seed scs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n16_3seed_scs_20260515T113242_result.json`
- **Structured JSON:** [`bad1f5b8edff89a82f37.json`](../../sessions/ba/bad1f5b8edff89a82f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**NER**: SJ 和 VC 在 N=16 下并列最强（ρ ≈ 0.41），SJ 更稳定（σ=0.010 vs 0.026）。相比 N=8，SJ 提升最大（+0.046, +12.7%），从第二跃升至与 VC 并列第一。

**RE**: VC 稳居第一（ρ=0.374），大幅领先 #2 LP（0.310）。VC 从 N=8→N=16 提升最大（+0.065, +21.1%）。

**排名稳定性**: Kendall's W = 0.956（NER 和 RE 均为），近乎完美一致。NER 仅 SJ/VC 在不同 seed 互换 #1-2，RE 仅 FK/LP 互换 #2-3，其余位置完全固定。

**N=8 → N=16**: 所有信号的 ρ 均提升，跨 seed σ 普遍降低。RE 排名从 N=8 的轻微不稳定变为 N=16 的高度一致。

报告已注册为 `art_20260515_c14e0b`，registry 已更新 `exp_001_n16_seed456 → DONE`。

---
