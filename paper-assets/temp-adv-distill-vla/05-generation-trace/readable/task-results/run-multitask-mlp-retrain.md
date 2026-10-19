# run multitask mlp retrain

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_multitask-mlp-retrain_20260515T065339_result.json`
- **Structured JSON:** [`dabb499188151e7d3b27.json`](../../sessions/da/dabb499188151e7d3b27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 多任务 MLP 重训结果

### VIP 特征提取
- 总任务数: 10
- 总轨迹数: 500
- 总 timestep 数: 74,507
- 提取时间: 0.4 分钟

### 多任务 MLP 训练
- 训练样本: 59,656
- Best epoch: 11 (early stop at 21)
- Overall R²: 0.9653

### Per-task Test R²
| Task | # Test Steps | R² | Status |
|------|-------------|-----|--------|
| alphabet_soup | 1266 | 0.9691 | PASS |
| bbq_sauce | 1216 | 0.9673 | PASS |
| butter | 1263 | 0.9836 | PASS |
| chocolate_pudding | 1265 | 0.9897 | PASS |
| cream_cheese | 1140 | 0.9769 | PASS |
| ketchup | 1304 | 0.9695 | PASS |
| milk | 1123 | 0.9796 | PASS |
| orange_juice | 1152 | 0.8546 | PASS |
| salad_dressing | 989 | 0.9825 | PASS |
| tomato_sauce | 1167 | 0.9776 | PASS |

### 判定: ALL PASSED (10/10 tasks R² > 0.7)

最低的 orange_juice 也有 0.8546，其余全在 0.96+。可以继续 Phase 1 IQL。

### 产出文件
| 文件 | 大小 | 位置 |
|------|------|------|
| VIP 特征 (10个 .pt) | 292MB | `artifacts/vip_features_all/` |
| MLP checkpoint | 2.3MB | `artifacts/gate1b_mlp_multitask.pt` |
| 结果 JSON | 1.5KB | `artifacts/multitask_mlp_results.json` |
| R² 条形图 | 82KB | `artifacts/multitask_mlp_per_task_r2.png` |

---
