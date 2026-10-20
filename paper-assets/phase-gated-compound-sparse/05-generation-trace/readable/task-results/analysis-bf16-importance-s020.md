# analysis bf16 importance s020

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_importance_s020_20260514T063748_result.json`
- **Structured JSON:** [`a0893030adea784b5f24.json`](../../sessions/a0/a0893030adea784b5f24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bf16_importance_s020 实验结果

### Interaction Index (sparsity=0.20)

| Phase | Mean | 95% CI | Median | Winsorized Mean | Skewness | Outliers |
|-------|------|--------|--------|-----------------|----------|----------|
| high_sparsity | **+0.1289** | [-0.1975, +0.6647] | +0.0145 | -0.0297 | 16.67 | 2 |
| mid_sparsity | **+1.2604** | [+0.7466, +1.8962] | +0.2027 | +0.7660 | 7.05 | 4 |
| low_sparsity | **+6.0288** | [+4.4671, +7.9237] | +1.4963 | +4.3426 | 6.01 | 8 |

### Perplexity

| Phase | Dense | Attn-only | KV-only | Both |
|-------|-------|-----------|---------|------|
| high_sparsity | 1.1689 | 1.5233 | 1.6191 | 2.1047 |
| mid_sparsity | 1.2269 | 1.5375 | 3.5164 | 5.4246 |
| low_sparsity | 1.2286 | 1.6486 | 15.7987 | 23.7400 |

### Phase Stats

| Phase | Tokens | Segments |
|-------|--------|----------|
| high_sparsity | 21,086 | 387 |
| mid_sparsity | 13,306 | 191 |
| low_sparsity | 27,748 | 397 |

### 数据完整性
- **per_problem_ii: 50 条（完整）**
- **NaN count: 0**
- Pass/Fail: **PASS**（CI overlap test 通过：low vs mid CI 不重叠）

### 与 s015/s025 对照

| Phase | s015 | **s020** | s025 |
|-------|------|----------|------|
| II_high | -0.1502 | **+0.1289** | +0.3028 |
| II_mid | +0.4473 | **+1.2604** | +5.7297 |
| II_low | +2.4058 | **+6.0288** | +25.8530 |

s020 的 II 值处于 s015 和 s025 之间，单调递增趋势符合预期。bf16 消除了 NaN 问题，50 条 per_problem_ii 数据完整无缺失。

---
