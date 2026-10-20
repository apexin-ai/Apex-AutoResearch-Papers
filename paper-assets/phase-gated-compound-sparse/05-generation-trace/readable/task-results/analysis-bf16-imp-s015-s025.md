# analysis bf16 imp s015 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_imp_s015_s025_20260514T062105_result.json`
- **Structured JSON:** [`133ffdad9467e4c7988c.json`](../../sessions/13/133ffdad9467e4c7988c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。汇总：

## bf16 Importance Masking 实验结果

| 指标 | bf16 s=0.15 | bf16 s=0.25 | fp16 s=0.15 (ref) | fp16 s=0.25 (ref) |
|------|-------------|-------------|--------------------|--------------------|
| **II high median** | 0.006 | 0.032 | ~0.25 | ~0.68 |
| **II mid median** | 0.081 | 1.118 | — | — |
| **II low median** | 0.398 | 7.196 | 2.88 | 24.16 |
| **gradient (lo/hi)** | **69.2x** | **222.4x** | 11.53x | 35.72x |
| **CI overlap** | PASS | PASS | — | — |
| **sign reversal** | PASS | FAIL (hi≈0) | — | — |
| **overall** | **PASS** | **PASS** | — | — |
| **PPL high (both)** | 1.59 | 2.70 | — | — |
| **PPL low (both)** | 12.51 | 63.67 | — | — |
| **n_problems** | 50 | 50 | — | — |

**关键发现：**
- 两个实验均为强阳性，gradient >> 1，单调递增 high < mid < low
- bf16 gradient 比 fp16 更大（69x vs 12x, 222x vs 36x），原因是 bf16 high phase II 更接近 0（importance masking 在 high phase 几乎完全消除了 compound sparsity 交互效应）
- bf16 low phase II 绝对值低于 fp16（0.40 vs 2.88, 7.20 vs 24.16），说明 bf16 数值精度下 PPL 整体偏低，但相对梯度更陡
- s=0.25 的 sign_reversal 未通过，因为 high phase II 虽接近 0 但略为正值（median=0.032），不影响整体结论
- s=0.25 compound sparsity 效应约为 s=0.15 的 5x（PPL: 63.67 vs 12.51）

---
