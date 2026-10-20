# analysis f1 stag breakdown

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-breakdown_20260514T191050_result.json`
- **Structured JSON:** [`9e62750b14e4a748f934.json`](../../sessions/9e/9e62750b14e4a748f934.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### 5 维 F1_stag Breakdown 结果

**Dim1 - Confidence**: f1_stag 随 confidence 单调递增 (0.74 → 0.85 → 0.94)。conf=2 的瓶颈是 recall_stag=0.77，precision 已达 0.95。

**Dim2 - Trajectory 长度**: 中等长度 (10-30步) f1_stag 最低 (0.66, recall 仅 0.60)。长 trajectory (>30) 表现最好 (0.78)。

**Dim3 - LF 一致性**: 最强预测因子。LF 一致时 f1_stag > 0.94；3-LF 2v1 分裂时降至 0.76 且 f1_prog 也大跌至 0.72。

**Dim4 - Outcome**: resolved trajectory 在 conf≥2 下 f1_stag 仅 0.33（stag 样本太少）；unresolved 为 0.85。

**Dim5 - 错误子类型 (conf≥2)**:
- 195 个错误中 166 个 (85%) 是 missed stagnation
- 这 166 个错误 **100% 来自 unresolved trajectory**，89% 是 **3lf_2v1_split** pattern（OB 投 progress 但 majority 标为 stag）
- 平均 sigmoid prob=0.78，是**高置信度盲点**
- 58% 集中在 trajectory 最后 1/3

**核心结论**: probe 的 f1_stag 瓶颈 = recall_stag。主要错误模式是 OB 与其他 LF 分歧时，probe 跟随 OB 判断而漏掉真实 stagnation。

产出已保存：
- 服务器: `results_f1_stag_breakdown.json`
- 本地项目: `memory.md` 含完整分析摘要

---
