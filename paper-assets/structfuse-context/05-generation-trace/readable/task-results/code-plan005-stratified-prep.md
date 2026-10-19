# code plan005 stratified prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan005-stratified-prep_20260515T050005_result.json`
- **Structured JSON:** [`ed66327869767a6deba7.json`](../../sessions/ed/ed66327869767a6deba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成**：
- **`prepare_stratification_index.py`** — 已运行，从 44,173 条 all.jsonl 构建了 19MB 元数据索引（34.3% 有结构数据，条件 Z%=78.0%）
- **`evaluate_stratified.py`** — GPU 评估脚本，支持多 pool_size（D038），dry-run 验证通过
- **`analyze_stratified.py`** — 5 维分层分析 + bootstrap CI + PDF 图表，dry-run 验证通过（输出 JSON + CSV + 5 个 PDF）
- **`stratification_index.json`** — 已保存到 `/root/autodl-tmp/structfuse/stratification_index.json`
- **规格文档** — 已注册 artifact

**待 M2 checkpoint**：运行 `evaluate_stratified.py` 对 18 个 run（2 encoder × 3 strategy × 3 seed）生成 per-query 结果，然后 `analyze_stratified.py` 一键出全部分析。

---
