# analysis exp 026 T ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_026_T_ablation_20260517T094952_result.json`
- **Structured JSON:** [`4efff8f20b9db68e5f87.json`](../../sessions/4e/4efff8f20b9db68e5f87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析汇总已写入 `artifacts/exp_026_T_ablation/analysis_summary.md`。

核心结论：

1. **Agreement-Temperature 单调性确认**：Fleiss κ 和 Soft Jaccard 均随 T 单调递减，4 个温度点无例外。这是干净的可发表结果。

2. **T=0.8 是结构一致性信号的最优点**：rho(SJ, F1) 在 T=0.8 达到峰值（NER 0.384, RE 0.273），高于 T=1.0 baseline（NER 0.360, RE 0.250）。太低的 T 压缩了 SJ 分布（天花板效应），太高的 T 引入噪声。

3. **三个 hypothesis 验证结果**：
   - T=0.5: **CONFIRMED** — 高 agreement、低 oracle headroom、SJ 信号最弱
   - T=0.8: **PARTIALLY CONFIRMED** — agreement 单调，但意外发现 SJ 信号峰值
   - T=1.2: **CONFIRMED** — 最高 diversity/headroom，但 sample 质量最差（RE 47% zero-F1），且 RE 上 structural > surface 关系被打破

4. **论文影响**：如果论文声称 T=1.0 是默认最优，需要 nuance——T=0.8 的信号质量更强。建议将 ablation table 同时展示 agreement + oracle headroom + rho(SJ, F1) + sample F1，叙述为"sweet spot"而非单调关系。

5. **缺失指标**：degeneracy rate（精确重复率）、LP range/std、LP selection F1 在当前 evaluation pipeline 中未计算，已在文件中标注 N/A。

---
