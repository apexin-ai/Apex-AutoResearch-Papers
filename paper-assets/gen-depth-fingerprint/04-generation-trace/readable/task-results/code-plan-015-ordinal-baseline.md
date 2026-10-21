# code plan 015 ordinal baseline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-015-ordinal-baseline_20260515T000746_result.json`
- **Structured JSON:** [`a7abc43c660caf1b8e07.json`](../../sessions/a7/a7abc43c660caf1b8e07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Detector | 5-fold F1 | LOGO F1 | Spearman ρ |
|---|---|---|---|
| LD-Score | 0.6607 | 0.6596 | 0.6837 |
| FastDetectGPT | 0.6938 | 0.6824 | 0.4174 |
| **Avg-LogProb** | **0.7592** | **0.7564** | **0.7282** |
| Binoculars | 0.5306 | 0.5300 | -0.5145 |
| **7-feature ensemble** | **0.8024** | **0.7980** | — |

关键发现：

1. **三个指定检测器均未超过 0.70 LOGO F1**：FastDetectGPT (0.68)、LD-Score (0.66)、Binoculars (0.53)。论文贡献定位安全。

2. **Avg-LogProb** (pythia-410m 下的平均 log 概率) 达到 0.76 LOGO F1，超过 0.70 阈值，但仍低于 7-feature 模型 4.2 个百分点。需要在论文中将其作为 baseline 讨论。

3. **所有检测器在 gen-1 类上表现最差**：Binoculars gen-1 F1=0.00，FastDetectGPT gen-1 F1=0.37。这表明区分"首次生成"vs"人写"是最难的——正是我们 7-feature 模型的优势所在 (gen-1 F1=0.62)。

4. 脚本和结果已保存在服务器 `/root/gen-depth-fingerprint/scripts/ordinal_baseline.py` 和 `results/ordinal_baseline_results.json`。registry plan-015 已更新为 DONE。

---
