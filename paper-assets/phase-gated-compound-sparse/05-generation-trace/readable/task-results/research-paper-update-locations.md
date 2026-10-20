# research paper update locations

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_update_locations_20260514T214853_result.json`
- **Structured JSON:** [`1ddf355a84810c4536dc.json`](../../sessions/1d/1ddf355a84810c4536dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已写入 `artifacts/n500_paper_patch_plan.md`。

**产出摘要**：

**Part A — 精确位置清单**：
- **8 张表格**需数据替换（T1-T8），其中 T3 (tab:llama-cross-arch) 需 D059 结构重构
- **77 处定量声明**（Q1-Q77），精确到 file:line
- **10 处 D059 违规**（D1-D10）：abstract/results/discussion/appendix 中 imp-vs-rand 或 random d_z，需改为 Wilcoxon p + median_diff
- **1 处 C8 限定语需修改**：results.tex:79 `The qualitative pattern replicates` → `is directionally consistent`
- **C5b 插入点**：discussion.tex:8 段落末尾或 conclusion.tex:5 之前
- **4 张 figure** 需 n=500 数据重生成（F1-F4），数据源和生成参数已记录

**Part B — 预写文本**：
- **B1 Qwen caveat**：~2 句，说明 imp-vs-rand 对比在 Qwen 上衰减的原因（低 baseline）
- **B2 C5b future work**：~3 句，oracle recovery 18% < 30% gate，phase-aware mitigation 是开放方向
- **B3 Mid-phase null rate**：~2 句，Qwen mid-phase ~45% null rate 限制统计功效

---
