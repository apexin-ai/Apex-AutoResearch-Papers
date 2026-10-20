# paper related work expansion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related-work-expansion_20260516T162553_result.json`
- **Structured JSON:** [`e796323fee7383c0b7b4.json`](../../sessions/e7/e796323fee7383c0b7b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/_project/paper/related_work_expanded.md`，已注册为 `art_20260516_704dea`。

**产出概览：**
- 26 篇已验证引用，覆盖 6 个方向
- 每篇标注了 authors / year / venue / core contribution / relation (support/contrast/extend)
- 最后包含 positioning statement 和 reference summary table

**各方向分布：**

| 方向 | 篇数 |
|------|------|
| World Model Learning | 6 |
| Temporal Abstraction | 4 |
| Compounding Errors | 5 |
| Gradient Interference | 5 |
| Plasticity Loss | 4 |
| Representation / Stop-Gradient | 3 |

核心定位：我们是第一个提供 trained temporal embedding 通过 obs decoder 梯度路径导致 CIVO 的 mechanistic account，方法论（2×2 ablation + gradient decomposition）可复用于任何 multi-head world model 架构。

---
