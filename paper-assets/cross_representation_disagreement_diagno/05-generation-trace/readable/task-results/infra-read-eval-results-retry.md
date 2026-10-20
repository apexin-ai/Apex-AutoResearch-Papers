# infra read eval results retry

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read_eval_results_retry_20260515T001442_result.json`
- **Structured JSON:** [`a52b3a4edbf84ed425c8.json`](../../sessions/a5/a52b3a4edbf84ed425c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量结果如下：

## 204 样本评估 (`mvp_v4_full.jsonl`)

| 指标 | 结果 | 阈值 | 状态 |
|------|------|------|------|
| C1 disagree_rate | 39.6% (76/192) | ≥10% | **PASS** |
| C2 diagnostic_rate | 86.8% (66/76) | ≥40% | **PASS** |
| C3 error_types | 3 types | ≥2 | **PASS** |
| C4 targeted_vs_blind | +8.3pp (T:61/96 B:53/96) | >5pp | **PASS** |
| C5 localization | 85.0% (34/40) | ≥60% | **PASS** |

**MVP RESULT: 5/5 PASS → PROCEED**

排除 GT=Unknown 后，C4 降至 +0.0pp FAIL，但全样本口径 5/5 通过。

## 其他状态

- **repair_fixed**: 尚未生成，`repair_only.py` 正在运行中（PID 64317/64370）
- **pipeline 进程 57877**: 仍存活

---
