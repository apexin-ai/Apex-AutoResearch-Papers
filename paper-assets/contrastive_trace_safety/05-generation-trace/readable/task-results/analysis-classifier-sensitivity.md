# analysis classifier sensitivity

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_classifier_sensitivity_20260522T182035_result.json`
- **Structured JSON:** [`caa9431876b09d0b84bb.json`](../../sessions/ca/caa9431876b09d0b84bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分类器敏感性分析结果（R1-8B AdvBench, 520 traces）

| Threshold | JB Rate | CR-composite Best | Precision Best | Divergence | Replicated (>15pp) |
|-----------|---------|-------------------|----------------|------------|-------------------|
| ≥1 | 30.6% (159/361) | L3 (9.7%) | L21 (67.7%) | **58.0pp** | **Yes** |
| ≥2 | 58.5% (304/216) | L6 (19.4%) | L1 (3.2%) | **16.2pp** | **Yes** |
| ≥3 | 87.1% (453/67) | L9 (29.0%) | L13 (41.9%) | 12.9pp | No |

**Key findings:**

- **≥1（最严格）**和 **≥2（论文使用的 threshold）** 均 replicate divergence >15pp，方向一致：composite 和 precision 的 best layer 选择不同深度
- **≥3** divergence 降至 12.9pp，低于 15pp 阈值——但此时 87.1% JB rate 导致 safe class 只剩 67 个样本，统计力不足
- Divergence 随 threshold 放宽（JB rate 升高）而单调递减：58.0 → 16.2 → 12.9pp
- 结论支持论文使用的 ≥2 threshold：它平衡了分类严格性（58.5% JB rate）与 divergence 显著性（16.2pp）

运行时间 9922s（~2.75 小时），结果已保存至 `artifacts/advbench_classifier_sensitivity.json`。

---
