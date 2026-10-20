# analysis scp and cka full dose response

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scp_and_cka_full_dose_response_20260525T072609_result.json`
- **Structured JSON:** [`b73c60aefed0ff0e60d1.json`](../../sessions/b7/b73c60aefed0ff0e60d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 1 结果：s0 cutoff checkpoints 全部不存在

在两台服务器上做了全面搜索：

| Checkpoint | westd-34685 | westd-10894 |
|---|---|---|
| cutoff_15k_s0 | ❌ 已删除 | ❌ |
| cutoff_25k_s0 | ❌ 已删除 | ❌ |
| cutoff_s0 (35K) | ❌ 已删除 | ❌ |
| cutoff_45k_s0 | ❌ 已删除 | ❌ |
| reverse_cutoff_s0 | ❌ 已删除 | ❌ |

这些实验的 CAR 评估数据保留在 memory 中（训练和 eval 确实完成过），但 checkpoint 文件在后续磁盘清理中被删除了。34685 上的 v3 训练（cutoff_25k_s2_v3, reverse_cutoff_s2_v3 等）目前只有 `dataset_statistics.json`，尚未产生 50K checkpoint。

**可用于 CKA 分析的条件（全部已在 10894 上）：**

| Condition | Seed | LoRA adapter |
|---|---|---|
| Vanilla s0 | 42 | ✅ |
| Full OCC s0 | 42 | ✅ |
| Detach+BN s0 | 42 | ✅ |
| Full OCC LN s0 | 42 | ✅ |
| Cutoff 15K s1 | 43 | ✅ |

7-point cutoff dose-response 无法完成。但我可以用这 5 个条件运行综合 CKA 分析——包含唯一可用的 cutoff 数据点（15K s1），与基线条件对比。这已足够展示"梯度撤除效应"（Cutoff 15K DINOv2 CKA=0.520 vs Vanilla 0.968）。

是否继续用这 5 个条件运行？还是需要先重训 s0 cutoff 实验？

---
