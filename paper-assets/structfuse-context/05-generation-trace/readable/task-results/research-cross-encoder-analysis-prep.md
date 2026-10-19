# research cross encoder analysis prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cross-encoder-analysis-prep_20260513T104034_result.json`
- **Structured JSON:** [`617c09381cd563724080.json`](../../sessions/61/617c09381cd563724080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入并注册。功能概要：

- **输入**: 读取 `pilot_results.json`（支持 flat 和 nested 两种 JSON 格式，路径可通过命令行参数覆盖）
- **输出**:
  - Markdown 对比表 + LaTeX 表（最优值加粗）
  - 策略 delta（embedding/dataflow vs random）和 encoder delta（Qwen vs StarCoder）
  - 策略排序一致性分析 → 判定是否支持 encoder-agnostic claim
  - 自动生成文字结论（best config、encoder gap、embedding lift、R@5 saturation）
  - 同时写出 `cross_encoder_report.md` 和 `cross_encoder_table.tex` 到同目录

运行方式：`python cross_encoder_analysis.py [path_to_pilot_results.json]`，零外部依赖。

---
