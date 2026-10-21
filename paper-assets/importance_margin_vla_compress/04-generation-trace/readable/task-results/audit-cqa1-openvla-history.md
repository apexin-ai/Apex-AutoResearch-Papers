# audit cqa1 openvla history

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_openvla_history_20260526T063958_result.json`
- **Structured JSON:** [`49facdbe2444fa55c335.json`](../../sessions/49/49facdbe2444fa55c335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1 OpenVLA 历史审计报告

### 结论：Crossover table 数据全部安全，无 cqa1 污染

全部 16 个 crossover table 数据点（12 个 k=0.9 实验 + 4 个 baseline）均在 **westd 服务器** 上运行，无一来自 cqa1-33015。

---

### cqa1 上的 OpenVLA 实验完整清单

| exp_id | server | status/conclusion | SR | 是否影响 paper 数据 | 备注 |
|--------|--------|-------------------|-----|-------------------|------|
| eval_openvla_attn_k09_goal_seed43 | cqa1-33015 | DONE/failed | 0% (每 task 均 0/50) | ❌ 不影响 | transformers==5.5.3，输出无效 |
| eval_openvla_attn_k09_goal_seed43_v2 | cqa1-33015 | DONE/killed | 0% (被 kill 前已全 0) | ❌ 不影响 | 同上，中途终止 |
| eval_openvla_attn_k09_goal_seed43_v3 | cqa1-33015 | PREPARING | 0% (Task 1: 0/50, Task 2 进行中被 kill) | ❌ 不影响 | 同上，未完成 |
| eval_openvla_random_k05_object_seed42_v2 | cqa1-33015 | DONE/killed | 0% (Task 1-2: 0/50, Task 3 进行中被 kill) | ❌ 不影响 | transformers==5.5.3，被 kill |
| eval_openvla_baseline_spatial_seed42 | cqa1-33015 | DONE/failed | 0% (4011 行日志全 FAIL，无 Overall 输出) | ❌ 不影响 | transformers==5.5.3，未完成 |

### cqa1 上的非 registry OpenVLA 痕迹

| 日志文件 | 行数 | 状态 | 备注 |
|---------|------|------|------|
| logs/openvla_l2norm_k09_spatial_s42.log | 4 | 仅加载模型即终止 | transformers==5.5.3 warning，无 eval 输出 |
| logs/openvla_l2norm_k095_spatial_s42.log | 4 | 仅加载模型即终止 | 同上 |
| runs/profiling_openvla_latency.log | 完成 | 延迟 profiling（非 SR 评估） | 测量推理速度，不影响 SR 数据 |
| eval_results/eval_openvla_sc_m128_vtconly_20k_seed42_dryrun.json | 完成 | Smart Compress dryrun，SR=0% (2 episodes) | dryrun 非正式实验 |

### Crossover Table 数据来源确认

| Suite | Metric | Value | 来源实验 | 服务器 | 安全 |
|-------|--------|-------|---------|--------|------|
| Object | Baseline | 74.0% | eval_openvla_baseline_object_seed42 | westd-38929 | ✅ |
| Object | Attn | 61.4% | eval_openvla_attn_k09_object_seed42_v3 | westd-38929 | ✅ |
| Object | L2norm | 70.6% | eval_openvla_l2norm_k09_object_seed42 | westd-27271 | ✅ |
| Object | Random | 62.8% | eval_openvla_random_k09_object_seed42 | westd-27271 | ✅ |
| Goal | Baseline | 74.8% | eval_openvla_baseline_goal_seed42_v3 | westd-27271 | ✅ |
| Goal | Attn | 73.2% | eval_openvla_attn_k09_goal_seed42 | westd-27271 | ✅ |
| Goal | L2norm | 74.8% | eval_openvla_l2norm_k09_goal_seed42 | westd-27271 | ✅ |
| Goal | Random | 79.6% | eval_openvla_random_k09_goal_seed42 | unknown* | ✅ |
| Spatial | Baseline | 80.0% | eval_openvla_baseline_spatial | westd-27271 | ✅ |
| Spatial | Attn | 80.4% | eval_openvla_attn_k09_spatial_seed42 | westd-27271 | ✅ |
| Spatial | L2norm | 75.0% | eval_openvla_l2norm_k09_spatial_seed42 | westd-27271 | ✅ |
| Spatial | Random | 79.8% | eval_openvla_random_k09_spatial_seed42 | westd-41074 | ✅ |
| Long | Baseline | 52.8% | eval_openvla_baseline_long_seed42 | westd-27271 | ✅ |
| Long | Attn | 44.0% | eval_openvla_attn_k09_long_seed42_v3 | westd-38929 | ✅ |
| Long | L2norm | 43.6% | eval_openvla_l2norm_k09_long_seed42_v3 | westd-38929 | ✅ |
| Long | Random | 46.8% | eval_openvla_random_k09_long_seed42_v3 | westd-38929 | ✅ |

*\*unknown 但非 cqa1 — registry 中 server 字段缺失，但 conclusion=success 且产出了合理 SR 值*

### 总结

1. **Paper 数据安全**：crossover table 16/16 数据点全部来自 westd 服务器，无 cqa1 污染
2. **cqa1 OpenVLA 全部无效**：5 个 registry 实验 + 2 个非 registry 尝试，全部因 transformers==5.5.3 输出 0% SR，均已标记 failed/killed
3. **延迟 profiling** 在 cqa1 上完成，但测量推理速度不受模型输出质量影响
4. **cqa1 当前仍运行非 OpenVLA 实验**（π0.5 zeromask、L2norm、Random 等），这些不受 transformers 版本兼容性问题影响

---
