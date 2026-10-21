# code mvp analysis script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-analysis-script_20260514T150049_result.json`
- **Structured JSON:** [`ba8f08fdc06233763340.json`](../../sessions/ba/ba8f08fdc06233763340.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。当前结果：

- **MVP: PASS**（基于 seed42 + seed123，2/3 seeds）
- adaptive 改善均值 +0.0526 > 90% × grid 改善均值 +0.0455（ratio=1.15）
- seed456 缺 grid 数据，未纳入判定
- 两个 seed 的 grid best-b 都是 0.5
- adaptive_fix b* 均值约 1.4，范围 [0.005, 20.0]

脚本位于 `/root/provenance_weight_training/analyze_mvp.py`，支持 `--export-json`、`--threshold` 参数，自动处理 TBD 缺失实验。

---
