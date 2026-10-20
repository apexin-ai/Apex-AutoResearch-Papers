# ops qw data rescue

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qw_data_rescue_20260515T173304_result.json`
- **Structured JSON:** [`aa4f1f43e54ac64d95a8.json`](../../sessions/aa/aa4f1f43e54ac64d95a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## QW GSM8K Profiling 数据抢救结果

### 数据完整性
- **QW Importance**: 4/4 per-sparsity 完整，exit code=0，PASS
- **QW Random**: 3/4 per-sparsity 完整，`rand_s030` per-sparsity 目录为空（merged fallback 存在但可能有聚合 bug，同 DS）
- 两个 job 均处理了 50/50 problems，log 末尾显示 PASS verdict

### Per-Phase Per-Sparsity II 汇总（Median，更鲁棒）

| Sparsity | IMP low | IMP mid | IMP high | IMP gradient | RAND low | RAND mid | RAND high | RAND gradient |
|----------|---------|---------|----------|-------------|----------|----------|-----------|--------------|
| 0.15 | 0.046 | 0.009 | 0.001 | **0.045** | 0.105 | 0.086 | 0.081 | 0.024 |
| 0.20 | 0.124 | 0.025 | 0.002 | **0.122** | 0.329 | 0.235 | 0.203 | 0.126 |
| 0.25 | 0.902 | 0.150 | 0.006 | **0.896** | 1.271 | 0.835 | 0.722 | 0.549 |
| 0.30 | 2.637 | 0.771 | 0.016 | **2.621** | N/A | N/A | N/A | N/A |

### 关键发现
1. **IMP gradient 单调递增**：0.045 → 0.122 → 0.896 → 2.621，phase 分化随 sparsity 增大明显加剧
2. **IMP 的 phase 分化比 RAND 更清晰**：low >> mid >> high 的阶梯结构更陡峭（IMP high 接近 0，RAND high 相对更大）
3. **`rand_s030` 缺失**：per-sparsity 目录为空，merged 数据显示极端负值（-68, -88），与 DS 的聚合 bug 一致，不可信

### Registry
`gsm8k_profiling_qw` → status=DONE, conclusion=success

---
