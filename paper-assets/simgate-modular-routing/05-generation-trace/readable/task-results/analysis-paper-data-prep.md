# analysis paper data prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-data-prep_20260514T062541_result.json`
- **Structured JSON:** [`7807db1562648beb549b.json`](../../sessions/78/7807db1562648beb549b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已产出 `artifacts/paper_data_tables.md`（artifact ID: art_20260514_3c02f5），包含：

**Table 1**: Death decomposition 完整数据（plan-012-full 最终版：Δ_full=+29.60, DAF=90.41%, r=0.9698）+ 5/11 tasks 有 per-task 明细，6 tasks 需从服务器提取

**Table 2**: Router SFT — plan-004-ablation-b 完整指标（accuracy=0.6536, internal recall=0.5152），plan-002-v4 标记为 RUNNING placeholder

**Table 3**: Baselines — keyword routing 3 版全部 degenerate，always-det/always-internal 对比

**Figure specs**: 3 张图的数据源、轴定义、优先级（Fig 1 scatter plot 必须，Fig 2/3 可选）

**Consistency check 结果**:
- paper_framing.md 11 项定量 claim 全部与 registry 一致
- **1 项未验证**："98.2% tie rate" 无 registry 来源，需补源或从数据重算
- 旧 experiment_tables.md 的 30-task 预筛数据已标注为 superseded

**7 个 action items** 按优先级列出，最关键的：(1) 从服务器提取 6 个 task 的 per-task 分解数据，(2) 补齐绝对分数，(3) 找到 98.2% tie rate 的来源，(4) 等 plan-002-v4 完成填表。

---
