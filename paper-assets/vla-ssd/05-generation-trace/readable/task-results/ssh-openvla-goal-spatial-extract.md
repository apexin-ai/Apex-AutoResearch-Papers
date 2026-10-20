# ssh openvla goal spatial extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_openvla_goal_spatial_extract_20260522T001622_result.json`
- **Structured JSON:** [`1c9ae7209bce999549bc.json`](../../sessions/1c/1c9ae7209bce999549bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取并写入 `artifacts/openvla_goal_spatial_data.md`。

关键发现：

**数据缺失项：**
- OpenVLA Goal **无 R² probing 数据**（`trained/action_prediction/` 实际是 LIBERO-Long，不是 Goal）
- OpenVLA Spatial **无 L1 attention 数据**（`attention/` 目录下的数据是 Goal 任务）
- NORA Spatial untrained **CF 缺失**（目录下无 `counterfactual_combined.json`）

**可用数据摘要：**

| | OpenVLA Goal | OpenVLA Spatial |
|--|--|--|
| R² peak | **缺失** | 0.696 (trained L13) / 0.673 (untrained L0) |
| L1 heads | 24/32 trained, 0/32 untrained | **缺失** |
| Cross-inst | 1.0 trained (L8+), 0.82 untrained (L31) | 1.0 trained (L4+), 0.754 untrained (L31) |
| CF top d | 0.978 empty (token), 3.85 (traj) | 0.942 empty (token) |

---
