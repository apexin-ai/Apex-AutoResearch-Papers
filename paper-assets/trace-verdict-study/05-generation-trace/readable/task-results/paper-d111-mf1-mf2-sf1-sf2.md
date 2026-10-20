# paper d111 mf1 mf2 sf1 sf2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d111_mf1_mf2_sf1_sf2_20260521T124840_result.json`
- **Structured JSON:** [`9b3388168bc2b0785ffe.json`](../../sessions/9b/9b3388168bc2b0785ffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，0 错误，0 未定义控制序列。21 页 PDF 生成成功。

## 修改汇总

### MF-1: C3 降级为 preliminary analysis (experiments.tex)
| 位置 | Before | After |
|------|--------|-------|
| §4.3 密度分解开头 | "We **consistently** observe that complete traces" | "We observe that complete traces" |
| §4.3 结论句 | "This asymmetry **implies** that content selection matters more than loss engineering." | "This asymmetry **suggests** that content selection **may** matter more than loss engineering." |

表格 caption 和尾部 caveat 已有 "Approximate"、"Qwen-2.5-Coder-7B only; cross-model validation left for future work"、"approximate decomposition (Qwen family, 2 scales, 3 seeds each)"，无需额外修改。Introduction 贡献 3 已标 "Preliminary analysis"。

### MF-2: C4 降格 (experiments.tex + discussion.tex)
| 位置 | Before | After |
|------|--------|-------|
| experiments.tex §4.2 消融小节 | "reveals a **consistent** two-tier pattern" | "reveals a two-tier pattern" |
| experiments.tex 消融讨论 | "The Tier~1/2 boundary is **unambiguous**:" | "The Tier~1/2 boundary is **clear in available data**:" |
| experiments.tex loop_only 后 | (无) | 新增: "These cross-model individual results support the two-tier pattern, though full component ablation has been conducted only on Qwen-7B." |
| discussion.tex 层级段 | "reveals a **consistent** two-tier pattern" | "reveals a two-tier pattern" |
| discussion.tex 层级段 | "suggests---but does not establish---a potential fallback design: extract exception events first, resort to Tier~2 only when no exception is raised." | "is corroborated by ae\_only and loop\_only data across all four models, though full component ablation has been conducted only on Qwen-7B." |

### SF-1: Reframe "why richer traces hurt" (introduction.tex + discussion.tex)
| 位置 | Before | After |
|------|--------|-------|
| introduction.tex 动机段末 | "The core question driving our study is counter-intuitive: *why do richer execution traces hurt model performance?*" | "This raises a fundamental question that drives our study: *why does providing more diagnostic information actually impair model learning?*" |
| discussion.tex 开头 | "The central finding is that for trace-based verdict prediction, learning efficiency strongly correlates with information density rather than information quantity." | "The central finding explains why richer traces hurt: for verdict prediction, learning efficiency strongly correlates with information density, not information quantity." |

### SF-2: 应用场景降级为 future directions (discussion.tex → conclusion.tex)
| 位置 | Before | After |
|------|--------|-------|
| discussion.tex | 含 "potential fallback design: extract exception events first, resort to Tier~2..." 的 speculative 应用描述 | 移除，替换为 cross-model caveat |
| conclusion.tex | "...model-dependent; generalization beyond LLM-generated Python code remains open." | "...model-dependent. Future work could explore a tiered extraction design that prioritizes exception events over lower-density components, and test whether the density principle extends to other trace-based tasks and to languages beyond Python." |

---
