# fix plan017 review fixes

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan017_review_fixes_20260514T092605_result.json`
- **Structured JSON:** [`e6810c34731b18df1ed0.json`](../../sessions/e6/e6810c34731b18df1ed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，汇总如下：

---

### 1. arXiv ID 验证结果

| arXiv ID | 论文 | 状态 | 处理 |
|-----------|------|------|------|
| 2408.03910 | CodexGraph | 真实 | 保留 |
| 2503.09089 | LocAgent | 真实 | 保留 |
| 2410.14684 | RepoGraph | 真实 | 保留 |
| 2406.07003 | GraphCoder | 真实 | 保留 |
| **2509.25257** | **RANGER** | **真实** | 保留，内容匹配 |
| **2605.03117** | **ARISE** | **真实** | 保留，**年份 2025→2026 已修正** |
| 2405.02355 | CodeGRAG | 真实 | 保留 |
| 2504.10046 | CodeRAG | 真实 | 保留 |

所有 8 篇引用均为真实论文，无幻觉。ARISE 的年份标注错误（2025→2026）已全局修正。

### 2. 术语修正改动列表

| 位置 | 原文 | 修正后 |
|------|------|--------|
| L57 (§1.4 Core idea) | `CodeQL's inter-procedural taint tracking` | `CodeQL's bounded inter-procedural data-flow analysis (2-hop call-graph scope)` |
| L59 (§1.4 Graph construction) | `taint-tracking queries` / `full inter-procedural data-flow` | `data-flow queries` / `bounded inter-procedural data-flow` + 增加 "within a 2-hop call-graph scope" |
| L77 (§2.1 表格) | `Inter-procedural taint tracking via CodeQL` | `Bounded inter-procedural data-flow analysis (2-hop) via CodeQL` |
| L153 (Related Work) | `CodeQL's inter-procedural taint tracking` | `CodeQL's bounded inter-procedural data-flow analysis (2-hop call-graph scope)` |
| L157 (Discussion) | `extending StructFuse's inter-procedural analysis to the inference-time setting` | `extending StructFuse's bounded inter-procedural analysis beyond the current 2-hop scope or to the inference-time setting` |

"taint tracking" 仅在 L9 保留——该处描述 CodexGraph 不具备的能力（"no taint tracking"），不涉及 StructFuse。

### 3. 完整性确认

- `grep "full inter-procedural"` → 0 匹配
- `grep "taint tracking"` → 仅 L9（描述 CodexGraph，正确）
- `grep "unbounded"` → 0 匹配
- ARISE 全部 3 处引用均已更新为 2026
- 文档已同步到服务器 `/root/structfuse-context/artifacts/analysis/plan017_literature_comparison.md`

---
