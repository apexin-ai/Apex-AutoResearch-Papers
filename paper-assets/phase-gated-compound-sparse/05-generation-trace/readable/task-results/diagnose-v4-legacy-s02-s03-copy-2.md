# diagnose v4 legacy s02 s03

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4-legacy-s02-s03_20260514T000556_result.json`
- **Structured JSON:** [`af6ed04a8aae21e11aee.json`](../../sessions/af/af6ed04a8aae21e11aee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完毕。

## 总结

### 实验状态

| 实验 | 状态 | Verdict | 关键指标 |
|------|------|---------|----------|
| **mvp_v4_legacy_s01** (sparsity=0.1) | DONE ✓ | **FAIL** | II[high]=−0.11, II[mid]=−15.97；sparsity 太低，无信号分离 |
| **mvp_v4_legacy_s02** (sparsity=0.2) | DONE ✓ | **PASS** | II[high]=+21.29 CI=[+0.03,+63.16], II[mid]=+21.87 CI=[+4.99,+41.79]；low vs mid CI 不重叠 |
| **mvp_v4_legacy_s03** (sparsity=0.3) | DONE ✓ | **FAIL** | II[high]=−224.51（负值，pruning 过度），II[mid]=+54.00 但 CI 跨零 |
| **mvp_v4_random_r2** (random baseline) | **仍在运行** | — | 当前进度 26/50，PID 32187 alive |

### 结果目录

| 目录 | 文件 |
|------|------|
| `profiling_output_v4a/` | `profiling_results.json` (s01) |
| `profiling_output_v4b/` | `profiling_results.json` (s02, 2.7MB) |
| `profiling_output_v4c/` | `profiling_results.json` (s03, 2.7MB) |
| `profiling_output_v4_random_r2/` | 空（random 仍在跑） |

### 关键发现

**只有 sparsity=0.2 (s02) 通过了 CI 检验**——importance-based masking 在 20% sparsity 下能产生显著的 phase 区分度（II > 0 且 CI 不含零）。0.1 太弱无信号，0.3 太激进导致 high_sparsity II 反转为大负值。

---
