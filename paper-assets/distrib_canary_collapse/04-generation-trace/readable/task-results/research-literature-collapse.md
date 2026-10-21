# research literature collapse

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-collapse_20260514T053157_result.json`
- **Structured JSON:** [`481dbf7a25f9e9176aae.json`](../../sessions/48/481dbf7a25f9e9176aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已就位，MCP 可正常读取。

---

## 调研完成，核心结论

**收录 23 篇论文**，覆盖 4 个类别：core-collapse (8)、canary-metrics (8)、data-mixing (6)、methodology (2)。

### 关键发现

**最直接的竞争者**：`chen2025scales` (arXiv 2510.05133) 明确报告 **"calibration degradation precedes accuracy loss"**——ECE 在 iteration 1 + 30% synthetic 时就上升 75%，而 accuracy 还未显著变化。但他们**未做 lead-lag 因果分析**，也没有多指标 panel。

**8 个文献空白**（详见 `gaps` 字段），最核心的三个：
1. 无人做过 canary 指标的 Granger causality / lead-lag 量化分析
2. ECE 在 collapse 场景下几乎未被系统研究（仅 1 篇）
3. 多指标 panel 框架完全缺失

**Novelty 评估**：我们的 panel Granger causality + 多指标 canary + α-dependent sensitivity 三个方向均有清晰的文献空白。主要风险是 chen2025scales 团队如果扩展他们的工作，会侵蚀我们在 ECE-as-canary 这个点上的 novelty——需要在方法论（Granger causality 框架）上尽快建立壁垒。

文件路径：
- 项目根：`literature_map.yaml`
- artifacts：`artifacts/literature_map.yaml`

---
