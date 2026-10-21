# diag bjb2 servers urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-servers-urgent_20260526T055700_result.json`
- **Structured JSON:** [`52bf2c86c30d77f5e557.json`](../../sessions/52/52bf2c86c30d77f5e557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 服务器 1: bjb2-28827（6×24GB GPU）

**Registry 数据滞后，不是部署失败。** 6 个实验已正常运行：

| GPU | exp_id | 进程年龄 | 显存 | 状态 |
|-----|--------|---------|------|------|
| 0 | pi05-crm-k2-spatial-s42-bjb2 | 2:56 | 14.7GB | 已加载 CRM，正在加载 LIBERO env |
| 1 | pi05-crm-k2-spatial-s43-bjb2 | 2:56 | 14.7GB | 同上 |
| 2 | pi05-crm-k2-spatial-s44-bjb2 | 2:56 | 14.7GB | 同上 |
| 3 | pi05-adaptive-spatial-s42-bjb2 | 1:51 | 3MB | 正在加载 π0.5 模型 |
| 4 | pi05-adaptive-spatial-s43-bjb2 | 1:51 | 3MB | 同上 |
| 5 | pi05-adaptive-spatial-s44-bjb2 | 1:51 | 3MB | 同上 |

依赖就绪：`crm_pi05_unified_3suite/crm_best.pt` 在使用中。已转 RUNNING + spec。

### 服务器 2: bjb2-24035（1×24GB）

`westd-pi05-adaptive-object-s43` 仍在跑（已 1:39:52）：
- 任务 1 `alphabet_soup`: 19/20 (95.0%)
- 任务 2 `cream_cheese`: 15/20 (75.0%)
- 任务 3 `salad_dressing`: 10/10（进行中）
- 继续运行，无需干预。

### 已 Harvest 的 SmolVLA paired 实验（全部已 DONE）

| exp_id | SR | 配对差 | conclusion |
|--------|-----|--------|------------|
| eval-spatial-vla-only-s46-paired | 0.800 | — | success |
| eval-spatial-adapt-tau025-s46-paired | 0.780 | -2.0pp | negative |
| eval-spatial-vla-only-s48-paired | 0.775 | — | success |
| eval-spatial-adapt-tau025-s48-paired | 0.810 | +3.5pp | success |
| eval-goal-vla-only-s49-paired | 0.835 | — | success |
| eval-goal-adapt-tau025-s49-paired | 0.805 | -3.0pp | negative |

Spatial 3-seed paired 配对差：{s46: -2.0pp, s48: +3.5pp}，需 s47 补齐才能定结论。Goal s49 单独看负向。

### 缺失依赖
无。π0.5 CRM checkpoint + 模型在两台服务器上均已就绪。

### 未新部署任何实验
所有 6 个 GPU 已占满，无需重新部署。

---
