# writing update paper framing

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_update_paper_framing_20260514T233747_result.json`
- **Structured JSON:** [`2d6060a804079d880df7.json`](../../sessions/2d/2d6060a804079d880df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 已更新。核心变更：

1. **Path B 定稿** — 默认叙事为 "adaptive matches grid-best within seed variance, eliminates tuning cost"，Path A 保留为升级选项
2. **Drayson 三层差异化** — (a) principled b* vs empirical b, (b) loss reweighting vs SIR resampling, (c) unknown proportion vs known proportion。定位为 complementary approaches，非"我们更好"
3. **n_min robustness** — D012 修复作为 ESS 约束敏感度低的 practical robustness 证据，纳入 Method ablation 规划
4. **双叙事弹性** — Claims 中无硬编码数字，用 "within seed variance" / "eliminates grid search cost" / "consistent improvement" 表述，≥90% 和 85-90% 场景均可承载
5. **Core Claims 重组** — Claim 1 聚焦 α_eff(b) 理论框架，Claim 2 聚焦免调参实用结果，Claim 3 为 setting contribution

---
