# ops diagnose openvla l2norm k07 westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-openvla-l2norm-k07-westd38929_20260521T115011_result.json`
- **Structured JSON:** [`296cabbe0e69fe33f956.json`](../../sessions/29/296cabbe0e69fe33f956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。

## 诊断结果

### eval_openvla_l2norm_k07_object_seed42_v2 → **SUCCESS**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **49.8%** (249/500) |
| Vision tokens | 256 → 179 (k=0.7, 剪 30%) |
| 耗时 | 262.4 min |

**Per-task SR:**

| Task | SR |
|------|-----|
| ketchup | 0.76 |
| orange juice | 0.68 |
| tomato sauce | 0.62 |
| milk | 0.56 |
| salad dressing | 0.54 |
| chocolate pudding | 0.46 |
| alphabet soup | 0.42 |
| bbq sauce | 0.38 |
| cream cheese | 0.28 |
| butter | 0.28 |

结果文件：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k07_object.json`

### 其他 3 个实验状态（westd-38929）

全部存活，运行约 4.5 小时：

| GPU | PID | 实验 | CPU% | GPU Mem | 状态 |
|-----|-----|------|------|---------|------|
| 1 | 2478 | random k=0.3 | 740% | 16091 MiB | **运行中** |
| 2 | 3110 | random k=0.7 | 724% | 15961 MiB | **运行中** |
| 3 | 3825 | l2norm k=0.5 v2/v3 | 729% | 15961 MiB | **运行中** |

Cron 列表为空（本 session 无需清理）。

---
