# analysis 5 paired clustered bootstrap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_5-paired-clustered-bootstrap_20260512T123207_result.json`
- **Structured JSON:** [`6cdf68f640b45eabef5f.json`](../../sessions/6c/6cdf68f640b45eabef5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `clustered_bootstrap_5paired.json`。

## 5-Paired Clustered Bootstrap 结果

### Pooled (跨 5 seed 平均)

| 指标 | 值 |
|------|-----|
| **Pooled gap (CLS - TRAJ)** | **-0.45pp** |
| **95% CI** | **[-1.71, +0.84]** |
| **p-value (H0: gap=0)** | **0.499** (不显著) |
| **TOST p-value (±2pp margin)** | **0.0071** (等价成立, p < 0.05) |
| N variants (pooled) | 523 |
| N clusters (problems) | 114 |

### Per-Seed Gaps

| Seed | CLS acc | TRAJ acc | Gap (pp) | 95% CI | p-value | TOST p |
|------|---------|----------|----------|--------|---------|--------|
| 42 | 84.69% | 85.66% | -0.97 | [-3.37, +1.62] | 0.460 | 0.203 |
| 123 | 86.92% | 85.47% | +1.45 | [-0.65, +3.73] | 0.203 | 0.318 |
| 456 | 85.56% | 87.40% | -1.84 | [-3.69, -0.09] | 0.048 | 0.430 |
| 789 | 84.11% | 84.88% | -0.78 | [-3.12, +1.59] | 0.509 | 0.161 |
| 0 | 85.56% | 85.85% | -0.29 | [-2.21, +1.57] | 0.803 | 0.039 |

### Seed-Level Paired T-test

- Mean gap: -0.48pp, SE: 0.55pp
- t = -0.888, p = 0.425
- Seed-level bootstrap CI: [-1.32, +0.52]

### 结论

1. **CLS 和 TRAJ 无显著差异** — pooled p=0.499, paired-t p=0.425, CI 包含 0
2. **TOST 等价成立** — pooled TOST p=0.0071 < 0.05，在 ±2pp margin 下两方法等价
3. 5 个 seed 中 4 个 CLS 略低于 TRAJ（平均 -0.45pp），seed 123 是唯一 CLS > TRAJ 的
4. seed 456 的 gap (-1.84pp) 在单 seed 分析中边缘显著 (p=0.048)，但 pooled 后消失

注：seed 789/0 的 CLS 和 TRAJ 均使用 4-bit 量化提取（精度比 bf16 低 ~2-3pp），但同 seed 内 CLS 和 TRAJ 使用相同量化，配对比较仍然有效。

---
