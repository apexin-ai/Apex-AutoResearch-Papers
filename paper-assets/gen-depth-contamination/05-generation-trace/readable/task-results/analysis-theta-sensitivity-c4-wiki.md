# analysis theta sensitivity c4 wiki

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta_sensitivity_c4_wiki_20260520T035548_result.json`
- **Structured JSON:** [`473f5e5809e60a44cea3.json`](../../sessions/47/473f5e5809e60a44cea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已生成。汇总如下：

### C4 DeBERTa vs OBD (Qwen-1.5B)

| θ | DeBERTa K* | OBD K* | ΔK* | DeBERTa pivotal (margin) | OBD pivotal (margin) |
|---|-----------|--------|-----|--------------------------|----------------------|
| 0.55 | 4 | 3 | +1 | 3v4 (+0.0113) | 2v3 (+0.0041) |
| 0.60 | 2 | 2 | 0 | 1v2 (+0.1120) | 1v2 (+0.0210) |
| 0.625 | 2 | 1 | +1 | 1v2 (+0.0870) | 0v1 (+0.3651) |
| 0.65 | 2 | 1 | +1 | 1v2 (+0.0620) | 0v1 (+0.3401) |
| 0.70 | 2 | 1 | +1 | 1v2 (+0.0120) | 0v1 (+0.2901) |

### Wiki DeBERTa vs OBD (Pythia)

| θ | DeBERTa K* | OBD K* | ΔK* | DeBERTa pivotal (margin) | OBD pivotal (margin) |
|---|-----------|--------|-----|--------------------------|----------------------|
| 0.55 | 4 | 2 | +2 | 3v4 (+0.0159) | 1v2 (+0.0636) |
| 0.60 | 3 | 2 | +1 | 2v3 (+0.0059) | 1v2 (+0.0136) |
| 0.625 | 2 | 1 | +1 | 1v2 (+0.0920) | 0v1 (+0.3707) |
| 0.65 | 2 | 1 | +1 | 1v2 (+0.0670) | 0v1 (+0.3457) |
| 0.70 | 2 | 1 | +1 | 1v2 (+0.0170) | 0v1 (+0.2957) |

**输出文件：**
- C4: `results/exp_deberta_c4_1b5/theta_sensitivity.json`
- Wiki: `results/exp_deberta_upperbound/theta_sensitivity_wiki_pythia.json`

**要点：**
- C4/Wiki 的 DeBERTa 在所有 θ 下都比 OBD 多检测 1-2 层深度
- C4 DeBERTa K* 在 θ 从 0.55→0.60 时从 4 跳降到 2（2v3 ci_lower=0.587 是卡点）
- Wiki DeBERTa K* 在 θ=0.60 时还能维持 3（2v3 ci_lower=0.6059，margin 仅 0.0059，非常 borderline）
- OBD 在两个域中 θ≥0.625 时都退化到 K*=1（只能分辨 depth-0 vs depth-1）
- OBD CI 由 5-fold per-fold AUC bootstrap 估计（10000 次重采样）

---
