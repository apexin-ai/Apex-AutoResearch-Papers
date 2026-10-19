# harvest bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827_20260524T032336_result.json`
- **Structured JSON:** [`bce1894ecbf2a58d06bb.json`](../../sessions/bc/bce1894ecbf2a58d06bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## GPU 状态
6× GPU 全部空闲（0% 利用率，0 MiB 显存占用）

## 收割结果

| JSON 文件 | success_rate | exp_id | Registry |
|-----------|-------------|--------|----------|
| `eval_goal_crm_obs_only_norm0.05_seed46.json` | **0.820** | eval-supp-goal-crm-norm005-s46 | ✓ metrics + conclusion=success |
| `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json` | **0.835** (trigger_rate=9.1%) | eval-supp-goal-adapt-tau025-s46 | ✓ metrics + conclusion=success |
| `eval_goal_k2mean_seed46.json` | **0.825** | eval-supp-goal-k2mean-s46 | ✓ metrics + conclusion=success |
| `eval_goal_vla_only_seed46.json` | **0.830** | eval-supp-goal-vla-only-s46 | ✓ metrics + conclusion=success |
| `eval_goal_reconvla_seed46.json` | **0.790** | eval-supp-goal-reconvla-s46 | ✓ metrics + conclusion=success |
| `eval_long_k2mean_seed45.json` | **0.560** | eval-supp-long-k2mean-s45 | ✓ metrics + conclusion=success |

## 磁盘
| 分区 | 用量 |
|------|------|
| `/`（根） | 14G/30G（44%）|
| `/root/autodl-tmp` | 82G/250G（33%）|

6 个被 cron 误标 failed 的实验已全部恢复，metrics 和 conclusion 均已更新到 registry。

---
