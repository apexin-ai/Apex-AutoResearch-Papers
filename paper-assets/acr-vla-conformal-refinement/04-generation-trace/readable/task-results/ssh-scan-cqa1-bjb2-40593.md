# ssh scan cqa1 bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-cqa1-bjb2-40593_20260523T233806_result.json`
- **Structured JSON:** [`baf19c705fb189c58039.json`](../../sessions/ba/baf19c705fb189c58039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。所有实验状态汇总如下：

---

## cqa1-32758（6x A100 24GB）

| GPU | 实验 | Registry ID | 进度 | 状态 |
|-----|------|-------------|------|------|
| cuda:0 | Goal K2mean s45 | eval-supp-goal-k2mean-s45 | **7/10** tasks | Running |
| cuda:1 | Spatial VLA-only s45 | eval-supp-spatial-vla-only-s45 | **7/10** tasks | Running |
| cuda:2 | Object K2mean s45 | eval-supp-obj-k2mean-s45 | **3/10** tasks | Running（启动较晚） |
| cuda:3 | Spatial CRM s45 | eval-supp-spatial-crm-norm005-s45 | **7/10** tasks | Running |
| cuda:4 | **Spatial Adaptive s45** | eval-supp-spatial-adapt-tau025-s45-r3 | **6/10** tasks | Running (PID 502821) |
| cuda:5 | Spatial Reconvla s45 | eval-supp-spatial-reconvla-s45 | **7/10** tasks | Running |

## bjb2-40593（1x A100 24GB）

| GPU | 实验 | Registry ID | 进度 | 状态 |
|-----|------|-------------|------|------|
| cuda:0 | Spatial K2mean s45 | eval-supp-spatial-k2mean-s45 | **3/10** tasks | Running (PID 204339) |

---

**关键发现：**
- 6卡全满载，无空闲GPU可部署新实验
- cuda:0/1/3/5 已完成 7/10 tasks，预计 **2-3 小时内完成**
- cuda:4 Spatial Adaptive s45 at 6/10，预计 **3-4 小时内完成**
- cuda:2 和 bjb2:cuda:0 启动较晚（3/10），预计 **5-7 小时**
- 无已完成未收割的实验——之前的 JSON 结果都已注册 DONE
- 已为 Spatial Adaptive s45 创建 `eval-supp-spatial-adapt-tau025-s45-r3` registry 条目并设为 RUNNING

**下一步时机：** cuda:0/1/3/5 的实验最先完成，建议 2-3 小时后再扫描收割并部署 s46 实验。

---
