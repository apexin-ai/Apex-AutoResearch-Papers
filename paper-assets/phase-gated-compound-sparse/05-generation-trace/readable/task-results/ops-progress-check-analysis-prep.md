# ops progress check analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-analysis-prep_20260515T005421_result.json`
- **Structured JSON:** [`5fedf524f19b725b26d3.json`](../../sessions/5f/5fedf524f19b725b26d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 实验进度

| Condition | DeepSeek | Qwen |
|-----------|----------|------|
| s015_imp | **DONE** (n=500) | **DONE** (n=500) |
| s015_rand | **DONE** (n=500) | **DONE** (n=500) |
| s020_imp | **DONE** (n=500) | **DONE** (n=500) |
| s020_rand | **DONE** (n=500) | **DONE** (n=500) |
| s025_imp | **Running** (235/500) | **Running** (367/500) |
| s025_rand | **Running** (286/500) | **Running** (340/500) |
| s030_imp | Pending | Pending |
| s030_rand | Pending | Pending |

GPU 利用率：4 卡均在 77-79%，~30-34GB VRAM / 98GB，运行正常。

**进度估算**：
- Qwen s025: ~70% 完成，按当前速度约 1-1.5h 后完成 s025，之后跑 s030
- DeepSeek s025: ~47-57% 完成，比 Qwen 慢

### 2. 分析脚本状态

- `analyze_n500_unified.py` 存在且可 import
- 依赖 OK：scipy 1.17.1, numpy 2.2.6
- B_BOOT = **10000** (硬编码，非 argparse 参数)
- N_PERM = 5000
- argparse 参数：`--model {deepseek,qwen,all}`, `--dry-run`, `--csv`, `--latex`
- 支持 4 个 sparsity levels: s015, s020, s025, s030

### 3. 输出目录结构

每个已完成 condition 输出单个 `profiling_results.json`（~18-22MB），内含 `per_problem_ii` 字段，每条 n=500。所有完成的 8 个 condition 数据量一致，无异常。

### 异常发现

无。一切按预期运行。

---
