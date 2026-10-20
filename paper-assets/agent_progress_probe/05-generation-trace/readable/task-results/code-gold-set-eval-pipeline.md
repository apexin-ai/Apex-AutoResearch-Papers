# code gold set eval pipeline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gold-set-eval-pipeline_20260514T223954_result.json`
- **Structured JSON:** [`367f66164abb5d58ab65.json`](../../sessions/36/367f66164abb5d58ab65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 端到端验证通过。三个产出全部生成：
- `gold_set_results.json` — 完整指标 JSON
- `gold_set_reliability.pdf` — 校准曲线图
- Console markdown 表格

**文件**: `src/evaluation/gold_set_eval.py`

**已实现功能**:
1. 加载 CSV/JSONL gold 标注（支持 `annotator_id`, `confidence` 可选字段）
2. 六个评估对象：Silver MV、RF、GB、LR、GRU Probe、LLM-as-Judge
3. 按 `window_id` 对齐，报告未匹配数量
4. 指标：macro-F1、accuracy、per-class P/R/F1、Cohen's κ
5. 按 silver confidence (1/2/3) 分层统计 gold-silver agreement
6. Reliability diagram (calibration curve + prediction distribution)
7. `--models` 选择器可单独跑某些模型
8. 路径自动探测，兼容 `artifacts/data/`、`data/`、`checkpoints/` 等多种目录布局

---
