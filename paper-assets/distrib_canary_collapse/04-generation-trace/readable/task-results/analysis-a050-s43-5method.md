# analysis a050 s43 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a050_s43_5method_20260516T195658_result.json`
- **Structured JSON:** [`4eaad8d61ccf51fc5a5f.json`](../../sessions/4e/4eaad8d61ccf51fc5a5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## α=0.50 seed=43 — 5-Method Lead-Lag 结果

| Pair | Naive | Diff FDR | Perm FDR | TY | Onset | Votes | Robust |
|------|-------|----------|----------|-----|-------|-------|--------|
| token_entropy→distinct_1 | ✓ | ✓ (0.015) | ✓ (0.042) | ✗ | ✗ | **3/5** | **✓** |
| token_entropy→distinct_2 | ✓ | ✓ (0.010) | ✗ (0.055) | ✗ | ✗ | 2/5 | ✗ |
| token_entropy→distinct_3 | ✓ | ✗ (0.051) | ✓ (0.042) | ✗ | ✗ | 2/5 | ✗ |
| token_entropy→perplexity | ✓ | ✓ (0.002) | ✗ (0.063) | ✗ | ✗ | 2/5 | ✗ |
| ece→distinct_1 | ✗ | ✓ (0.000) | ✓ (0.029) | ✗ | ✗ | 2/5 | ✗ |
| ece→distinct_2 | ✗ | ✓ (0.015) | ✓ (0.042) | ✗ | ✗ | 2/5 | ✗ |
| ece→distinct_3 | ✗ | ✗ (0.051) | ✓ (0.042) | ✗ | ✗ | 1/5 | ✗ |
| ece→perplexity | ✗ | ✓ (0.002) | ✓ (0.042) | ✗ | ✗ | 2/5 | ✗ |

### 汇总

- **Perm Granger FDR**: 6/8 显著
- **Diff XCorr FDR**: 5/8 显著
- **Naive XCorr**: 4/8（token_entropy 的 4 对，lag=1 方向正确）
- **TY Granger**: 0/8（与 C003 约束一致——α≤0.50 下 TY 不可靠）
- **Threshold Onset**: 0/8（None——α=0.50 退化不足以触发阈值）
- **Robust consensus (≥3/5)**: **1/8** — 仅 `token_entropy→distinct_1`

### 关键观察

1. Perm Granger 是最敏感的方法（6/8），但 reverse 方向全部不显著（0/8），证实前向因果方向
2. α=0.50 下信号较弱，多数 pair 只有 2 个方法达到显著——相比 α=0.75/1.0 的 robust pairs 数量明显少
3. TY Granger 全军覆没，印证 C003 约束（低 α 下 T=11 样本不足 + ADF 积分阶数不稳定）

产出已保存至：
- `results/alpha_sweep/a050_s43/analysis/5method_leadlag.json`
- `results/alpha_sweep/a050_s43/analysis/5method_summary.txt`

---
