# diagnose exp015 check results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp015_check_results_20260515T104439_result.json`
- **Structured JSON:** [`17e5db40e8e035e11e56.json`](../../sessions/17/17e5db40e8e035e11e56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：SUCCESS** — 3 个模型全部完成，结果完整。

EXIT_CODE=129（SIGHUP）是进程在写完结果后被 kill，不影响数据完整性。

### 完整结果

| 模型 | K\*_neural | K\*_lgbm | Accuracy | AUC(0v1) | AUC(1v2) | AUC(2v3) | AUC(3v4) | AUC(4v5) |
|------|-----------|---------|----------|----------|----------|----------|----------|----------|
| **Pythia-1.4B** | 2 | 2 | 0.3892 | 0.966 | 0.676 | 0.596 | 0.555 | 0.532 |
| **OLMo-1B** | 2 | 2 | 0.3729 | 0.950 | 0.657 | 0.589 | 0.547 | 0.530 |
| **Qwen-cont** | **3** | 2 | 0.4368 | 0.988 | 0.702 | **0.616** | 0.590 | 0.566 |

关键发现：
- Neural probe 在所有模型上 AUC(2v3) 都高于 LightGBM baseline（Pythia: 0.596 vs 0.552, OLMo: 0.589 vs 0.550, Qwen: 0.616 vs 0.561）
- **Qwen-cont 是唯一 K\*_neural=3 的模型**（2v3 AUC=0.616 > 0.6 threshold），Pythia 和 OLMo 的 K\*_neural 与 K\*_lgbm 一致都是 2
- 所有 permutation test p-value = 0.0，统计显著

---
