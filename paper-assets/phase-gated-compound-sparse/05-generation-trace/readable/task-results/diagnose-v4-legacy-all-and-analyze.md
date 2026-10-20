# diagnose v4 legacy all and analyze

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4-legacy-all-and-analyze_20260514T001037_result.json`
- **Structured JSON:** [`9c12dcb52ab84490128e.json`](../../sessions/9c/9c12dcb52ab84490128e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s01 registry 更新完毕。

## 总结

### s01 (importance, sparsity=0.1, cuda:0)
- **状态**: 完成，Verdict=**FAIL**，conclusion → negative
- **关键指标**:

| Phase | II mean | 95% CI | 判定 |
|-------|---------|--------|------|
| high_sparsity | -0.11 | [-0.81, +0.41] | CI 跨零 |
| mid_sparsity | -15.97 | [-47.99, +1.29] | CI 跨零 |
| low_sparsity | 0.00 | [0.00, 0.00] | 零（无 KV 剪枝） |

- sparsity=0.1 太低，pruning 信号几乎不可区分

### random_r2 (random baseline, sparsity=0.1-0.3, cuda:3)
- **状态**: 仍在跑，进度 **28/50**（最新日志 08:10）
- 预计剩余 ~30 分钟（~2 min/problem × 22 problems）
- Registry 不动

### 分析脚本
等 random_r2 完成后再跑 `analyze_v4_comparison.py`。

### 四实验汇总

| Exp ID | Masking | Sparsity | Verdict | II[high] | II[mid] | 状态 |
|--------|---------|----------|---------|----------|---------|------|
| s01 | importance | 0.1 | FAIL | -0.11 (CI跨零) | -15.97 (CI跨零) | DONE/negative |
| s02 | importance | 0.2 | PASS | +21.29 (全正) | +21.87 (全正) | DONE/success |
| s03 | importance | 0.3 | FAIL | -224.5 (CI跨零) | — | DONE/negative |
| random_r2 | random | 0.1-0.3 | — | — | — | RUNNING 28/50 |

**关键发现**: importance masking 在 sparsity=0.2 是甜点——0.1 太弱无信号，0.3 过强导致 catastrophic degradation。等 random baseline 完成后可对比 importance vs random 的 II 差异。

---
