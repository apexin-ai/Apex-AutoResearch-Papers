# analysis sf1 overclaim search

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf1-overclaim-search_20260520T133104_result.json`
- **Structured JSON:** [`80c3d68bdc4f70ab95bd.json`](../../sessions/80/80c3d68bdc4f70ab95bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 执行总结

### 已修改（可写文件，6 处）

| 文件 | 行 | 原文 | 改后 |
|------|----|------|------|
| limitations_content.tex | 8 | `bottleneck is fundamental` | `bottleneck is structural` |
| appendix.tex | 645 | `fundamental rather than prompt-specific` | `structural rather than prompt-specific` |
| analysis.tex | 85 | `same-model Pareto frontier:` | `same-model trade-off ceiling at the 7B--32B scale tested:` |
| diagnosis.tex | 138 | `same-model Pareto frontier:` | `same-model trade-off ceiling at the 7B--32B scale tested:` |
| diagnosis.tex | 138 | `shift the Pareto frontier remains open` | `shift the observed trade-off boundary remains open` |
| discussion.tex | 4 | `shift the Pareto frontier is open` | `shift the observed trade-off boundary is open` |

### 待修改（只读文件，需手动处理，8 处）

| 文件 | 行 | 原文 | 建议改为 |
|------|----|------|----------|
| **abstract.tex** | 6 | `fundamental independence-accuracy trade-off` | `persistent independence-accuracy trade-off` |
| **introduction.tex** | 28 | `fundamental independence-accuracy trade-off` | `persistent independence-accuracy trade-off` |
| **introduction.tex** | 33 | `same-model Pareto frontier` | `same-model trade-off ceiling` |
| **introduction.tex** | 29 | `demonstrates that this gap is recoverable` | `shows that this gap is recoverable` |
| **introduction.tex** | 33 | `demonstrates the frontier is escapable` | `shows the ceiling is escapable` |
| **solutions.tex** | 9 | `demonstrates that the MAX-SAT...is sound` | `shows that the MAX-SAT...is sound` |
| **conclusion.tex** | 3 | `demonstrates the gap is recoverable` | `shows the gap is recoverable` |

### 无需修改

- 所有 "significantly" 均有 p-value 支撑 ✅
- "prove" 是引用 Ladha (1992) 的已证数学结论 ✅
- introduction.tex:6 "demonstrate" 是引用 Loo et al. ✅
- appendix.tex:524 "demonstrates" 有 p=0.014 ✅
- Scope qualifiers 在 abstract/intro/limitations 已有，analysis 和 diagnosis 已补加 ✅

---
