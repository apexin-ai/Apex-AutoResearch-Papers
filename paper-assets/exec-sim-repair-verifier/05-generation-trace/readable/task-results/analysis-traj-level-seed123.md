# analysis traj level seed123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_traj-level-seed123_20260512T075126_result.json`
- **Structured JSON:** [`8e1d1936d32e74ba6bdf.json`](../../sessions/8e/8e1d1936d32e74ba6bdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练和评估均正常完成（EXIT_CODE=0），eval_loss=0.1048，train_loss=0.2261。

## 指标
- accuracy: 85.47%
- unresolved_f1: 87.00%
- resolved_f1: 83.52%
- per_test_consistency: 78.59%

## 对比

**vs traj-level seed=42:**

| 指标 | seed=42 | seed=123 | diff |
|------|---------|----------|------|
| accuracy | 85.66% | 85.47% | -0.19pp |
| unresolved_f1 | 87.50% | 87.00% | -0.50pp |
| resolved_f1 | 83.18% | 83.52% | +0.34pp |
| per_test_consistency | 79.94% | 78.59% | -1.35pp |

**vs per-test classification 3-seed mean (88.41%):**
- accuracy gap = -2.94pp（seed=42 gap 为 -2.75pp）

## 结论
- **[success]** Seed=123 结果与 seed=42 高度一致（accuracy 差仅 0.19pp），确认 traj-level 方法的 ~3pp gap（vs per-test classification）在不同 seed 下稳定存在，非随机波动。两个 seed 的 gap 分别为 2.75pp 和 2.94pp，均在 per-test 的 1σ 范围内（std=0.96）但方向一致偏低。

---
