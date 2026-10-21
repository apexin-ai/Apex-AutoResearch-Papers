# paper 015b nve fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_015b-nve-fix_20260517T131105_result.json`
- **Structured JSON:** [`0d2e86b28ce27d38e769.json`](../../sessions/0d/0d2e86b28ce27d38e769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。汇总：

### 改动清单

| 文件 | 行 | 改前 | 改后 |
|---|---|---|---|
| `results.tex` | 34 | `0.47$\times$` | `1.45$\times$` |
| `results.tex` | 99 | `never exceeds $0.47\times$` | `peaks near the diagnostic threshold ($1.45\times$ at 55K) but retreats to $0.55\times$ by 105K, confirming frozen embedding prevents the sustained escalation characteristic of CIVO` |
| `appendix.tex` | 119 | `NVE never exceeds the CIVO threshold: it remains in the $0.39$--$0.47\times$ range...` | 改为描述完整轨迹 (peak 1.45× @55K → 0.65× @65K → 0.55× @105K)，强调 transient vs sustained |
| `appendix.tex` | 121 | `frozen embedding never exceeds $0.47\times$ in the same window---an $8.7\times$ NVE gap` | 改为描述 transient peak 1.45× 自行回落 vs 008d 单调上升 (1.78→4.12) 的对比 |
| `appendix.tex` | 138 | `NVE 0.47$\times$` | `peak NVE 1.45$\times$ (transient)` |

### 验证
- `grep "0.47" docs/paper/**/*.tex` → **无匹配**
- Table 1 中 015b NVE 现为 `1.45×`，与 JSON 数据一致
- 叙事改为 transient vs sustained 框架，与 C2 framing 一致

---
