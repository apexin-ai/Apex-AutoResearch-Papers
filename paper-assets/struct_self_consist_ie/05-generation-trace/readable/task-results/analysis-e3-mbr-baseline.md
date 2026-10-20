# analysis e3 mbr baseline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e3_mbr_baseline_20260521T113214_result.json`
- **Structured JSON:** [`8be7ccc7030884e8b430.json`](../../sessions/8b/8be7ccc7030884e8b430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MBR baseline 计算完成。结果汇总：

## E3 MBR Micro-F1 Results

**Micro-F1（3 个数据集 × 5 种方法）：**

| Dataset | Greedy | LP | MBR | MV | Oracle | MBR−Grd | MV−Grd |
|---------|--------|------|------|------|--------|---------|--------|
| SciERC (529) | .6663 | .6639 | .6657 | .6579 | .7795 | −0.06pp | −0.84pp |
| CoNLL (2756) | .9116 | .8968 | .9115 | .9132 | .9547 | −0.01pp | +0.15pp |
| FewNERD (32565) | .7916 | .7919 | .7840 | .7690 | .8856 | −0.76pp | −2.27pp |

**核心发现：**

1. **MBR 在所有 3 个数据集上都无法超越 greedy**（micro-F1），oracle gap closure 为 0 或负值（−0.5% / −0.1% / −8.1%）
2. **MV construction 同样失败**：仅 CoNLL 微弱正（+0.15pp），FewNERD 大幅负（−2.27pp）
3. **LP selection 是唯一在 FewNERD 上有正向信号的方法**（instance-avg +1.37pp），但 micro-F1 仅 +0.02pp
4. **Oracle gap 巨大**（4–11pp）→ 信息存在于 samples 中，但 MBR/MV/LP 均无法有效提取

**论文定位**：MBR 作为理论最优无监督选择方法，使用 pairwise entity F1 作为 utility，仍然不能 beat greedy。这从实验角度确认了 paper_framing 中的核心论断 — unsupervised selection 在 NER 上面临结构性瓶颈，不是 utility function 选错的问题。

数据源：SciERC (scierc_mf4v2_seed456), CoNLL (exp_002_conll_n16_r1024), FewNERD full (fewnerd_mf4v2_seed456, N=8)。脚本和 JSON 结果均已保存到服务器。

---
