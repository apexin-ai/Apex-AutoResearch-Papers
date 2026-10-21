# analysis mf4 analyzing

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mf4-analyzing_20260522T175428_result.json`
- **Structured JSON:** [`117f0ee7090bf3520fe1.json`](../../sessions/11/117f0ee7090bf3520fe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已更新为 DONE。以下是三 seed 汇总：

## FewNERD MF4 三 Seed 汇总 (N=8, T=1.0, n=32565)

| Metric | seed=42 | seed=123 | seed=456 | **Mean ± Std** |
|---|---|---|---|---|
| greedy_f1 | 0.7911 | 0.7909 | 0.7909 | **0.7910 ± 0.0001** |
| mv_strict_f1 | 0.7585 | 0.7648 | 0.7685 | **0.7639 ± 0.0051** |
| mv_delta_pp | −3.27 | −2.61 | −2.24 | **−2.71 ± 0.52** |
| lp_f1 | 0.7918 | 0.7918 | 0.7921 | **0.7919 ± 0.0002** |
| lp_delta_pp | +0.07 | +0.09 | +0.12 | **+0.09 ± 0.03** |
| degeneracy_rate | 0.091 | 0.093 | 0.081 | **0.088 ± 0.006** |
| oracle_f1 | 0.8787 | 0.8892 | 0.8810 | **0.8830 ± 0.0055** |
| oracle_headroom_pp | 8.76 | 9.83 | 9.01 | **9.20 ± 0.56** |
| fleiss_kappa | 0.3537 | 0.3503 | 0.3555 | **0.3532 ± 0.0026** |
| soft_jaccard | 0.6751 | 0.6701 | 0.6845 | **0.6766 ± 0.0073** |

**关键结论：**
- **Greedy F1 极其稳定**：0.7910 ± 0.0001，三 seed 几乎无差异
- **MV 一致性地 hurt**：−2.71 ± 0.52 pp，方差主要来自 MV，但方向一致（全部为负）
- **LP 微弱正 delta**：+0.09 ± 0.03 pp，统计上接近零但方向一致（全部为正）
- **退化率稳定**：~8.8%，模型在 ~1/11 的实例上 8 次采样产生完全相同的输出
- **Oracle headroom 充足**：~9.2 pp，说明样本中蕴含的多样性信息远未被 MV/LP 充分利用

---
