# analysis eval pi05 baseline spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_baseline_spatial_seed42_20260521T200919_result.json`
- **Structured JSON:** [`62dc1b4b428485737dfc.json`](../../sessions/62/62dc1b4b428485737dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果：eval_pi05_baseline_spatial_seed42

**总 Success Rate: 97.2% (486/500)** | 运行时间: 55.8 min

### Per-task 分解

| Task | Description | SR | Success/Total |
|------|-------------|-----|---------------|
| T0 | pick up black bowl between the plate | **100%** | 50/50 |
| T1 | pick up black bowl next to the ramekin | **100%** | 50/50 |
| T2 | pick up black bowl from stove | **100%** | 50/50 |
| T3 | pick up black bowl on the cookie box | **100%** | 50/50 |
| T4 | pick up black bowl in the top drawer | **98%** | 49/50 |
| T5 | pick up black bowl on the ramekin | **78%** | 39/50 |
| T6 | pick up black bowl next to the cookie | **100%** | 50/50 |
| T7 | pick up black bowl on the stove | **98%** | 49/50 |
| T8 | pick up black bowl next to the plate | **98%** | 49/50 |
| T9 | pick up black bowl on wooden cabinet | **100%** | 50/50 |

### 关键观察

- **Spatial 97.2% vs Object 98.2%**：两个 suite 的 baseline 性能接近，Spatial 略低 1 个百分点
- **T5 是明显短板 (78%)**：ramekin 上的 bowl 抓取成功率显著低于其他 task，拉低了整体均值。去掉 T5 后其余 9 个 task 平均 99.3%
- **无错误/无警告**：运行干净完成，EXIT_CODE=0

---
