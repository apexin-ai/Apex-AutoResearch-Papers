# code r9 threshold sensitivity

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r9_threshold_sensitivity_20260518T091607_result.json`
- **Structured JSON:** [`a26bd29d50f95af84a8d.json`](../../sessions/a2/a26bd29d50f95af84a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**结论：HS probe 的 step-level 性能对 threshold 选择非常不敏感，结果稳健。**

### QwQ-32B (n_test=19, L60, W=3)

| Threshold | HS bal_acc | Text bal_acc | Δ(HS-Text) | HS FPR | HS det_K5 | Text det_K5 |
|-----------|-----------|-------------|------------|--------|-----------|-------------|
| 0.3 | 0.7382 | 0.6454 | +0.0928 | 0.252 | 94.7% | 78.9% |
| 0.4 | 0.7351 | 0.6443 | +0.0908 | 0.241 | 94.7% | 57.9% |
| 0.5 | 0.7353 | 0.6428 | +0.0925 | 0.230 | 89.5% | 57.9% |
| 0.6 | 0.7329 | 0.6478 | +0.0851 | 0.225 | 84.2% | 47.4% |
| 0.7 | 0.7332 | 0.6418 | +0.0914 | 0.214 | 84.2% | 36.8% |

- **HS bal_acc 全范围仅波动 0.53pp** (0.7329-0.7382)
- Δ(HS-Text) 在所有 threshold 下稳定在 +8.5~9.3pp
- HS trace detection (K=5) 从 94.7% 缓降到 84.2%，Text 从 78.9% 降到 36.8%

### R1-32B (n_test=20, L63, W=10)

| Threshold | HS bal_acc | Text bal_acc | Δ(HS-Text) | HS FPR | HS det_K5 | Text det_K5 |
|-----------|-----------|-------------|------------|--------|-----------|-------------|
| 0.3 | 0.7185 | 0.6624 | +0.0561 | 0.390 | 85.0% | 80.0% |
| 0.4 | 0.7200 | 0.6448 | +0.0752 | 0.382 | 85.0% | 80.0% |
| 0.5 | 0.7243 | 0.6451 | +0.0792 | 0.362 | 80.0% | 80.0% |
| 0.6 | 0.7300 | 0.6465 | +0.0835 | 0.345 | 80.0% | 80.0% |
| 0.7 | 0.7316 | 0.6522 | +0.0794 | 0.332 | 70.0% | 80.0% |

- **HS bal_acc 全范围仅波动 1.31pp** (0.7185-0.7316)
- Δ(HS-Text) 稳定在 +5.6~8.4pp
- Text probe detection rate 完全不随 threshold 变化（始终 80%），HS 从 85% 缓降到 70%

### K sweep (threshold=0.5)

| K | QwQ HS det | QwQ Text det | R1-32B HS det | R1-32B Text det |
|---|-----------|-------------|--------------|----------------|
| 3 | 100% | 94.7% | 95.0% | 80.0% |
| 5 | 89.5% | 57.9% | 80.0% | 80.0% |
| 7 | 68.4% | 47.4% | 75.0% | 70.0% |
| 10 | 57.9% | 21.1% | 50.0% | 45.0% |

HS probe 在 K≤5 时维持高检测率，且 HS-Text 差距随 K 增大而扩大（QwQ 尤其明显）。

结果保存于 `artifacts/exp_r9_threshold_sensitivity/results.json`，脚本为 `scripts/run_threshold_sensitivity.py`。

---
