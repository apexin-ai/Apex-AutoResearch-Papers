# harvest bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546_20260524T032326_result.json`
- **Structured JSON:** [`b51cbaa02a323945012d.json`](../../sessions/b5/b51cbaa02a323945012d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 更新完成。汇总报告如下：

---

## 汇总报告

### GPU 状态 (bjb1-32546)

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 22% | 6289/24564 MiB | 运行中 |
| 1 | 33% | 9012/24564 MiB | 运行中 |
| 2 | 46% | 8360/24564 MiB | 运行中 |
| 3 | 24% | 5844/24564 MiB | 运行中 |
| 4 | 0% | 2/24564 MiB | 空闲 |
| 5 | 0% | 2/24564 MiB | 空闲 |

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 10G | 21G | 34% |
| /root/autodl-tmp | 250G | 68G | 183G | 28% |

### 收割的 JSON 结果

| 文件名 | success_rate | exp_id | Registry 操作 |
|--------|-------------|--------|---------------|
| eval_spatial_k2mean_seed46.json | **0.80** | eval-supp-spatial-k2mean-s46 | metrics 更新 (原 conclusion=failed→已是 success，补 metrics) |
| eval_object_reconvla_seed45.json | **0.78** | eval-supp-reconvla-obj-s45 | metrics 更新 + conclusion failed→**success** |
| eval_long_reconvla_seed45.json | **0.59** | eval-supp-long-reconvla-s45 | metrics 更新 (conclusion 已自动修正为 success) |
| eval_long_vla_only_seed45.json | **0.575** | eval-supp-long-vla-only-s45 | 已有正确数据，无需更新 |
| eval_long_crm_obs_only_norm0.05_seed45.json | **0.605** | eval-supp-long-crm-norm005-s45 | 已有正确数据，无需更新 |
| eval_long_adaptive_...tau0.25_seed45.json | **0.60** | eval-supp-long-adapt-tau025-s45 | 已有正确数据，无需更新 |
| eval_object_crm_obs_only_norm0.05_seed46.json | **0.795** | eval-supp-obj-crm-norm005-s46 | **新建** + metrics + conclusion=success |
| eval_object_vla_only_seed46.json | **0.79** | eval-supp-obj-vla-only-s46 | 已有正确数据，无需更新 |
| eval_goal_adaptive_...tau0.25_seed45.json | **0.81** | eval-supp-goal-adapt-tau025-s45 | 已有正确数据，无需更新 |

### 未找到的 JSON
- `eval_long_k2mean_seed45.json` — 不存在于 logs/ 目录（registry 中已有来自 bjb2 的数据 SR=0.56）

### 被 cron 误标 failed 已修正：3 个
1. **eval-supp-spatial-k2mean-s46** — SR=0.80，metrics 已补录
2. **eval-supp-reconvla-obj-s45** — SR=0.78，conclusion 已修正为 success
3. **eval-supp-long-reconvla-s45** — SR=0.59，metrics 已补录

### 当前运行中
- Registry 中 RUNNING 状态仅剩 **eval-supp-long-vla-only-s46**
- /tmp 日志显示 GPU 0-3 上有 seed46 系列 Long 评估在跑（adapt/crm/reconvla s46，时间戳 ~11:20 今天）

---
