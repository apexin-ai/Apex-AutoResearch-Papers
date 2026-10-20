# analyze exp 011

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_011_20260520T033057_result.json`
- **Structured JSON:** [`035324c9290085dcb530.json`](../../sessions/03/035324c9290085dcb530.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**关键结论：**
- Gen 10 SLV = 2479.70，相比 Gen 9 继续上升 +16.56（+0.67%），总增幅 +4.78%
- SLV 从 Gen 2 起严格单调递增 8 代，controller 始终锁死 r=0.2 → **确认 Type II（controller silence）**
- r=0.2 增幅 (+4.78%) < r=0.3 增幅 (+6.1%)，符合「更少 real data → 更慢 spectral expansion」的预期，进一步支持 r_crit ∈ (0.25, 0.3] 的判断

---
