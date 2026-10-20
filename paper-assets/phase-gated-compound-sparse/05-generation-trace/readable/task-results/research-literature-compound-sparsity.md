# research literature compound sparsity

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-compound-sparsity_20260513T235814_result.json`
- **Structured JSON:** [`2f426922008bfe71b814.json`](../../sessions/2f/2f426922008bfe71b814.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。新增 13 篇论文写入 `literature_map.yaml`，关键分析写入 `memory.md`。

**要点总结：**

| 发现 | 影响 |
|------|------|
| SLiM (ICML'25) 证明 compound error 非加性 | 支撑我们核心 claim，可引用为理论先驱 |
| GRASPrune (ACL'26) learned gate 联合 prune FFN+heads | **最直接 competitor**，但不分析 interaction direction、无 phase conditioning |
| Phase Transitions (npj AI'26) 多维 PTP 正交可叠加 | 直接支撑 phase-gating 理论动机 |
| Compression Ordering 证明交互依赖操作顺序 | 与我们"masking strategy 决定交互方向"同构 |
| "Doing More With Less" unstructured pruning 超越 unpruned | 符号反转的外部证据 |
| Decision Repr Transitions: Silent/Decisive Phase 二分 | 与 phase-gated 思想高度呼应 |
| **无论文直接对比 importance vs random 在 compound 下的交互方向差异** | **我们的 novelty gap 确认成立** |

---
