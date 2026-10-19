# paper experiments refinement v1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments-refinement-v1_20260517T040633_result.json`
- **Structured JSON:** [`689781e69017b69a5820.json`](../../sessions/68/689781e69017b69a5820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改完成：

1. **Section 4.2 (lines 117-123)**: 在 `\paragraph{Why does richer conditioning fail?}` 之前加入了 scalar < perdof ordering 的解释段落，包含 cross-seed 数据和 noise origin 论点。

2. **Section 4.1 (lines 86-88)**: 替换了原来带 em-dash 的 "Three baselines---" 句，加入 VLA-mean 含义的两句解释。另在 statistical protocol 段落 (line 51) 补充了 multi-seed VLA-mean 数据 (12.5%, seeds 42/43/44/45 = 12/15/10/13%)。

3. **Section 4.4 (lines 198-236)**: 完整替换 placeholder 为实际 per-task 分析表格和两段分析文字，核心论点是 improvement 集中在 medium-difficulty tasks。

---
