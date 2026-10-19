# monitor fresh metrics all evals

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_fresh-metrics-all-evals_20260515T013810_result.json`
- **Structured JSON:** [`6427cc80ea7eef6f502e.json`](../../sessions/64/6427cc80ea7eef6f502e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。Summary：

---

## bjb1-18228 三个 RUNNING eval 状态

| 实验 | 进度 | Running Avg | ETA |
|------|------|-------------|-----|
| **eval-argmin-only-spatial** (cuda:1) | **7/10 tasks** | **42.86%** | ~3h |
| **eval-acr-spatial-v4-small** (cuda:3) | **4.5/10 tasks** | **52.5%** | ~6.3h |
| **eval-acr-spatial-v4-obs-only-r2** (cuda:0) | **3.5/10 tasks** | **63.33%** | ~6.1h |

### 各任务明细

**argmin-only-spatial** (reconvla, no CRM):
| Task | Success |
|------|---------|
| between_plate_and_ramekin | 60% |
| next_to_ramekin | **100%** |
| from_table_center | 0% |
| on_cookie_box | 30% |
| in_top_drawer | 10% |
| on_ramekin | 10% |
| next_to_cookie_box | **90%** |

**acr-spatial-v4-small** (perdof CRM, norm=0.1):
| Task | Success |
|------|---------|
| between_plate_and_ramekin | 60% |
| next_to_ramekin | **100%** |
| from_table_center | 10% |
| on_cookie_box | 40% |
| in_top_drawer | ⏳ rollout 5/10 |

**acr-spatial-v4-obs-only-r2** (obs_only CRM, norm=0.1):
| Task | Success |
|------|---------|
| between_plate_and_ramekin | **90%** |
| next_to_ramekin | **100%** |
| from_table_center | 0% |
| on_cookie_box | ⏳ rollout 5/10 (1/5) |

### 额外发现

- **cuda:2 不空闲** — 占用两个进程:
  - PID 232820 (运行 7h50m): `eval acr_vla` 用 crm_v2/perdof, norm=0.05（老实验）
  - PID 288939 (运行 4m22s): `eval crm_scalar` 用 crm_v3_norm/scalar_unc, norm=0.1（**刚启动的新实验**）
- **bjb2-40593 eval-vla-mean-spatial-t10**: log 文件不存在，GPU 完全空闲 (0%, 0 MiB)。确认 failed/未执行。

### 初步观察

obs-only-r2 前 3 个 task 均值 63.33% 显著高于 argmin-only 的 42.86%，尤其 between_plate_and_ramekin 任务 obs-only 达到 90% vs argmin-only 60%。v4-small (perdof) 居中 52.5%。不过 task 3 (from_table_center) 对所有方法都是 0-10%，是个普遍难 task。

---
