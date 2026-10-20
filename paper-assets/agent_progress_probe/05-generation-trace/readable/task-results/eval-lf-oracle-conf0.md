# eval lf oracle conf0

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lf_oracle_conf0_20260514T092025_result.json`
- **Structured JSON:** [`285eddcc18cc8c97e157.json`](../../sessions/28/285eddcc18cc8c97e157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。关键发现：

**LF Majority Vote 仍然是 1.0** — 因为 `predict_majority_vote()` 直接返回 `w["majority_label"]`，而 ground truth 也是 `w["majority_label"]`，所以不论 conf 值如何都是恒等式。这不是 conf≥0 独有的问题，是代码实现的循环性。

**全量 conf≥0 结果表：**

| Method | Macro-F1 | Accuracy |
|--------|----------|----------|
| GRU Probe (probe_001 ref) | 0.9055 | — |
| LF Majority Vote | 1.0000 (tautological) | 1.0000 |
| LF Any-Stagnation | 0.8002 | 0.8141 |
| LF All-Agreement | 0.8543 | 0.8985 |
| Single LF: file_diff_delta | 0.7573 | 0.8457 |
| Single LF: command_repetition | **0.7460** | 0.8122 |
| Single LF: outcome_backpropagation | 0.5931 | 0.6976 |

**与 conf≥2 对比：**
- `command_repetition` 单独：0.9451 → **0.7460**（降 0.20），循环性在全量数据上大幅减弱
- `file_diff_delta` 单独：0.7573，全量上反而成为最好的单 LF
- 所有单 LF 和组合策略都低于 GRU Probe 的 0.9055

**Test 集标签分布：** stagnation=2,230 (27.5%) / progress=5,871 (72.5%)，类别不均衡程度与 conf≥2 类似。

**LF 覆盖率（test set）：** file_diff_delta 59.8%, command_repetition 72.1%, outcome_backpropagation 24.7%。

如果需要修复 Majority Vote 的循环性（从 raw LF labels 重新计票而非直接读 `majority_label`），可以后续改。

---
