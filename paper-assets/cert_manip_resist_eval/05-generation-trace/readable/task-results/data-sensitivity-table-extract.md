# data sensitivity table extract

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_sensitivity-table-extract_20260523T101251_result.json`
- **Structured JSON:** [`309d8f41fb93a0f5829d.json`](../../sessions/30/309d8f41fb93a0f5829d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。汇总：

- **36 行完整**，按 K=3/5/7 分组，每组 12 行（MMLU×6 + ARC×6）
- `rv_exceeds_eta` 计数：K=3: 1/12, K=5: 3/12, K=7: 4/12, 总计 8/36（即 28/36 条件下 η_max 超过 RV）
- RV 范围：K=3 [0.105, 0.419] 中位数 0.297；K=5 [0.064, 0.455] 中位数 0.215；K=7 [0.005, 0.522] 中位数 0.206；全局 [0.005, 0.522]
- 所有数值精确取自 JSON（表格行保留 3 位小数，文件末尾附有 5 位精度参考值）
- 输出路径：`docs/paper/data/sensitivity_table_data.txt`

---
