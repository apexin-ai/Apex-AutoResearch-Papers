# analysis eval supp k2mean spatial s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-supp-k2mean-spatial-s42_20260523T093827_result.json`
- **Structured JSON:** [`43c9cea5ab6ef0c0a25f.json`](../../sessions/43/43c9cea5ab6ef0c0a25f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)，产出已注册。

**结论**: K=2 mean SR = **81.5%**，比 VLA-only (78.5%) 高 3pp。Hypothesis 被否定——multi-sample averaging 本身就是主要改进来源，CRM correction 仅贡献约 0.5pp 的增量 (81.5% → 82.0%)。改进分解：

- 78.5% → 81.5% (+3.0pp): 来自 2-sample averaging
- 81.5% → 82.0% (+0.5pp): 来自 CRM correction

这意味着 paper narrative 需要调整：不能把 CRM 作为核心改进机制，averaging/sampling diversity 才是主要贡献。

---
