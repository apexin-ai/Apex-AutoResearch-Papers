# code bootstrap ci delta r2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_ci_delta_r2_20260524T203754_result.json`
- **Structured JSON:** [`e521fb3d3e08f0f6b35c.json`](../../sessions/e5/e521fb3d3e08f0f6b35c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

Bootstrap CI 分析完成。利用已有的 bootstrap_v3 MCCV 结果（1000 iterations, demo-level resampling）聚合了 10 个 cell 的 ΔR²。

### Gap 显著性检验

**Strict test fails**: 存在微小 CI 重叠。
- VLA→VLA max CI_upper = **0.1064** (openvla_goal)
- VLM→VLA min CI_lower = **0.0906** (tracvla_spatial)  
- Gap = **-0.016** (overlap)

### 关键发现

| Category | Cell | ΔR² | 95% CI |
|----------|------|-----|--------|
| VLA→VLA | openvla_long | 0.033 | [0.004, 0.103] |
| VLA→VLA | openvla_object | 0.037 | [-0.004, 0.085] |
| VLA→VLA | openvla_spatial | 0.037 | [0.009, 0.102] |
| VLA→VLA | openvla_goal | 0.086 | [-0.056, 0.106] |
| VLM→VLA | tracvla_spatial | 0.156 | [0.091, 0.224] |
| VLM→VLA | nora_spatial | 0.308 | [0.301, 0.512] |
| VLM→VLA | tracvla_goal | 0.333 | [0.207, 0.451] |
| VLM→VLA | tracvla_long | 0.358 | [0.171, 0.533] |
| VLM→VLA | tracvla_object | 0.362 | [0.283, 0.504] |

重叠仅由 **tracvla_spatial**（VLM→VLA 中 ΔR² 最低的 cell）和 **openvla_goal**（VLA→VLA 中 CI 最宽的 cell）驱动，重叠量仅 0.016。其余 cell 之间 gap 清晰。NORA-Goal 因 exit layer R² 极不稳定（L35 R²≈-0.006）被标记排除。

结果保存于 `westd-19183:/root/autodl-tmp/vla-ssd/results/bootstrap_ci/bootstrap_ci_results.json`。

---
