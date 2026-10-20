# paper integrate exp004

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate_exp004_20260515T231453_result.json`
- **Structured JSON:** [`5b11c4a9d73b639a5b95.json`](../../sessions/5b/5b11c4a9d73b639a5b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成。汇总如下：

**修改的文件（7 个）：**

| 文件 | 修改内容 |
|------|---------|
| `experiments_c1.tex` | Table 1 新增 Qwen-7B 列（5-fold CV ±σ）；开头更新为 5 model configurations；新增 Cross-scale validation 段落（K\*=2, 0v1 AUC↓, JSD, top features）；条件数更新为 9 |
| `discussion.tex` | §4.1 新增 7B scale invariance 段落：depth saturation 是 autoregressive generation 的固有属性，非小模型 artifact |
| `introduction.tex` | "4 model-mode configurations at ≤1.5B scale" → "5 model configurations (1B–7B)" |
| `main.tex` (abstract) | "4 model-mode configurations (≤1.5B)" → "5 model configurations (1B–7B)"，条件数 8→9 |
| `main.tex` (limitations) | "(1) model scale (≤1.5B)" → "(≤7B, with only one 7B configuration tested; cross-scale scoring)"；"four configurations" → "five configurations" |
| `conclusion.tex` | 新增 7B cross-scale validation 结论句；"scaling to 7B+" → "scaling beyond 7B" |
| `tab_crossscorer.tex` | 新增 Qwen-7B-cont 行（scorer: Qwen-1.5B, K\*=2, AUC(0v1)=0.9644, AUC(1v2)=0.6178）|

**Provenance**：所有定量 claim 已通过 `edit_paper_section` 关联到 `exp_004_7b_crossscale`。0v1 AUC 下降（0.964 vs >0.99）如实报告，未 cherry-pick。

未找到独立的 rebuttal 文件（只有 worker log），FR-4 回应内容已隐含在 experiments 和 discussion 的 scale invariance 论述中。

---
