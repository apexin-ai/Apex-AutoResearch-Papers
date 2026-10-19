# audit bjb2 28827 cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-cleanup_20260519T120344_result.json`
- **Structured JSON:** [`7ac94141cd1619333c0c.json`](../../sessions/7a/7ac94141cd1619333c0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计报告：bjb2-40593 (原 bjb2-28827)

**重要说明**：项目配置绑定的是 **bjb2-40593**（单 GPU 机器），与任务描述的多 GPU 机器 bjb2-28827 不一致。任务中提到的 GPU 0/2/4/5 分配在当前服务器上不存在。以下是当前服务器的实际状态。

---

### 任务中指定的 5 个实验 — 全部不存在

| 实验 | 状态 |
|------|------|
| reconvla K=5 seed42 (原 GPU 4) | **进程不存在，无输出文件** |
| perdof norm005 seed45 (原 GPU 0) | **进程不存在，无输出文件** |
| obs_only norm003 seed44 (原 GPU 2) | **进程不存在，无输出文件** |
| random_selection seed46 (原 GPU 2) | 见下方（不同配置在跑） |
| perdof norm03 seed43 (原 GPU 5) | **进程不存在，无输出文件** |

---

### 当前服务器实际运行中的 2 个进程（共享 GPU 0）

**1. random_selection seed46 (object benchmark)**
- tmux: `eval-random-selection-seed46-t16`，PID 503784，启动 09:38
- 进度：**4/10 tasks 完成**（~10h 运行中）
- 已完成 tasks：
  - alphabet_soup: 0/10, cream_cheese: 0/10, salad_dressing: 2/10, bbq_sauce: 2/10

**2. crm_obs_only spatial norm02 seed43（顺序跑 seed43→44→45）**
- tmux: `eval-spatial-obs-only-norm02-seq`，PID 508930，启动 09:44
- 进度：**5/10 tasks 完成**（seed43 第一轮，~10h 运行中）
- 已完成 tasks：
  - between_plate_and_ramekin: 8/10, next_to_ramekin: 10/10, table_center: 1/10, cookie_box: 3/10, top_drawer: 0/10

---

### 已完成的实验结果（服务器上现存 JSON）

| 文件 | mode | benchmark | SR |
|------|------|-----------|----|
| eval_object_scalar_seed45_r2.json | crm_scalar | object | **0.07** |
| eval_object_random_selection_seed42.json | random_selection | object | **0.13** |
| eval_object_obs_only.json | crm_obs_only | object | **0.19** |
| eval_object_vla_only_seed44.json | vla_only | object | **0.10** |
| eval_mag_obsonly_norm003.json | crm_obs_only | spatial | **0.34** |

---

### 结论

任务描述中 5 个实验的进程和输出文件在当前服务器上均不存在。可能原因：
1. bjb2-28827 是之前的实例，已被 bjb2-40593 替换，数据未迁移
2. 这些实验在不同服务器上运行

需要确认 bjb2-28827 是否仍然可达，还是已经被释放。

---
