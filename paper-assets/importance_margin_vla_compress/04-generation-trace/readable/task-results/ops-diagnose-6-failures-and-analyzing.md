# ops diagnose 6 failures and analyzing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_6_failures_and_analyzing_20260523T034556_result.json`
- **Structured JSON:** [`742f865bf18502a02d3f.json`](../../sessions/74/742f865bf18502a02d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| exp_id | server | 状态 | SR | 详情 |
|--------|--------|------|----|------|
| eval_pi05_random_k085_goal_seed43 | cqa1-33015 | ✅ 已完成 | 53.4% | libero_goal, random k=0.85, 500ep |
| eval_pi05_l2norm_k085_long_seed43_v2 | westd-38929 | ✅ 已完成 | 79.0% | libero_10, l2norm k=0.85, 500ep |
| eval_pi05_random_k03_long_seed43_v3 | westd-38929 | ✅ 已完成 | 28.4% | libero_10, random k=0.3, 500ep |
| eval_pi05_l2norm_k07_long_seed43_v2 | westd-38929 | ✅ 已完成 | 65.8% | libero_10, l2norm k=0.7, 500ep |
| eval_pi05_random_k085_long_seed43 | westd-41074 | ✅ 已完成 | 41.8% | libero_10, random k=0.85, 500ep |
| eval_pi05_random_k05_long_seed43_v2 | westd-41074 | ✅ 已完成 | 51.2% | libero_10, random k=0.5, 500ep |
| eval_pi05_random_k09_object_seed43_v3 | westd-27271 | ❌ 日志不存在 | — | 在 westd-27271 全盘搜索未找到任何匹配日志文件，实验可能从未启动 |

前 6 个实验 + 1 个 ANALYZING 实验全部在服务重启前已跑完（500/500 episodes），只是被 cron monitor 误标为 failed/ANALYZING。已全部更新为 conclusion=success, status=DONE。

`eval_pi05_random_k09_object_seed43_v3` 需要重新部署。

---
