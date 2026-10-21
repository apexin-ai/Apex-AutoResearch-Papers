# analysis theta sensitivity arxiv

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta_sensitivity_arxiv_20260520T035135_result.json`
- **Structured JSON:** [`4336d0c9ec528e55ff90.json`](../../sessions/43/4336d0c9ec528e55ff90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## θ 敏感性分析结果

### DeBERTa vs OBD 对比表（arXiv, Qwen-1.5B）

| θ | DeBERTa K* | OBD K* | ΔK* | DeBERTa pivotal (margin) | OBD pivotal (margin) |
|-------|------------|--------|-----|--------------------------|----------------------|
| 0.55 | **5** | 3 | +2 | 4v5 (+0.016) | 2v3 (+0.074) |
| 0.60 | **4** | 3 | +1 | 3v4 (+0.013) | 2v3 (+0.024) |
| 0.625 | **3** | 2 | +1 | 2v3 (+0.108) | 1v2 (+0.223) |
| 0.65 | **3** | 2 | +1 | 2v3 (+0.083) | 1v2 (+0.198) |
| 0.70 | **3** | 2 | +1 | 2v3 (+0.033) | 1v2 (+0.148) |

### 关键发现

1. **DeBERTa K\* 在 θ=0.60→0.625 时从 4 降到 3**。3v4 pair 的 CI_lower=0.6127，刚好高于 0.60（margin 仅 +0.013），但低于 0.625。这是 borderline 转折点。

2. **OBD 在所有 θ 下始终比 DeBERTa 低 1-2 级**。OBD K\*=3（θ≤0.60）和 K\*=2（θ≥0.625），说明 DeBERTa 的深层区分能力显著强于 OBD。

3. **θ=0.625 是两个方法的共同断崖点**：DeBERTa 从 4→3，OBD 从 3→2。但 DeBERTa 在 θ=0.625 时 margin 大（+0.108），而 OBD 在 θ=0.60 时 margin 已经很薄（+0.024），说明 DeBERTa 的 K\*=3 判定远比 OBD 的 K\*=3 稳健。

4. **θ=0.55 时 DeBERTa 可达 K\*=5**，但 4v5 margin 极薄（+0.016），实际意义有限。

JSON 已保存至两个路径：
- `/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_arxiv/theta_sensitivity.json`
- `/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_arxiv_qwen1b5/theta_sensitivity.json`

---
