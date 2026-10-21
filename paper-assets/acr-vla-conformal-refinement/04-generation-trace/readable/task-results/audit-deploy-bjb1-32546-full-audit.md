# audit deploy bjb1 32546 full audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb1-32546-full-audit_20260523T101221_result.json`
- **Structured JSON:** [`580bcd4f350b006a6154.json`](../../sessions/58/580bcd4f350b006a6154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验已全部注册为 RUNNING。

## 审计结果汇总

**bjb1-32546 全部 6 GPU 占满，无空闲 GPU 可部署新实验。**

| GPU | exp_id | 实验 | 状态 | 运行时长 |
|-----|--------|------|------|---------|
| cuda:0 | eval-supp-adapt-tau025-obj-s43 | Object Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:1 | eval-supp-crm-norm005-goal-s43 | Goal CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:2 | eval-supp-adapt-tau025-goal-s43 | Goal Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:3 | eval-supp-long-vla-only-s42 | Long VLA-only s42 | RUNNING (已注册) | ~48min |
| cuda:4 | eval-supp-crm-norm005-obj-s43 | Object CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:5 | eval-supp-adapt-tau025-goal-s44 | Goal Adaptive tau=0.25 s44 | RUNNING (已注册) | ~1.1h |

**P1 部署选项对照：**
- #1 Long K=2 mean s42 — **无空闲 GPU，无法部署**
- #2 Goal CRM norm=0.05 s43 — **已在 cuda:1 运行**（由之前 Worker 启动）
- #3 Goal Adaptive tau=0.25 s43 — **已在 cuda:2 运行**（由之前 Worker 启动）
- #4 Goal Reconvla s44 — **无空闲 GPU，无法部署**

已为 cuda:0/1/2/4 上的 4 个未注册实验补建了 registry 条目（RUNNING）。这些实验预计还需 ~10-12h 完成（20 rollouts × 10 tasks 的 eval 通常需 12-14h）。

---
