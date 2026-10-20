# research literature scan

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260512T230501_result.json`
- **Structured JSON:** [`bfb33c87173ad4a21a98.json`](../../sessions/bf/bfb33c87173ad4a21a98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献扫描完成。结果写入 `artifacts/literature_map.yaml`（13篇论文）。

**截至 2026-05-12，未发现新的 cross-method circuit consensus 工作。** 核心发现：

| 论文 | 做了什么 | 为什么不是我们的 novelty |
|------|---------|------------------------|
| CIRCUS (2603.00523v2) | intra-method threshold variation ensemble | 单一算法内变阈值，不跨算法族 |
| Mondorf et al. (2510.06811) | EAP-IG + EP 平行/串行 ensemble | 仅 gradient-family 内组合 |
| Certified Circuits (2602.22968) | 数据扰动稳定性认证 | 单方法 + data axis，非 method axis |
| Nikankin et al. (2510.25786) | 单方法 bootstrapping | 同上 |

**CSS 的 cross-algorithm-family consensus（gradient vs mask vs causal）在当前文献中无人做过，novelty 成立。**

CIRCUS 无 v2/follow-up（v2 只是同篇 minor update，2026-03-20）。

值得关注的新工作：
- Formal MI (ICLR 2026) — 可用于验证 consensus circuit 的 minimality
- PIE (2604.16889) — CLT-native 新方法，可纳入 CSS ensemble
- GIM — MIB benchmark 第一，作为强 baseline 纳入

---
