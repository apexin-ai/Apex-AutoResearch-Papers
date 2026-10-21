# writing results section

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_results-section_20260515T043424_result.json`
- **Structured JSON:** [`9269705083f28646a7fc.json`](../../sessions/92/9269705083f28646a7fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**报告**

| 项目 | 内容 |
|------|------|
| **Section** | §5 Results (4 subsections: Classification, Differential Depth Response, Baselines, Downstream Utility) |
| **Word count** | ~1,131 words (含 LaTeX markup), 约 2 pages in acl.sty 双栏 |
| **Tables** | 4 个已定义: `tab:logo-results` (per-gen LOGO), `tab:ablation` (feature ablation), `tab:baselines` (baseline comparison), `tab:downstream` (downstream PPL) |
| **Figures referenced** | 4 个需制作: `fig:feature-drift` (§5.2 drift vs stationarity), `fig:baseline-ci` (§5.3 CI forest plot), 另有 Fig 2 (§5.1 per-gen/per-class) 和 Fig 4 (§5.4 downstream bar chart) 需在正文中补 `\ref` 或移至 appendix |
| **Citations needed** | 无外部 citation 在 Results 内引用 (检测器名称如 FastDetectGPT、Binoculars、LD-Score 在 Method/Related Work 中已引); `Appendix~\ref{app:length}` 需在 appendix 中建立对应 label |
| **Notes** | (1) Binoculars 使用 bugfix 后数值 0.579 ✓; (2) 全部数字来自 registry 确认 (plan-014, plan-015-v2, plan-004-v2, plan-002-eval, plan-003, plan-013); (3) §5.4 负面结果以 diagnostic-not-curative framing 如实报告; (4) 未使用 "dual dynamics"/"H1/H2"/"discovery" 等禁用术语; (5) 5-class fine-grained 结果 (F1=0.505) 未放入主文, 可移至 appendix |

---
