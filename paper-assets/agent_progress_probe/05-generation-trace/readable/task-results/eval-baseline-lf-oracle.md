# eval baseline lf oracle

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline-lf-oracle_20260514T154835_result.json`
- **Structured JSON:** [`a0773c2951ed4bbd6dad.json`](../../sessions/a0/a0773c2951ed4bbd6dad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 `/root/autodl-tmp/agent_progress_probe/lf_ensemble_baselines.py` 已完成，结果保存到 `lf_ensemble_baseline_results.json`。

## conf≥2 Test Set (N=1824)

| Method | M-F1 | Acc | F1stag | F1prog |
|---|---|---|---|---|
| GRU Probe (probe_001) | 0.9055 | 0.9282 | 0.8593 | 0.9518 |
| **Majority Vote (≡ GT)** | **1.0000** | 1.0000 | 1.0000 | 1.0000 |
| Any-Stagnation | 0.8544 | 0.8712 | 0.8050 | 0.9038 |
| All-Stagnation | 0.7659 | 0.8542 | 0.6222 | 0.9096 |
| Weighted Vote | 0.8154 | 0.8794 | 0.7067 | 0.9241 |
| Single: file_diff_delta | 0.7636 | 0.8531 | 0.6182 | 0.9090 |
| **Single: command_repetition** | **0.9451** | 0.9589 | 0.9175 | 0.9726 |
| Single: outcome_backpropagation | 0.7510 | 0.7955 | 0.6458 | 0.8563 |

## 关键发现

1. **MV ≡ GT**: conf≥2 test set 的标签就是 MV 生成的，所以 MV 达到 1.0 是恒等式，不是真正的预测能力

2. **command_repetition 单 LF (0.9451) > probe (0.9055)**: 因为 cmd_rep 覆盖率 97.4%，且在 conf≥2 test set 上它几乎总是属于多数投票方。这说明 probe 在 conf≥2 上没有超过最佳单 LF

3. **Probe 的真正价值在 conf=1 区间**: 39408 个 ambiguous 窗口（70% 只有 1 个活跃 LF，30% 是 2 个 LF 分歧），probe 目前未在该区间评估（仅在 conf≥2 上训练/测试）

4. **非平凡 baseline 最佳**: Any-Stagnation (0.8544)，probe 比它高 +0.0511

---
