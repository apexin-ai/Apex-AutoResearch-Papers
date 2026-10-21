# paper r20 text edits

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r20_text_edits_20260522T192247_result.json`
- **Structured JSON:** [`d342d4acd6a82987547e.json`](../../sessions/d3/d342d4acd6a82987547e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成，上下文通顺。汇总如下：

### 修改汇总

| Task | 文件 | 行号 | 内容 |
|------|------|------|------|
| **B1** | `discussion.tex:19` | 原 L18 末尾 | 在 base-vs-instruct 段落末追加替代解释句："An alternative explanation...yet we observe opposite patterns" |
| **B2** | `discussion.tex:25` | 原 L24 | "≥500 models accumulate (ensuring ≥80 per stratum...)" → "N≥80 per cohort suffices for significant detection; we recommend N≥500 for robust estimation..." |
| **B3** | `experiments.tex:16` | 原 L16 | K=10 解释从 "reflects ability–DIF interactions...residual non-uniform DIF that MH does not capture" → "may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation" |
| **B4** | `appendix.tex:49` | 原 L49 | Matching 段落：加入 caliper 0.2 SD、sample size ~50% 说明 |
| **B5** | `experiments.tex:118` | 原 L118 | GSM1K 分析拆为独立句，标注 exploratory，使用 outlier-removed 数值 (r=−0.38, p=0.036)，加 "suggestive rather than confirmatory" |
| **B6** | `discussion.tex:3-4` | 原 L3 | `\enlargethispage*{20\baselineskip}` → `\enlargethispage*{4\baselineskip}` + TODO 注释 |
| **B7** | — | — | **跳过**：论文中未找到 "34.35%"、"6-month window" 或相关内容，无修改目标 |

---
