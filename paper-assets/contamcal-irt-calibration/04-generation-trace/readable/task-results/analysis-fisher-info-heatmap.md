# analysis fisher info heatmap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fisher_info_heatmap_20260516T174835_result.json`
- **Structured JSON:** [`07941b57dec367feaeab.json`](../../sessions/07/07941b57dec367feaeab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图已生成并注册。

**输出文件（服务器 cqa1-21977）：**
- `/root/autodl-tmp/exp006/figures/fisher_info_heatmap.pdf` / `.png`
- `/root/autodl-tmp/exp006/figures/ci_width_scaling.pdf` / `.png`
- 生成脚本：`/root/contamcal-irt-calibration/exp004_sim_sweep/plot_fisher_heatmap.py`

**关键结果：**

| | N=8 | N=20 | N=50 | N=100 |
|---|---|---|---|---|
| AUC=0.55 | 0.197 | 0.133 | 0.087 | 0.065 |
| AUC=0.65 | 0.228 | 0.156 | 0.102 | 0.076 |
| AUC=0.80 | 0.416 | 0.258 | 0.163 | 0.116 |
| AUC=0.90 | 0.540 | 0.330 | 0.206 | 0.148 |

**Scaling exponent:** 全局 α = **-0.482**（接近理论 √N 率 -0.5），per-AUC 范围 [-0.44, -0.51]。高 AUC（harder discrimination）的 CI 更宽但 scaling 更陡，低 AUC 下 CI 已很窄。支持 Claim 3。

---
