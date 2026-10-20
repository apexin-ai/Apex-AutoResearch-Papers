# analysis recency s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recency_s030_20260517T005557_result.json`
- **Structured JSON:** [`21ec9dd0453db3440e8e.json`](../../sessions/21/21ec9dd0453db3440e8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**recency_s030 分析完成。结论：SUCCESS**

核心结果：
- **Phase gradient**: d_z=-0.096 (negligible), p=0.114, **不显著**
- **对照 importance_s030**: d_z=+0.330, p<1e-79, 显著
- **对照 random_s030**: d_z=-0.049, p=0.0015, 微弱显著但 effect negligible

与 recency_s015 一致：recency eviction 在 s=0.15 和 s=0.30 两个 sparsity 水平都没有显著 phase gradient，而 importance-based eviction 在相同 sparsity 下有强显著 gradient。对照假设验证成功，确认 phase-dependent compound severity 是 attention-score-specific 的，不是 positional artifact。

Registry 已更新为 DONE/success，分析报告已注册为 artifact。

---
