# eval cls8b eval seed42

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-eval-seed42_20260512T172229_result.json`
- **Structured JSON:** [`3df9d9d14f78bfbbe1f7.json`](../../sessions/3d/3df9d9d14f78bfbbe1f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**8B CLS seed42 eval 结果**
- 测试集：1890 条，pass/fail 比例 51.7%/48.3%
- **Overall accuracy: 90.48%**（baseline 51.7%，gap +38.7pp）
- fail F1: 90.06%，pass F1: 90.86%
- Unparseable: 0
- MVP-B 全部 PASS

**输出文件**（服务器 `/home/sonny/exec-sim-repair-verifier/eval_results/`）：
- `cls8b_seed42.json` — 聚合指标
- `cls8b_seed42_predictions.json` — 1890 条 per-instance predictions（含 index, problem_id, label, prediction, correct）

Registry `cls8b-eval-seed42` 已更新为 DONE/success。

---
