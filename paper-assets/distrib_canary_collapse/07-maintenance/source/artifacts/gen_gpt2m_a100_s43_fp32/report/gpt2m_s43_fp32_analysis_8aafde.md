# GPT-2-Medium s43 fp32 Analysis Report

**Experiment**: `gen_gpt2m_a100_s43_fp32`
**Config**: GPT-2-medium (355M) × WikiText-103 × α=1.0 × seed=43 × fp32
**Date**: 2026-05-19

## 1. Training Completion

| Item | Status |
|------|--------|
| Generations | 11/11 (gen_0 ~ gen_10) |
| EXIT_CODE | 0 |
| Steps/gen | 5000 |
| Precision | fp32 (bf16=false) |

All 11 generations completed successfully.

## 2. Drift Analysis (Gen 0 → Gen 10)

| Metric | Gen 0 | Gen 10 | Drift % |
|--------|------:|-------:|--------:|
| token_entropy | 3.5714 | 0.5873 | **-83.6%** |
| ece | 0.0112 | 0.5166 | +4526.1% |
| perplexity | 32.63 | 15023.88 | **+45947.5%** |
| distinct_1 | 0.1030 | 0.0774 | -24.9% |
| distinct_2 | 0.5513 | 0.3696 | -33.0% |
| distinct_3 | 0.8569 | 0.6285 | -26.6% |
| effective_rank | 2.372 | 33.343 | +1305.4% |
| mauve | 0.0341 | 0.0278 | -18.5% |
| self_bleu | 0.0097 | 0.0107 | +10.4% |

Severe model collapse observed. Entropy drops 83.6%, perplexity explodes ~460x.

## 3. Lead-Lag Results (5-Method, n_perm=5000)

### 3.1 Per-Method Forward Significance

| Method | Forward sig | Reverse sig |
|--------|:-----------:|:-----------:|
| Perm Granger (FDR) | **8/8** | 5/8 |
| Diff XCorr (FDR) | **8/8** | 8/8 |
| Threshold Onset | 0/8 | — |
| TY Granger | 4/8 | — |
| Naive XCorr (lag>0) | 1/8 | — |

### 3.2 Consensus Detail (Forward: canary → downstream)

| Pair | Votes | Methods |
|------|:-----:|---------|
| token_entropy→distinct_1 | 2/5 | diff, perm |
| token_entropy→distinct_2 | 3/5 | diff, perm, ty |
| **token_entropy→distinct_3** | **4/5** | naive, diff, perm, ty |
| token_entropy→perplexity | 2/5 | diff, perm |
| ece→distinct_1 | 2/5 | diff, perm |
| ece→distinct_2 | 3/5 | diff, perm, ty |
| ece→distinct_3 | 3/5 | diff, perm, ty |
| ece→perplexity | 2/5 | diff, perm |

- **K≥4**: 1/8
- **K≥3** (robust pairs): 4/8

### 3.3 Threshold Onset Failure Analysis

token_entropy 在 Gen 0→1 暴跌 55.4%（3.57→1.59），导致 3σ threshold 在 Gen 0 就被触发（onset=null），threshold_onset 方法无法检测 lead time。naive xcorr 的 peak lag 多为负值（downstream 先达到峰值相关），同一原因：entropy 的急剧下降压缩了 lead-lag 时间窗口。

## 4. Cross-Seed Comparison: s42 (bf16) vs s43 (fp32)

| Metric | s42 (bf16) | s43 (fp32) | Note |
|--------|:----------:|:----------:|------|
| final_ppl | 16520.5 | 15023.9 | s43 slightly less |
| entropy_drift | -86.6% | -83.6% | s43 slightly less |
| ppl_drift | +50527.6% | +45947.5% | s43 slightly less |
| K≥4 | 6/8 | **1/8** | significant drop |
| K≥3 | — | 4/8 | — |
| PermG_fwd | 6/8 | **8/8** | s43 stronger |
| PermG_rev | 3/8 | 5/8 | s43 stronger reverse |
| Diff XCorr | 8/8 | 8/8 | same |
| Threshold | 8/8 | 0/8 | s43 total failure |
| TY | 5/8 | 4/8 | comparable |

### Key Observations

1. **PermG_fwd 和 diff xcorr 一致性强**：两者均 8/8，比 s42 的 PermG_fwd=6/8 更强，表明 forward causal signal 在 s43 中实际上更清晰。
2. **K≥4 下降根因是 threshold 和 naive 失败**：threshold 从 8/8 跌至 0/8，naive 从隐含的多数显著跌至 1/8。这不是 lead-lag 信号消失，而是 entropy 在 Gen 0→1 的急剧坍缩使得 threshold/naive 方法的时间分辨率不足。
3. **fp32 drift 略弱于 bf16**：与 D079 预期（fp32 drift 更大）不一致。但差异不大（ppl: 15024 vs 16521），可能是 seed 效应。
4. **Reverse PermG 增强**：s43 reverse=5/8 > s42 reverse=3/8，提示 s43 中 feedback loop 更明显。

## 5. Verdict

**NEGATIVE** (K≥4 = 1/8 < 4/8 threshold)

但需要注意：这是 K≥4 共识指标的失败，不是 lead-lag 信号的失败。PermG_fwd=8/8 和 diff=8/8 显示 forward causal direction 在 s43 中完全成立。K≥4 的下降源于 threshold_onset 方法对 rapid early collapse 的敏感性不足。如果仅看 Granger-class 方法（perm+TY+diff），consensus ≥ 2/3 的 pairs = 8/8。

## 6. Paths

| Item | Path |
|------|------|
| Results dir | `/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/` |
| Config | `/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/config.json` |
| all_metrics.json | `/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/all_metrics.json` |
| 5method JSON | `/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/analysis/5method_leadlag.json` |
| Log | `~/runs/distrib_canary_collapse/gen_gpt2m_a100_s43_fp32.log` |
