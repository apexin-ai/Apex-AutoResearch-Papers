# ssh scan deploy bjb1 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302_result.json`
- **Structured JSON:** [`fb4e4fcb241260c03bcf.json`](../../sessions/fb/fb4e4fcb241260c03bcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## bjb1-32546 每卡状态

| GPU | 状态 | 实验 | PID |
|-----|------|------|-----|
| cuda:0 | **新部署** | eval-supp-spatial-k2mean-s46 | 188432 |
| cuda:1 | RUNNING | eval-supp-long-vla-only-s45 | 103128 |
| cuda:2 | RUNNING | eval-supp-long-adapt-tau025-s45 | 103397 |
| cuda:3 | RUNNING | eval-supp-long-crm-norm005-s45 | 103675 |
| cuda:4 | RUNNING | eval-supp-long-reconvla-s45 | 103942 |
| cuda:5 | RUNNING | eval-supp-reconvla-obj-s45 | 172434 |

## cqa1-32758 每卡状态

| GPU | 状态 | 实验 | PID |
|-----|------|------|-----|
| cuda:0 | RUNNING | eval-supp-goal-k2mean-s45 | 456787 |
| cuda:1 | RUNNING | eval-supp-spatial-vla-only-s45 | 456947 |
| cuda:2 | RUNNING | eval-supp-obj-k2mean-s45 | 512632 |
| cuda:3 | RUNNING | eval-supp-spatial-crm-norm005-s45 | 457405 |
| cuda:4 | **RUNNING（已修复）** | eval-supp-spatial-adapt-tau025-s45-r3 | 502821 |
| cuda:5 | RUNNING | eval-supp-spatial-reconvla-s45 | 457485 |

## cuda:4 结论
PID 502816/502821 存活，确实在跑 spatial adaptive_conformal_crm seed45 τ=0.25。进度约 task 8-9/10（已完成 pick_up_the_black_bowl_from_table_center 等任务）。Registry 重建为 `eval-supp-spatial-adapt-tau025-s45-r3`，状态 RUNNING。

## 部署
- **eval-supp-spatial-k2mean-s46** → bjb1-32546 cuda:0, PID 188432, tmux `eval-spatial-k2mean-s46`

## Registry 修复
- `eval-supp-reconvla-obj-s45`：server 从 cqa1-32758 改为 bjb1-32546，gpu 从 cuda:4 改为 cuda:5
- `eval-supp-spatial-adapt-tau025-s45-r3`：新建条目，RUNNING on cqa1-32758 cuda:4

## 已完成未收割
bjb1-32546 上 `eval_object_crm_obs_only_norm0.05_seed46.json`（May 24 06:30, SR=79.5%）和 `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json`（May 24 06:06）是较新的结果文件，可能未被收割。两台服务器均满载运行。

---
