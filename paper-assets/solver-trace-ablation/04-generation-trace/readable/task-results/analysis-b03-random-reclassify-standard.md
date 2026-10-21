# analysis b03 random reclassify standard

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_b03-random-reclassify-standard_20260515T182054_result.json`
- **Structured JSON:** [`b48fec752790676e4b8c.json`](../../sessions/b4/b48fec752790676e4b8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 registry 已更新。汇总：

### 新旧对比表（β=0.3 Random 标准 taxonomy 重分类）

| 实验 | Proved | H7 旧→新 | H1 旧→新 | H8 | Genuine 旧→新 | 变化 |
|---|---|---|---|---|---|---|
| plan017-additive-random-s42 | 48% | 0→**4** | 48→**44** | 0 | 0→0 | H7a 新增 4 例 |
| exp1-random-b03-s43-r4 | 92% | 7→7 | 82→82 | 0 | 3→3 | 无变化 |
| exp1-random-b03-s44-r2 | 23% | 0→0 | 23→23 | 0 | 0→0 | 无变化 |

唯一实质变化：**s42 新增 4 个 H7a**（text-match tautology），旧 strict taxonomy 未检出。H1 相应从 48 降到 44（4 个被重分类为 H7a）。genuine 仍为 0。

JSON 结果存于 `/root/autodl-tmp/outputs/h7_classification/h7_random_b03_reclassify.json`，三个实验 registry metrics 均已更新为 `taxonomy_version: classify_h7_v2_2026-05-16`。

---
