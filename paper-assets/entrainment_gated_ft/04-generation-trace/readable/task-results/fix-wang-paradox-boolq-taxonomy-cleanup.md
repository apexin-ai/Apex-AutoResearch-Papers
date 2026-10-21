# fix wang paradox boolq taxonomy cleanup

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_wang-paradox-boolq-taxonomy-cleanup_20260519T170231_result.json`
- **Structured JSON:** [`d3cbae7b884129357aea.json`](../../sessions/d3/d3cbae7b884129357aea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 修复 1: wang_et_al_differentiation.md (服务器)
- **5 处 "paradox"** 全部替换：→ "divergence"/"decoupling"/"aggregate-individual decoupling" 等 D008 批准叙事
- **6 个旧 scipy p 值** 替换为 exact permutation p 值并标注方法：
  - LAMBADA: 0.0083 → 0.0167; table: 0.008 → 0.017
  - ARC-Easy/MMLU: 0.117 → 0.2333
  - HellaSwag: 0.742 → 0.6833
  - ARC-Challenge: 0.883 → 0.35
  - WinoGrande: 0.608 → 0.95
- 所有统计声明添加 "(exact permutation test, two-tailed, n=5)"
- 验证：0 paradox, 0 co-evolution 残留

### 修复 2: convergence_table.csv
- BoolQ taxonomy: "retrieval" → "comprehension"

### 修复 3: "paradox" 残留审计

**活跃文件 — 无需修改：**
| 文件 | 行号 | 内容 | 判定 |
|------|------|------|------|
| paper_framing.md:3 | "drop 'paradox' narrative" | meta-reference（描述决策），OK |
| paper_framing.md:39 | "Do NOT frame as 'co-evolution'" | 禁令声明，OK |
| paper_framing.md:51 | "Simpson's paradox / ecological fallacy" | 外部概念引用，OK（允许） |
| ROADMAP.md:32 | 任务项 | 已标记完成 |
| ROADMAP.md:54,56 | D008/D006 决策记录 | 历史决策日志，OK |
| memory.md:27 | 禁用词列表 | 禁令本身，OK |

**Dream reports (artifacts/dream_reports/)**: ~30+ 处 "paradox"/"co-evolution"，全部在 archived review reports 中。这些是历史评审记录，不应修改。

**结论**: 活跃文档中无违规 "paradox"/"co-evolution" 残留。

### 任务 4: Paper Agent 材料清单
写入 `artifacts/paper_agent_inputs.md`，包含 6 个部分：framing 摘要、数据文件位置（5 个 paper_data 文件 + 服务器端数据）、待产出（exp-004-r2、exp-007）、Related Work 需求（8 个 topic areas）、写作约束（EMNLP 8p + D008/D009/W3 限制）、投稿信息（ARR June ~June 15）。

---
