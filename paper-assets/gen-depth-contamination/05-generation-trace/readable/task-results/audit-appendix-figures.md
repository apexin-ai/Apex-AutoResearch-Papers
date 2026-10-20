# audit appendix figures

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix_figures_20260525T194410_result.json`
- **Structured JSON:** [`ce2591ee0e70d615870e.json`](../../sessions/ce/ce2591ee0e70d615870e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `artifacts/audit_appendix_figures.md`。

**核心发现：**

**高优先级问题 (3个)：**
1. **Fig 2 & Fig 3a Pythia scorer不一致** — 图使用self-scored (1v2=0.6539)，表格使用Qwen-scored (0.6074)，差异8.4pp。Mistral 0v1也有类似问题 (0.9843 vs 0.9209)。OLMo 1v2=0.5079来源不明（既非self=0.6145也非Qwen=0.5001）。
2. **Fig 3b caption完全错误** — caption声称显示"6-class ordinal accuracy"和4个模型，实际显示0v1 AUC和3个模型（无Qwen-rw）。
3. **OBD per-depth recall与overall accuracy矛盾** — (96+39+14+19+22)/500=38.0%，但报告38.6%。

**中优先级 (5个)：** Claude d3 recall .100应为.101；Tab s10 CI upper 0.606应为0.6025；Tab s13 OLMo "Self" K*定义歧义；Small→27B avg 76.5%算术不符 (实际80.4%)；arXiv JSD text=0.077 vs figure data=0.057。

**结构性问题：** 6个figure中4个的数据完全硬编码在Python脚本中（非从实验输出读取），仅transfer heatmap从JSON读取。

---
