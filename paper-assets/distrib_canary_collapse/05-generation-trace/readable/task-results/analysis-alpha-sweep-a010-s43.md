# analysis alpha sweep a010 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a010_s43_20260519T003747_result.json`
- **Structured JSON:** [`d5da79dcf6085239446f.json`](../../sessions/d5/d5da79dcf6085239446f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## alpha_sweep_a010_s43 分析结果

### 训练状态
- 正常完成 (EXIT_CODE=0), 11 generations (gen0-gen10)

### Drift (gen0 → gen10)

| Metric | Drift% |
|--------|--------|
| token_entropy | **-13.1%** |
| ece | -61.1% |
| perplexity | -38.9% |
| distinct_1 | **-29.1%** |
| distinct_2 | -40.3% |
| distinct_3 | -31.9% |
| effective_rank | +23.5% |
| mauve | -46.3% |

### 5-Method Lead-Lag

| Method | Score |
|--------|-------|
| naive_xcorr | 7/8 |
| diff_xcorr (BH-FDR) | 8/8 |
| threshold_onset | 3/8 |
| **perm_granger fwd** | **0/8** |
| perm_granger rev | 0/8 |
| **ty_granger** | **0/8** |
| **K>=4/5** | **0/8** |

### 对比

**vs fp32 s42 (a010_s42):**
- Diversity collapse 缓解: d1 -29.1% (bf16) vs -39.7% (fp32), d3 -31.9% vs -58.9% → D079 confirmed, bf16 抑制 collapse 27-46%
- ECE 方向逆转: bf16 -61.1% (改善) vs fp32 +57.4% (恶化)
- Effective rank 方向逆转: bf16 +23.5% vs fp32 -3.1%
- Causal signal 不变: 两者 PermG/TY 均 0/8

**vs null a000_s43:**
- Drift 幅度可区分 (d1 2.1x, d2 4.1x, d3 6.7x, entropy 3.0x)
- 但 causal lead-lag 不存在 → 盲区复现

**D078 精度桥梁:** bf16 不消除盲区，只减小 collapse 幅度。ECE/eff_rank 在 bf16 下行为模式与 fp32 完全不同。

### Conclusion: **success**

D075 盲区验证通过。α=0.10 存在实质性 diversity collapse 但 canary 无因果先导信号 (PermG 0/8, TY 0/8, K>=4 0/8)。Correlation methods (naive 7/8, diff 8/8) 检出 co-movement 但非 temporal precedence。Registry 已更新为 DONE(success)。

---
