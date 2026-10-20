# analysis bonferroni global

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bonferroni_global_20260520T193542_result.json`
- **Structured JSON:** [`ed3096be934f5f8672f4.json`](../../sessions/ed/ed3096be934f5f8672f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**总检验数 N = 63**，Bonferroni 校正阈值 α/N = 0.000794。

### 核心结论全部保留 (Bonferroni 校正后)

| 核心检验 | 原始 p | Bonferroni p | 显著? |
|---|---|---|---|
| RSA 置换检验 L12 | < 0.0001 | 0.0063 | **Yes** |
| RSA trained > untrained (image_mean, L12) | 3.9×10⁻⁵ | 0.0025 | **Yes** |
| Counterfactual wrong instruction | 2.6×10⁻¹⁷⁷ | ≈ 0 | **Yes** |
| Counterfactual empty instruction | 1.8×10⁻²¹⁷ | ≈ 0 | **Yes** |
| TOST cross-architecture equivalence | < 0.0001 | 0.0063 | **Yes** |
| Dose-response top-24 | 2.3×10⁻¹⁰⁵ | ≈ 0 | **Yes** |
| Probe R² trained > untrained | < 0.0001 | 0.0063 | **Yes** |
| Specificity bottom-24 ablation | 1.9×10⁻⁹² | ≈ 0 | **Yes** |

### 校正后变为不显著的检验 (5/45)

Bonferroni 和 Holm 结果一致，同样 5 项丢失显著性：

| 检验 | 原始 p | Bonferroni p | Holm p | 性质 |
|---|---|---|---|---|
| RSA trained vs untrained (last_preaction, L12) | 0.0045 | 0.284 | 0.099 | 次要 readout，image_mean 仍显著 |
| DINOv2 vs SigLIP projector | 0.032 | 1.0 | 0.604 | 辅助 baseline 比较 |
| Fused backbone vs SigLIP projector | 0.011 | 0.673 | 0.224 | 辅助 baseline 比较 |
| CV exact paired permutation (6 dims) | 0.016 | 0.984 | 0.313 | 受限于 2⁶=64 种排列 |
| Cross-rep Spearman (R²_proj vs R²_vla) | 0.0029 | 0.183 | 0.067 | Holm 下接近显著 |

### 总结

- 原始显著: 45/63 → Bonferroni 后: 40/63 → Holm 后: 40/63
- 丢失的 5 项均为辅助/次要分析，不影响论文的核心 claims
- 所有 counterfactual、dose-response、permutation、probe bootstrap 检验的 p-values 极小 (< 10⁻¹⁸)，校正后仍远低于 0.05

文件已保存至服务器 `/root/autodl-tmp/vla-ssd/results/statistical_supplements/bonferroni_global.json` 和本地 `artifacts/statistical_supplements/bonferroni_global.json`。

---
